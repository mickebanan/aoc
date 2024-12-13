class Instruction:
    opcode = None
    length = None

    @classmethod
    def take_two(cls, machine, parameters):
        p1, p2 = machine.program[machine.pc + 1], machine.program[machine.pc + 2]
        if parameters[-1] == '2':
            p1 += machine.relative_base
        elif parameters[-1] == '1':
            p1 = machine.pc + 1
        if parameters[-2] == '2':
            p2 += machine.relative_base
        elif parameters[-2] == '1':
            p2 = machine.pc + 2
        return p1, p2

    @classmethod
    def take_three(cls, machine, parameters):
        p1, p2 = cls.take_two(machine, parameters)
        pv = machine.program[machine.pc + 3]
        if parameters[0] == '2':
            pv += machine.relative_base
        return p1, p2, pv

    @classmethod
    def execute(cls, machine, parameters):
        pass


class AddInstruction(Instruction):
    opcode, length = 1, 4

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        p1, p2, pv = cls.take_three(machine, parameters)
        v1 = machine.program[p1]
        v2 = machine.program[p2]
        machine.program[pv] = v1 + v2
        machine.log(' Add: values %s and %s, saving %s to position %s' % (v1, v2, v1 + v2, pv))
        machine.pc += cls.length


class MulInstruction(Instruction):
    opcode, length = 2, 4

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        p1, p2, pv = cls.take_three(machine, parameters)
        v1 = machine.program[p1]
        v2 = machine.program[p2]
        machine.program[pv] = v1 * v2
        machine.log(' Multiply: values %s and %s, saving %s to position %s' % (v1, v2, v1 * v2, pv))
        machine.pc += cls.length


class InputInstruction(Instruction):
    opcode, length = 3, 2

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        pv = machine.program[machine.pc + 1]
        if parameters[-1] == '2':
            pv += machine.relative_base
        if not machine.inputs:
            machine.waiting = True
            machine.log('Awaiting input')
            return
        value = machine.inputs.pop(0)
        machine.program[pv] = int(value)
        machine.log(' Input, value: %s, saved to position %s' % (value, machine.pc + 1 + machine.relative_base
                                                                 if parameters[-1] == '2' else machine.pc + 1))
        machine.pc += cls.length


class OutputInstruction(Instruction):
    opcode, length = 4, 2

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        if parameters[-1] == '0':
            pv = machine.program[machine.program[machine.pc + 1]]
        elif parameters[-1] == '1':
            pv = machine.program[machine.pc + 1]
        else:
            pv = machine.program[machine.pc + 1 + machine.relative_base]
        machine.log(' Output, value: %s, from position %s'
                    % (pv, machine.program[machine.pc + 1] if parameters[-1] == '0' else machine.pc + 1))
        machine.pc += cls.length
        return pv


class JumpIfTrueInstruction(Instruction):
    opcode, length = 5, 3

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        p1, p2 = cls.take_two(machine, parameters)
        v1 = machine.program[p1]
        v2 = machine.program[p2]
        if v1 != 0:
            machine.pc = v2
            machine.log(' Jump if true: %s is not zero, jumping to %s' % (v1, v2))
        else:
            machine.pc += cls.length
            machine.log(' Jump if true: %s is zero, moving forward' % v1)


class JumpIfFalseInstruction(Instruction):
    opcode, length = 6, 3

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        p1, p2 = cls.take_two(machine, parameters)
        v1 = machine.program[p1]
        v2 = machine.program[p2]
        if v1 == 0:
            machine.pc = v2
            machine.log(' Jump if false: %s is zero, jumping to %s' % (v1, v2))
        else:
            machine.pc += cls.length
            machine.log(' Jump if false: %s is not zero, moving forward' % v1)


class LessThanInstruction(Instruction):
    opcode, length = 7, 4

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        p1, p2, pv = cls.take_three(machine, parameters)
        v1 = machine.program[p1]
        v2 = machine.program[p2]
        machine.program[pv] = 1 if v1 < v2 else 0
        machine.log(' Less than: %s < %s, saving %s to position %s' % (v1, v2, 1 if v1 < v2 else 0, pv))
        machine.pc += cls.length

class EqualsInstruction(Instruction):
    opcode, length = 8, 4

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        p1, p2, pv = cls.take_three(machine, parameters)
        v1 = machine.program[p1]
        v2 = machine.program[p2]
        machine.program[pv] = 1 if v1 == v2 else 0
        machine.log(' Equals %s == %s, saving %s to position %s' % (v1, v2, 1 if v1 == v2 else 0, pv))
        machine.pc += cls.length


class RelativeBaseOffsetInstruction(Instruction):
    opcode, length = 9, 2

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        p1 = machine.program[machine.pc + 1]
        if parameters[-1] == '0':
            v1 = machine.program[p1]
        elif parameters[-1] == '1':
            v1 = p1
        else:
            v1 = machine.program[p1 + machine.relative_base]
        machine.log(' Adjust relative base with %s (%s) in %s' % (p1, machine.relative_base, v1))
        machine.relative_base += v1
        machine.log(' New relative base:', machine.relative_base)
        machine.pc += cls.length


class HaltInstruction(Instruction):
    opcode, length = 99, 1

    @classmethod
    def execute(cls, machine, parameters):
        machine.log_instruction(cls)
        machine.log(' Halting program')
        machine.halted = True


class IntCode:
    def __init__(self, program, inputs=None, debug=False, memory=10000):
        self.program = program[:]
        if not isinstance(self.program, list):
            self.program = [int(a) for a in self.program.split(',')]
        self.debug = debug
        self.inputs = [int(a) for a in inputs] if inputs else []
        self.log_program()
        self.log('inputs:', self.inputs)
        self.program.extend([0] * memory)
        self.halted = False
        self.waiting = False
        self.pc = 0  # Program counter
        self.relative_base = 0

    @staticmethod
    def _get_instruction(opcode):
        return next(instr for instr in Instruction.__subclasses__() if opcode == instr.opcode)

    def get(self, i):
        # Get the program instruction from the given position.
        return self.program[i]

    def input(self, a):
        # Add an item to the input list.
        self.inputs = self.inputs + [int(a)]
        self.waiting = False

    def log(self, *s):
        if self.debug:
            print(*s)

    def log_instruction(self, instruction):
        s = ' '.join(str(a) for a in self.program[self.pc:self.pc + instruction.length])
        self.log('[%s]' % s)

    def log_program(self):
        if not self.debug:
            return
        pc = 0
        while pc < len(self.program):
            instr = self.program[pc]
            opcode = int((('00000' + str(instr))[-5:])[3:])
            # opcode = int(opcode[3:])
            if opcode in (1, 2, 7, 8):
                ln = 4
            elif opcode in (3, 4, 9):
                ln = 2
            elif opcode in (5, 6):
                ln = 3
            elif opcode == 99:
                ln = 1
            else:
                ln = 5
            for i in range(ln):
                print('%s ' % self.program[pc + i], end='')
            pc += ln
            print()

    def run(self):
        while True:
            if self.halted:
                break
            output = self.parse()
            if output is not None:
                return output
            if self.waiting:
                return

    def parse(self):
        opcode = self.program[self.pc]
        opcode = ('00000' + str(opcode))[-5:]
        parameters, opcode = opcode[:3], opcode[3:]
        opcode = int(opcode)
        instr = self._get_instruction(opcode)
        value = instr.execute(self, parameters)
        return value


if __name__ == '__main__':
    # Unit tests for the machine (incomplete).
    # Addition, pointer
    p = [1, 5, 6, 3, 99, 10, 5]
    m = IntCode(p, debug=True)
    m.run()
    assert m.program[3] == (10 + 5)
    # Addition, direct
    p = [1101, 10, 20, 3, 99]
    m = IntCode(p, debug=True)
    m.run()
    assert m.program[3] == (10 + 20)
    # Multiplication, pointer
    p = [2, 5, 6, 3, 99, 10, 5]
    m = IntCode(p, debug=True)
    m.run()
    assert m.program[3] == (10 * 5)
    # Multiplication, direct
    p = [1102, 10, 20, 3, 99]
    m = IntCode(p, debug=True)
    m.run()
    assert m.program[3] == (10 * 20)
    # Input
    p = [3, 1, 99]
    m = IntCode(p, debug=True, inputs=[5])
    m.run()
    assert m.program[1] == 5
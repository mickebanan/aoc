import time


def timer(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        r = f(*args, **kwargs)
        print(f'Function {f.__name__} executed in {(time.time() - t):.3f} s')
        return r
    return wrapper


def transpose(m, as_list=False):
    _m = []
    for i in range(len(m[0])):
        r = []
        for row in m:
            r.append(row[i])
        if as_list:
            _m.append(r)
        else:
            _m.append(''.join(r))
    return _m


def pp(m):
    print('vvv')
    for row in m:
        if isinstance(row, list):
            print(''.join(row))
        else:
            print(row)
    print('^^^')
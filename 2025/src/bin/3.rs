fn main() {
    let data = std::fs::read_to_string("data/3.dat").unwrap();
    let mut p1: Vec<u128> = Vec::new();
    let mut p2: Vec<u128> = Vec::new();
    for line in data.lines() {
        p1.push(get_biggest_k(&line, 2));
        p2.push(get_biggest_k(&line, 12));
    }
    println!("part 1: {}", p1.iter().sum::<u128>());
    println!("part 2: {}", p2.iter().sum::<u128>());
}

fn get_biggest_k(line: &str, k: usize) -> u128 {
    let mut drop = line.len() - k;
    let mut stack: Vec<u8> = Vec::with_capacity(k);
    for c in line.chars() {
        let v = c.to_digit(10).unwrap() as u8;
        while drop > 0 && !stack.is_empty() && *stack.last().unwrap() < v {
            stack.pop();
            drop -= 1;
        }
        stack.push(v);
    }
    if drop > 0 {
        let new_len = stack.len() - drop;
        stack.truncate(new_len);
    }
    let mut res: u128 = 0;
    for v in stack {
        res = res * 10 + v as u128;
    }
    res
}
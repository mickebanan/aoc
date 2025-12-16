fn reduce(op: char, iter: impl Iterator<Item = u64>) -> u64 {
    match op {
        '+' => iter.sum(),
        '*' => iter.product(),
        _ => unreachable!("unknown operator: {op}"),
    }
}

fn main() {
    let data = std::fs::read_to_string("data/6.dat").unwrap();
    let lines: Vec<&str> = data.lines().collect();
    let mut grid: Vec<Vec<u64>> = Vec::new();
    for line in &lines[..lines.len() - 1] {
        grid.push(line
            .split_whitespace()
            .map(|v| v.parse::<u64>().unwrap())
            .collect());
    }
    let ops: Vec<char> = lines.last()
        .unwrap()
        .split_whitespace()
        .map(|s| s.chars().next().unwrap())
        .collect();
    let ymax = grid.len();
    let xmax = grid[0].len();
    // part 1
    let p1: u64 = (0..xmax)
        .zip(ops.iter().copied())
        .map(|(x, op)| reduce(op, (0..ymax).map(|y| grid[y][x])))
        .sum();
    println!("part 1: {p1}");
    // part 2
    let ymax = lines.len() - 1;
    let xmax = lines[0].len();
    let mut p2: u64 = 0;
    let mut ops_iter_rev = ops.iter().rev();
    let mut values: Vec<u64> = Vec::new();
    for x in (0..xmax).rev() {
        let mut value = String::new();
        for y in 0..ymax {
            let c = lines[y].chars().nth(x).unwrap();
            if c != ' ' {
                value.push(c);
            }
        }
        if value.len() > 0 {
            values.push(value.parse::<u64>().unwrap());
        } else {
            let op = ops_iter_rev.next().unwrap();
            p2 += reduce(*op, values.drain(..));
        }
    }
    let op = ops_iter_rev.next().unwrap();
    p2 += reduce(*op, values.into_iter());
    println!("part 2: {p2}");
}
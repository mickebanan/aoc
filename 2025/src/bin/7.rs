use std::collections::HashMap;

fn main() {
    let data = std::fs::read_to_string("data/7.dat").unwrap();
    let mut splits = 0;
    let lines: Vec<&str> = data.lines().collect();
    let mut paths: HashMap<usize, usize> = HashMap::new();
    paths.insert(lines[0].chars().position(|c| c == 'S').unwrap(), 1);
    for line in lines[1..].iter() {
        for (x, c) in line.chars().enumerate() {
            if c == '^' {
                if let Some(v) = paths.remove(&x) {
                    if x > 0 {
                        *paths.entry(x - 1).or_insert(0) += v;
                    }
                    *paths.entry(x + 1).or_insert(0) += v;
                    splits += 1;
                }
            }
        }
    }
    println!("part 1: {splits}");
    println!("part 2: {}", paths.values().sum::<usize>());
}

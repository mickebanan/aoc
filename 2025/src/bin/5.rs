fn main() {
    let data = std::fs::read_to_string("data/5.dat").unwrap();
    let mut intervals: Vec<(u64, u64)> = Vec::new();
    let mut tests: Vec<u64> = Vec::new();
    let mut p1 = 0;
    for line in data.lines() {
        if line.contains("-") {
            let (start, end) = line.split_once("-").unwrap();
            intervals.push((start.parse().unwrap(), end.parse().unwrap()));
        } else if !line.is_empty() {
            tests.push(line.parse::<u64>().unwrap());
        }
    }
    for test in &tests {
        for (start, end) in &intervals {
            if start <= test && test <= end {
                p1 += 1;
                break;
            }
        }
    }
    let mut new_intervals: Vec<(u64, u64)> = Vec::new();
    intervals.sort_by_key(|v| v.0);
    for (start, end) in intervals {
        match new_intervals.last_mut() {
            None => new_intervals.push((start, end)),
            Some((_, last_end)) => {
                if start <= *last_end {
                    *last_end = (*last_end).max(end);
                } else {
                    new_intervals.push((start, end));
                }
            }
        }
    }
    println!("part 1: {p1}");
    println!("part 2: {}", new_intervals.iter().map(|(s, e)| e - s + 1).sum::<u64>());
}
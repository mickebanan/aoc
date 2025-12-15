fn main() {
    let data = std::fs::read_to_string("data/2.dat").unwrap();
    let mut p1: u64 = 0;
    let mut p2: u64 = 0;
    for interval in data.split(",") {
        let (start, stop) = interval.split_once("-").unwrap();
        let start: u64 = start.parse().unwrap();
        let stop: u64 = stop.parse().unwrap();
        for e in start..=stop {
            let es = e.to_string();
            if is_repeated_1(&es) {
                p1 += e;
            }
            if is_repeated_2(&es) {
                p2 += e;
            }
        }
    }
    println!("part 1: {p1}");
    println!("part 2: {p2}");
}

fn is_repeated_1(s: &str) -> bool {
    let (left, right) = s.split_at(s.len() / 2);
    left == right
}

fn is_repeated_2(s: &str) -> bool {
    let doubled = format!("{}{}", s, s);
    doubled[1..(2 * s.len() - 1)].contains(s)
}
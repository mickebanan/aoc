fn main() {
    let data = std::fs::read_to_string("data/1.dat").unwrap();
    let mut pos = 50;
    let mut count = 0;
    for item in data.lines() {
        let (dir, len) = item.split_at(1);
        let length: i32 = len.parse().unwrap();
        pos = (pos - if dir == "L" {-length} else {length}).rem_euclid(100);
        count += if pos == 0 {1} else {0};
    }
    println!("part 1: {count}");
    
    let mut pos = 50;
    let mut count = 0;
    for item in data.lines() {
        let (dir, len) = item.split_at(1);
        let length: i32 = len.parse().unwrap();
        count += length / 100;
        let rest = length % 100;
        let new = pos + if dir == "L" {-rest} else {rest};
        count += match new {
            v if dir == "L" && pos != 0 && v <= 0 => 1,
            v if dir == "R" && pos != 0 && v >= 100 => 1,
            _ => 0,
        };
        pos = match new {
            v if v <= 0 => (100 + v) % 100,
            v if v >= 100 => (new - 100) % 100,
            v => v,
        };
    }
    println!("part 2: {count}");
}
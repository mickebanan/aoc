fn main() {
    let mut data: Vec<Vec<u8>> = std::fs::read_to_string("data/4.dat")
        .unwrap().lines().map(|line| line.as_bytes().to_vec()).collect();
    let ymax = data.len() as isize;
    let xmax = data[0].len() as isize;
    let mut p1 = 0;
    let mut p2 = 0;
    let mut first = true;
    loop {
        let mut changed = false;
        let mut new_data = data.clone();
        for y in 0..ymax {
            for x in 0..xmax {
                if data[y as usize][x as usize] == b'@' {
                    if neighbors(y, x, &data, ymax, xmax) < 4 {
                        if first {
                            p1 += 1;
                        }
                        p2 += 1;
                        new_data[y as usize][x as usize] = b'.';
                        changed = true;
                    }
                }
            }
        }
        first = false;
        data = new_data;
        if !changed {
            break;
        }
    }
    println!("part 1: {}", p1);
    println!("part 2: {}", p2);
}

fn neighbors(y: isize, x: isize, data: &Vec<Vec<u8>>, ymax: isize, xmax: isize) -> u8 {
    let mut neighbors = 0;
    let dirs: [(isize, isize); 8] = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ];
    for (dy, dx) in dirs {
        let ny = y + dy;
        let nx = x + dx;
        if ny >= ymax || ny < 0 || nx >= xmax || nx < 0 {
            continue;
        }
        if data[ny as usize][nx as usize] == b'@' {
            neighbors += 1;
        }
    }
    neighbors
}

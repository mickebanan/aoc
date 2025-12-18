struct Rectangle {
    xmin: i64,
    xmax: i64,
    ymin: i64,
    ymax: i64,
    area: i64,
}

fn main() {
    let data = std::fs::read_to_string("data/9.dat").unwrap();
    let nodes: Vec<(i64, i64)> = data.lines()
        .map(|x| x.split_once(',')
            .map(|(x,y)| {
                (x.parse::<i64>().unwrap(), y.parse::<i64>().unwrap())
            }).unwrap())
        .collect();
    let mut rectangles = Vec::new();
    for (i, (x1, y1)) in nodes.iter().enumerate() {
        for (x2, y2) in nodes.iter().skip(i + 1) {
            let r = Rectangle {
                xmin: *x1.min(x2),
                xmax: *x1.max(x2),
                ymin: *y1.min(y2),
                ymax: *y1.max(y2),
                area: area(&(*x1, *y1), &(*x2, *y2)),
            };
            rectangles.push(r);
        }
    }
    rectangles.sort_by_key(|r| std::cmp::Reverse(r.area));
    println!("part 1: {:?}", rectangles[0].area);
    let mut edges: Vec<((i64, i64), (i64, i64))> = nodes.windows(2)
        .map(|w| (w[0], w[1])).collect();
    if let (Some(&last), Some(&first)) = (nodes.last(), nodes.first()) {
        edges.push((last, first));
    }
    for rect in rectangles.iter() {
        if is_contained(&rect, &edges) {
            println!("part 2: {}", rect.area);
            break;
        }
    }
}

fn area(a: &(i64, i64), b: &(i64, i64)) -> i64 {
    ((a.0 - b.0).abs() + 1) * ((a.1 - b.1).abs() + 1)
}

fn overlap(a0: &i64, a1: &i64, b0: &i64, b1: &i64) -> bool {
    let (a0, a1) = if a0 <= a1 { (a0, a1) } else { (a1, a0) };
    let (b0, b1) = if b0 <= b1 { (b0, b1) } else { (b1, b0) };
    a0 <= b1 && b0 <= a1
}

fn intersects(a: &(i64, i64), b: &(i64, i64), r: &Rectangle) -> bool {
    let (x1, y1) = a;
    let (x2, y2) = b;
    if x1 == x2 {
        x1 > &r.xmin && x1 < &r.xmax && overlap(y1, y2, &r.ymin, &r.ymax)
    } else {
        y1 > &r.ymin && y1 < &r.ymax && overlap(x1, x2, &r.xmin, &r.xmax)
    }
}

fn is_contained(r: &Rectangle, edges: &Vec<((i64, i64), (i64, i64))>) -> bool {
    if edges.iter().any(|(a, b)| intersects(a, b, r)) {
        return false;
    }
    true
}

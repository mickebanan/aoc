use std::collections::HashMap;

fn main() {
    /* Visade sig vara mycket lättare i praktiken än vad det verkade,
     * för man behövde inte pussla med bitarna överhuvudtaget. Tack och god jul!
     */
    let data = std::fs::read_to_string("data/12.dat").unwrap();
    let mut shapes = HashMap::new();
    let mut regions: Vec<&str> = Vec::new();
    for stuff in data.split("\n\n") {
        if !stuff.contains("x") {
            let kv = stuff.split("\n").collect::<Vec<&str>>();
            shapes.insert(kv[0].strip_suffix(":").unwrap().parse::<usize>().unwrap(),
                          kv[1..].to_vec());
        } else {
            regions.extend(stuff.split("\n").collect::<Vec<&str>>());
        }
    }
    let mut p1 = 0;
    for region in regions {
        let (wh, packages) = split_region(region);
        let area = area_region(wh);
        let required_area = packages.iter().enumerate()
            .map(|(i, &package)| {
                let shape = shapes.get(&i).unwrap();
                area_shape(shape) * package
            }).sum();
        if area > required_area { p1 += 1 }
    }
    println!("p1: {}", p1);
}

fn split_region(region: &str) -> (&str, Vec<usize>){
    let (wh, packages) = region.split_once(":").unwrap();
    let packages = packages.split_whitespace()
        .map(|v| v.parse::<usize>().unwrap())
        .collect::<Vec<usize>>();
    (wh, packages)
}

fn area_region(wh: &str) -> usize {
    wh.split("x").map(|v| v.parse::<usize>().unwrap()).product()
}

fn area_shape(shape: &Vec<&str>) -> usize {
    shape.iter()
        .flat_map(|row| row.chars())
        .filter(|c| *c == '#')
        .count()
}
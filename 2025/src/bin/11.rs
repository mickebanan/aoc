use std::collections::HashMap;

#[derive(Copy, Clone)]
struct Devices {
    dac: bool,
    fft: bool,
    check: bool,
}

impl Devices {
    fn accept(&self) -> bool {
        !self.check || (self.fft && self.dac)
    }

    fn do_check(mut self, location: &str) -> Self {
        if self.check {
            match location {
                "dac" => self.dac = true,
                "fft" => self.fft = true,
                _ => {}
            }
        }
        self
    }

    fn get_key(&self) -> u8 {
        if !self.check {
            return 0;
        }
        (self.dac as u8) | ((self.fft as u8) << 1)
    }
}

fn main() {
    let data = std::fs::read_to_string("data/11.dat").unwrap();
    let mut connections = HashMap::new();
    for line in data.lines() {
        let (from, to) = line.split_once(':').unwrap();
        let tos = to.split_whitespace().collect::<Vec<_>>();
        connections.insert(from, tos);
    }
    let d = Devices {dac: false, fft: false, check: false};
    let mut cache = HashMap::new();
    println!("part 1: {:?}", find_circuits(&connections, "you", d, &mut cache));
    let d = Devices {dac: false, fft: false, check: true};
    let mut cache = HashMap::new();
    println!("part 2: {:?}", find_circuits(&connections, "svr", d, &mut cache));
}

fn find_circuits<'a>(connections: &HashMap<&str, Vec<&'a str>>,
                     location: &'a str,
                     devices: Devices,
                     cache: &mut HashMap<(&'a str, u8), usize>) -> usize {
    let devices = devices.do_check(&location);
    let key = (location, devices.get_key());
    if let Some(ans) = cache.get(&key) {
        return *ans;
    }
    let ans = if location == "out" {
        if devices.accept() { 1 } else { 0 }
    } else {
        connections
            .get(location)
            .map(|outs| {
                outs.iter()
                    .map(|next| find_circuits(connections, *next, devices, cache))
                    .sum()
            })
            .unwrap_or(0)
    };
    cache.insert(key, ans);
    ans
}
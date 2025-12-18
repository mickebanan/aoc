struct Point {x: i64, y: i64, z: i64}

struct Edge {u: usize, v: usize, dist: u64}

struct Dsu {  // Disjoint set union
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl Dsu {
    fn n_largest_component_sizes(&mut self, n: usize) -> Vec<usize> {
        let mut sizes: Vec<usize> = (0..self.parent.len())
            .map(|i| self.find(i))
            .collect::<std::collections::HashSet<_>>()
            .into_iter()
            .map(|r| self.size[r])
            .collect();
        sizes.sort_by(|a, b| b.cmp(a));
        sizes.truncate(n);
        sizes
    }

    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            size: vec![1; n],
        }
    }

    fn find(&mut self, u: usize) -> usize {
        if self.parent[u] != u {
            self.parent[u] = self.find(self.parent[u]);
        }
        self.parent[u]
    }

    fn union(&mut self, x: usize, y: usize) -> bool {
        let root_x = self.find(x);
        let root_y = self.find(y);
        if root_x == root_y {
            return false;
        }
        self.parent[root_y] = root_x;
        self.size[root_x] += self.size[root_y];
        true
    }
}

fn main() {
    let data = std::fs::read_to_string("data/8.dat").unwrap();
    let points = data.lines()
        .map(|line| {
            let mut it = line.split(',').map(|s| s.parse::<i64>().unwrap());
            Point { x: it.next().unwrap(), y: it.next().unwrap(), z: it.next().unwrap() }
        }).collect::<Vec<Point>>();
    let mut edges: Vec<Edge> = points.iter().enumerate()
        .flat_map(|(i, p)| points.iter().enumerate().skip(i + 1)
            .map(move |(j, q)| Edge {u: i, v: j, dist: distance2(&p, &q)}))
        .collect();
    edges.sort_by_key(|edge| edge.dist);
    let (mut dsu, _) = kruskal(points.len(), &edges, 1000);
    let p1 = &dsu.n_largest_component_sizes(3);
    println!("part 1: {}", p1.iter().product::<usize>());
    let (_, last) = kruskal(points.len(), &edges, usize::MAX);
    println!("part 2: {}", points[last.0].x * points[last.1].x);
}

fn distance2(a: &Point, b: &Point) -> u64 {
    (a.x - b.x).pow(2) as u64 + (b.y - a.y).pow(2) as u64 + (b.z - a.z).pow(2) as u64
}

fn kruskal(n: usize, edges: &Vec<Edge>, limit: usize) -> (Dsu, (usize, usize)) {
    let mut dsu = Dsu::new(n);
    let mut count = 0;
    let mut last: (usize, usize) = (0, 0);
    for edge in edges {
        if count >= limit {
            break;
        }
        if dsu.union(edge.u, edge.v) {
            last = (edge.u, edge.v);
        }
        count += 1;
    }
    (dsu, last)
}
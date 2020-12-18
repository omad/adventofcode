use std::collections::HashSet;

fn main() {
    let content = std::fs::read_to_string("day17.input").expect("Couldn't read file");

    let mut active_elements: HashSet<(i32, i32, i32)> = HashSet::new();

    for (y, line) in content.lines().enumerate() {
        for (x, ch) in line.chars().enumerate() {
            if ch == '#' {
                println!("{}, {}", x, y);
                active_elements.insert((x as i32, y as i32, 0));
            }
        }
    }

    println!("initial_state: {:?}", active_elements);

//    println!("neighbours test: {:#?}", neighbours((0, 0, 0)));

    let mut state = active_elements;
    for i in 0..6 {
        println!("{}", i);
        state = step(&state);
//        println!("{:?}", state);
    }

    println!("{}", state.len());

}

fn step(state: &HashSet<(i32, i32, i32)>) -> HashSet<(i32, i32, i32)> {
    let mut next: HashSet<(i32, i32, i32)> = HashSet::new();

    let bound = bounds(&state);
    println!("bounds: {:?}", bound);
    let ((min_x, max_x), (min_y, max_y), (min_z, max_z)) = bound;

    for x in min_x - 1 .. max_x + 2 {
        for y in min_y - 1 .. max_y + 2 {
            for z in min_z - 1 .. max_z + 2 {
                let point = (x, y, z);
                let neighbours = neighbours(point);
                let active_neighbours: usize = state.intersection(&neighbours).count();
                let is_active = state.contains(&point);

                if is_active {
                    if active_neighbours == 2 || active_neighbours == 3 {
                        next.insert(point);
                    }
                } else {
                    if active_neighbours == 3 {
                        next.insert(point);
                    }
                }
            }
        }
    }

    next
}

fn bounds(state: &HashSet<(i32, i32, i32)>) -> ((i32, i32), (i32, i32), (i32, i32)) {
    let (mut min_x, mut min_y, mut min_z): (i32, i32, i32) = (0, 0, 0);
    let (mut max_x, mut max_y, mut max_z): (i32, i32, i32) = (0, 0, 0);

    for &(x, y, z) in state.iter() {
        if x < min_x {min_x = x}
        if x > max_x {max_x = x}
        if y < min_y { min_y = y }
        if y > max_y { max_y = y }
        if z < min_z { min_z = z }
        if z > max_z { max_z = z }

    }
    ((min_x, max_x), (min_y, max_y), (min_z, max_z))

}

fn neighbours(point: (i32, i32, i32)) -> HashSet<(i32, i32, i32)> {
    let (ox, oy, oz) = point;
    let mut neighbours = HashSet::new();
    for x in ox-1 .. ox+2 {
        for y in oy-1 .. oy+2 {
            for z in oz-1 .. oz+2 {
                neighbours.insert((x, y, z));

            }
        }
    }
    neighbours.remove(&point);
    neighbours
}

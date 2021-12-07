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

    let mut state = active_elements.clone();
    for i in 0..6 {
        println!("{}", i);
        state = step(&state);
//        println!("{:?}", state);
    }

    println!("{}", state.len());

    let mut state4: HashSet<(i32, i32, i32, i32)> = active_elements.iter().map(|&(x, y, z)| (x, y, z, 0)).collect();

    for i in 0..6 {

        println!("{}", i);
        state4 = step4(&state4);
    }

    println!("{}", state4.len());

}

fn step(state: &HashSet<(i32, i32, i32)>) -> HashSet<(i32, i32, i32)> {
    let mut next: HashSet<(i32, i32, i32)> = HashSet::new();


    let potential_changes: HashSet<(i32, i32, i32)> = state.iter().fold(state.clone(), |mut all, point| {all.extend(neighbours(*point)); all});

    for &point in potential_changes.iter() {
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

    next
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

fn step4(state: &HashSet<(i32, i32, i32, i32)>) -> HashSet<(i32, i32, i32, i32)> {
    let mut next: HashSet<(i32, i32, i32, i32)> = HashSet::new();


    let potential_changes: HashSet<(i32, i32, i32, i32)> = state.iter().fold(state.clone(), |mut all, point| {all.extend(neighbours4(*point)); all});

    for &point in potential_changes.iter() {
        let neighbours = neighbours4(point);
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

    next
}


fn neighbours4(point: (i32, i32, i32, i32)) -> HashSet<(i32, i32, i32, i32)> {
    let (ox, oy, oz, ow) = point;
    let mut neighbours = HashSet::new();
    for x in ox-1 .. ox+2 {
        for y in oy-1 .. oy+2 {
            for z in oz-1 .. oz+2 {
                for w in ow-1 .. ow+2 {
                    neighbours.insert((x, y, z, w));
                }

            }
        }
    }
    neighbours.remove(&point);
    neighbours
}

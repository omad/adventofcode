

fn main() {
    let content = std::fs::read_to_string("day3.input").expect("Couldn't read file");

    let mut x = 0;
    let mut collided_trees = 0;
    for line in content.lines() {

        let is_tree = line.chars().nth(x % line.len()) == Some('#');
        if is_tree {
            collided_trees += 1;
        }
        x += 3;

    }
    println!("{}", collided_trees);

    let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    let mut product: u64 = 1;
    for slope in slopes.iter() {
        let mut collided_trees = 0;
        let mut x = 0;
        let (dx, dy) = slope;

        for line in content.lines().step_by(*dy) {

            let is_tree = line.chars().nth(x % line.len()) == Some('#');
            if is_tree {
                collided_trees += 1;
            }
            x += dx;

        }
        println!("Slope: ({}, {}) Collided:{}", dx, dy, collided_trees);
        product *= collided_trees;

    }
    println!("{}", product);

}

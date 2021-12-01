// use std::fs::File;
use itertools::Itertools;

fn main() {
    let content = std::fs::read_to_string("day1.input").expect("Couldn't read file");

    let mut nums: Vec<u32> = vec![];

    for line in content.lines() {
        nums.push(line.parse().unwrap());
    }

    'outer: for i in 0 .. nums.len() {
        for j in i .. nums.len() {
            if nums[i] + nums[j] == 2020 {

                println!("{}", nums[i] * nums[j]);
                break 'outer;
            }
        }
    }

    for pair in nums.iter().combinations(2) {
        let x = pair[0];
        let y = pair[1];
        if x + y == 2020 {
            println!("{}", x * y);
            break;
        }
    }
    for triple in nums.iter().combinations(3) {
        let x = triple[0];
        let y = triple[1];
        let z = triple[2];
        if x + y + z == 2020 {
            println!("{}", x * y * z);
            break;
        }
    }


    println!("Hello, world!");
}

use itertools::Itertools;

fn main() {

    let content = std::fs::read_to_string("day9.input").expect("Couldn't read file");

    let nums: Vec<u64> = content
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    let mut chosen = 0;

    // Part #1
    for (i, num) in nums.iter().enumerate() {
        print!("{}: {}", i, num);
        if i <= 25 {
            println!(" skipped.");
            continue;
        }
        let valid: bool = nums[i-25..i].iter()
            .tuple_combinations::<(_, _)>()
            .any(|(a, b)| a + b == *num);

        if valid {
            println!(" valid.");
        } else {
            println!(" invalid.");
            chosen = *num;
            break;
        }
    }

    for size in 2..nums.len() {
        for window in nums.windows(size) {
            let sum: u64 = window.iter().sum();
            if sum == chosen {
                let min: &u64 = window.iter().min().unwrap();
                let max: &u64 = window.iter().max().unwrap();
                println!("Part 2: {}", min + max);
                return;
            }
        }
    }
}

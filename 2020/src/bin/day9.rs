use itertools::Itertools;

fn main() {

    let content = std::fs::read_to_string("day9.input").expect("Couldn't read file");

    let nums: Vec<u64> = content
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

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
            break;
        }


    }
}

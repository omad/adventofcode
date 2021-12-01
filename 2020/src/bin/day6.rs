use std::collections::HashSet;
use std::iter::FromIterator;

fn main() {
    let content = std::fs::read_to_string("day6.input").expect("Couldn't read file");

    let mut any_count: usize = 0;
    let mut all_count: usize = 0;
    for group in content.split("\n\n") {

        // Part One
        let group_contents = group
            .chars()
            .filter(|c| c.is_ascii_alphabetic() );

        let group_responses: HashSet<char> = HashSet::from_iter(group_contents);

        any_count += group_responses.len();

        // Part Two
        let mut all_answered: HashSet<char> = HashSet::from_iter("abcdefghijklmnopqrstuvwxyz".chars());
        for line in group.lines() {
            let answers: HashSet<char> = HashSet::from_iter(line.chars());
            all_answered = all_answered.intersection(&answers).cloned().collect();
        }

        all_count += all_answered.len();

    }
    println!("Sum of counts where anyone answered yes {}", any_count);
    println!("Sum of counts where everyone answered yes {}", all_count);
}


use std::convert::TryInto;
use std::collections::HashMap;

fn main() {
    let starting_nums = [0,3,6];
    let last_spoken = play_game(&starting_nums, 10);
    println!("{:?}: {}", starting_nums, last_spoken);

//    let starting_nums = [1,3,2];
//    let last_spoken = play_game(&starting_nums, 2020);
//    println!("{:?}: {}", starting_nums, last_spoken);
//
//    let starting_nums = [19,20,14,0,9,1];
//    let last_spoken = play_game(&starting_nums, 2020);
//    println!("{:?}: {}", starting_nums, last_spoken);
}

fn play_game(starting_nums: &[i32], iters: usize) -> i32 {

    let mut when_said: HashMap<i32, usize> = HashMap::new();
    let mut last_spoken = 0;

    for turn in 0..iters+1 {
        if turn < starting_nums.len() {
            last_spoken = starting_nums[turn];
            when_said.insert(last_spoken, turn);
        } else {
            match when_said.get(&last_spoken) {
                Some(the_turn) => {
                    if the_turn == turn - 1 {
                        last_spoken = 0
                    } else {

                    }
                    last_spoken = (turn - the_turn).try_into().unwrap();
                    when_said.insert(last_spoken, turn);
                },
                None => {
                    last_spoken = 0;
                    when_said.insert(last_spoken, turn);
                }
            }
        }
        println!("Turn: {}, num spoken: {}", turn + 1, last_spoken)
    }
    last_spoken
}

use std::collections::HashSet;

#[derive(Debug, Clone)]
enum Op {
    Jmp(i32),
    Nop(i32),
    Acc(i32)
}

fn main() {

    let content = std::fs::read_to_string("day8.input").expect("Couldn't read file");

    let program: Vec<Op> = content.lines().map(
        |line| {
            let num:i32 = line.split(' ').skip(1).next().unwrap().parse().unwrap();
            match &line[0..3] {
                "nop" => Op::Nop(num),
                "acc" => Op::Acc(num),
                "jmp" => Op::Jmp(num),
                _ => unreachable!()

            }
        }
    ).collect();

    let result = run_program(&program);
    match result {
        Ok(acc) => println!("Program wasn't supposed to succeed here! acc: {}", acc),
        Err(acc) => println!("acc: {}", acc)
    };

    for (i, op) in program.iter().enumerate() {
        let mut new_prog = program.clone();

        match op {
            Op::Nop(num) => new_prog[i] = Op::Jmp(*num),
            Op::Jmp(num) => new_prog[i] = Op::Nop(*num),
            _ => continue
        }

        let result = run_program(&new_prog);

        match result {
            Ok(acc) => println!("Patched op at {}. Last acc value was {}", i, acc),
            Err(_acc) => continue
        };
    }

}

fn run_program(program: &Vec<Op>) -> Result<i32, i32> {

    let mut ptr: i32 = 0;
    let mut acc: i32 = 0;
    let mut accessed_locs: HashSet<i32> = HashSet::new();

    loop {
        if ptr == program.len() as i32 {
            break;
        }
        accessed_locs.insert(ptr);
        match program[ptr as usize] {
            Op::Nop(_) => ptr += 1,
            Op::Acc(num) => {
                acc += num;
                ptr += 1;
            },
            Op::Jmp(num) => {
                let nextptr = ptr + num;

                if accessed_locs.contains(&nextptr) {
                    // We've hit a loop, captain
                    return Err(acc);
                } else {
                    ptr = nextptr;
                }
            }
        }
    }
    return Ok(acc)
}

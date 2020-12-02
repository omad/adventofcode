

fn main() {

    let content = std::fs::read_to_string("day2.input").expect("Couldn't read file");

    let mut valid_passwds: u32 = 0;
    for line in content.lines() {
//        let foo = line.split(' ').collect();

        let v = line.split_whitespace().take(3).collect::<Vec<&str>>();
        if let [pair, char, passwd] = &v[..] {
            let bounds: Vec<u32> = pair.split('-').take(2).map(|num| num.parse().unwrap()).collect();
            let char = char.chars().nth(0).unwrap();
            let count = count_chars(char, passwd);
            if bounds[0] <= count && count <= bounds[1] {
                valid_passwds += 1;
            }
            // println!("{}:{}:{}:{}:{}", bounds[0], bounds[1], char, passwd, count);
        }

    }
    println!("{}", valid_passwds);
}


fn count_chars(lookfor: char, mystr: &str) -> u32 {
    let mut count: u32 = 0;
    for c in mystr.chars() {
        if lookfor == c {
            count += 1;
        }
    }
    count
}

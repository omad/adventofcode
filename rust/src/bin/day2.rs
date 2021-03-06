use std::str::FromStr;

fn main() {

    let content = std::fs::read_to_string("day2.input").expect("Couldn't read file");

    let mut valid_passwds = 0;

    let mut valid_passwds_pt2 = 0;
    for line in content.lines() {
//        let foo = line.split(' ').collect();

        let v = line.split_whitespace().take(3).collect::<Vec<&str>>();
        if let [pair, thechar, passwd] = &v[..] {
            let bounds: Vec<usize> = pair.split('-').take(2).map(|num| num.parse().unwrap()).collect();
            let thechar = thechar.chars().nth(0).unwrap();
            let count = count_chars(thechar, passwd);
            if bounds[0] <= count && count <= bounds[1] {
                valid_passwds += 1;
            }
            // println!("{}:{}:{}:{}:{}", bounds[0], bounds[1], char, passwd, count);

            if is_valid_pt2(bounds[0], bounds[1], thechar, passwd) {
                valid_passwds_pt2 += 1;
            }
        }

    }
    println!("{}", valid_passwds);
    println!("{}", valid_passwds_pt2);
}

fn is_valid_pt2(pos1: usize, pos2: usize, thechar: char, thestr: &str) -> bool {
    (thestr.chars().nth(pos1 - 1) == Some(thechar)) ^ (thestr.chars().nth(pos2 - 1) == Some(thechar))
}

fn count_chars(lookfor: char, mystr: &str) -> usize {
    let mut count = 0;
    for c in mystr.chars() {
        if lookfor == c {
            count += 1;
        }
    }
    count
}

#[derive(Debug)]
struct PasswordLine {
    num1: usize,
    num2: usize,
    thechar: char,
    password: String
}
impl FromStr for PasswordLine {
    type Err = LineParseError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let v = s.split_whitespace().take(3).collect::<Vec<&str>>();
        let pair = v[0];
        let thechar = v[1];
        let passwd = v[2];
        let bounds: Vec<usize> = pair.split('-').take(2).map(|num| num.parse().unwrap()).collect();
        let thechar = thechar.chars().nth(0).unwrap();

        Ok(PasswordLine {num1: bounds[0], num2: bounds[1], thechar, password: passwd.to_string()})

    }
}

#[derive(Debug)]
enum LineParseError {
    InvalidLine { details: String },
}
impl std::string::ToString for LineParseError {
    fn to_string(&self) -> String {
        match self {
            LineParseError::InvalidLine { details } => details.to_string(),
        }
    }
}

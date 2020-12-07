use std::collections::HashSet;

fn main() {

    let content = std::fs::read_to_string("day4.input").expect("Couldn't read file");

    // let required: HashSet<&'static str> =
        // ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"].iter().cloned().collect();
    let required: HashSet<String> =
        ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].iter().map(|&s| String::from(s)).collect();
    // let valid_eyes: HashSet<&'static str> =
    //     ["amb","blu","brn","gry","grn","hzl","oth"].iter().cloned().collect();
    let valid_eyes = ["amb","blu","brn","gry","grn","hzl","oth"];

    let mut valid_passports = 0;
    let mut valid_passports_pt2 = 0;
    let mut total_lines = 0;
    let mut total_passports = 0;

    let mut curr_passport: HashSet<String> = HashSet::new();
    let mut curr_passport_p2: HashSet<String> = HashSet::new();
    // let mut curr_passport = HashSet::new();
    for line in content.lines() {
//        let foo = line.split(' ').collect();

        total_lines += 1;
        let fields = line.split_whitespace().collect::<Vec<&str>>();

        if fields.len() == 0 {
            // Check the passport validity
            if required.is_subset(&curr_passport) {
                valid_passports += 1;
            }
            if required.is_subset(&curr_passport_p2) {
                valid_passports_pt2 += 1;
            }

            total_passports +=1;
            // Start again
            curr_passport = HashSet::new();
            curr_passport_p2 = HashSet::new();
            continue;
        } else {
            // Keep collecting fields
            for field in fields {
                let colon_index = field.find(':').unwrap();
                let (field_name, field_val) = (&field[..colon_index], &field[colon_index + 1..]);
                // let field_name = field.chars().take(3).collect::<String>();

                // let field_val = field.chars().skip(4).collect::<String>();
                let valid = match field_name {
                    "byr" => {
                        let year: i32 = field_val.parse().unwrap();
                        1920 <= year && year <= 2002
                    },
                    "iyr" => {
                        let year: i32 = field_val.parse().unwrap();
                        2010 <= year && year <= 2020
                    },
                    "eyr" => {
                        let year: i32 = field_val.parse().unwrap();
                        2020 <= year && year <= 2030
                    },
                    "hgt" => {
                        let units = &field_val[field_val.len()-2..];
                        let height: i32 = field_val[..field_val.len()-2].parse().unwrap_or_default();
                        println!("Field: {}, Units: {}, Height: {}", field_val, units, height);
                        match units {
                            "in" => {
                                59 <= height && height <= 76
                            },
                            "cm" => {
                                150 <= height && height <= 193
                            },
                            _ => false
                        }
                    },
                    "hcl" => {
                        field_val.len() == 7
                            && &field_val[..1] == "#"
                            && field_val[1..].chars().all(|c| "1234567890abcdef".contains(c))
                    },
                    "ecl" => {
                        valid_eyes.contains(&field_val)
                    },
                    "pid" => {
                        field_val.len() == 9 && field_val.chars().all(|c| c.is_ascii_digit())
                    },
                    "cid" => true,
                    _ => false

                };
                curr_passport.insert(field_name.to_string());
                if valid {
                    curr_passport_p2.insert(field_name.to_string());
                }
            }
        }
    }
    if required.is_subset(&curr_passport) {
        valid_passports += 1;
    }
    if required.is_subset(&curr_passport_p2) {
        valid_passports_pt2 += 1;
    }
    println!("Lines: {} Passports: {} Valid: {}", total_lines, total_passports, valid_passports);
    println!("{}", valid_passports_pt2);
}

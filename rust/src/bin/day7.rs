use std::collections::HashMap;
use std::collections::HashSet;
// struct BagType {
//     name: String,
//     must_contain: Vec<(i32, String)>

// }

fn main() {

    let content = std::fs::read_to_string("day7.input").expect("Couldn't read file");

    // let mut bag_types: Vec<BagType> = Vec::new();
    let mut bag_types = HashMap::new();

    for line in content.lines() {
        // parse
        let words: Vec<&str> = line.split(' ').collect();
        let bag_name = words[..2].join(" ");
        let rules_str = words[4..].join(" ");
        let rules: Vec<&str> = rules_str.split(", ").collect();

        let contents = bag_types.entry(bag_name).or_insert(HashSet::new());
        for rule in rules {
            let words: Vec<&str> = rule.split(' ').collect();
//            println!("{:?}", words);
//            let num: i32 = words[0].parse().unwrap();
            let num = words[0];
            if num == "no" {
                continue;
            }
            let name = words[1..3].join(" ");
            contents.insert(name);
        }


//        let mut contains:Vec<(i32, String)> = Vec::new();
//        for rule in rules {
//            let words: Vec<&str> = rule.split(' ').collect();
//            let num: i32 = words[0].parse().unwrap();
//            let name = words[1..2].join(" ");
//            contains.push((num, name));
//        }
//        bag_types.push(BagType {
//            name: bag_name,
//            must_contain: contains
//        });
    }

    println!("Found {} types of bags.", bag_types.len());

    println!("{:?}", bag_types);
//    let mut can_contain_shiny_gold: Vec<String> = Vec::new();
    let mut count = 0;
    for bag_type in bag_types.keys() {
        if can_contain(&bag_type, &bag_types) {
            count += 1;
        }
    }

    println!("{} of them can somehow contain shiny gold.", count);
}

fn can_contain(name: &str, bag_types: &HashMap<String, HashSet<String>>) -> bool {
//    println!("{:?}", name);
    let valid_contents = bag_types.get(name).unwrap();
    if valid_contents.contains("shiny gold") {
        return true;
    } else {
        let mut found: bool = false;
        for bag_type in valid_contents {
            if can_contain(bag_type, bag_types) {
                found = true;
            }
        }
        return found;
    }

}

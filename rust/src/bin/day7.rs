use std::collections::HashMap;
use std::collections::HashSet;
// struct BagType {
//     name: String,
//     must_contain: Vec<(usize, String)>

// }

fn main() {

    let content = std::fs::read_to_string("day7.input").expect("Couldn't read file");

    let mut bag_types: HashMap<String, HashMap<String, usize>> = HashMap::new();

    for line in content.lines() {
        let words: Vec<&str> = line.split(' ').collect();
        let bag_name = words[..2].join(" ");
        let rules_str = words[4..].join(" ");
        let rules: Vec<&str> = rules_str.split(", ").collect();

        let contents = bag_types.entry(bag_name).or_insert(HashMap::new());
        for rule in rules {
            let words: Vec<&str> = rule.split(' ').collect();
            let num = words[0];
            if num == "no" {
                continue;
            }
            let num: usize = num.parse().unwrap();
            let name = words[1..3].join(" ");
            contents.insert(name, num);
        }
    }

    println!("Found {} types of bags.", bag_types.len());

    println!("{:?}", bag_types);
    let mut count = 0;
    for bag_type in bag_types.keys() {
        if can_contain(&bag_type, &bag_types) {
            count += 1;
        }
    }

    println!("{} of them can somehow contain shiny gold.", count);


    // Now for part 2
    let all_the_bags = count_contents("shiny gold", &bag_types);
    println!("{} oh god so many bags.", all_the_bags);

}

fn can_contain(name: &str, bag_types: &HashMap<String, HashMap<String, usize>>) -> bool {
    let valid_contents = bag_types.get(name).unwrap();
    if valid_contents.contains_key("shiny gold") {
        return true;
    } else {
        let mut found: bool = false;
        for bag_type in valid_contents.keys() {
            if can_contain(bag_type, bag_types) {
                found = true;
            }
        }
        return found;
    }

}

fn count_contents(name: &str, bag_types: &HashMap<String, HashMap<String, usize>>) -> usize {
//    print!("Counting {}", name);
    let this_bag = bag_types.get(name).unwrap();
    let mut count: usize = this_bag.values().sum::<usize>();
//    println!(" so far {}.", count);
    for (bag, num) in this_bag.iter() {
        count += num * count_contents(bag, bag_types);
    }
    count
}

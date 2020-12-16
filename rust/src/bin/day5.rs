use std::collections::HashSet;

fn main() {

    let content = std::fs::read_to_string("day5.input").expect("Couldn't read file");
    println!("Hello, world!");
    let line = "FBFBBFFRLR";
    let bin = &line[0..7];
    let bin = bin.replace("B", "1");
    let bin = bin.replace("F", "0");
    let num = u8::from_str_radix(&bin, 2).unwrap();
    println!("{}", num);
    let mut occupied_seats = HashSet::new();
    let mut max_seat: i64 = 0;
    for line in content.lines() {
        let row = &line[0..7].replace("B", "1")
              .replace("F", "0");
        let rown = i64::from_str_radix(&row, 2).unwrap();
        
        let col = &line[7..10].replace("R", "1")
              .replace("L", "0");
        let coln = i64::from_str_radix(&col, 2).unwrap();
        
        let seat: i64 = rown * 8 + coln;
        occupied_seats.insert(seat);
        if seat > max_seat {
            max_seat = seat;
        }
        println!("{}: row {}, column {}, seat ID {}.", line, rown, coln, seat);
    }
    println!("{}", max_seat);

    for i in 0..max_seat {
        if !occupied_seats.contains(&i)
            && occupied_seats.contains(&(i-1))
            && occupied_seats.contains(&(i+1)) {
            println!("I think your seat is: {}", i);
        }
    }
}


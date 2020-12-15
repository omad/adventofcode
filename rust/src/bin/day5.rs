fn main() {

    let content = std::fs::read_to_string("day5.input").expect("Couldn't read file");
    println!("Hello, world!");
    let line = "FBFBBFFRLR";
    let bin = &line[0..7];
    let bin = bin.replace("B", "1");
    let bin = bin.replace("F", "0");
    let num = u8::from_str_radix(&bin, 2).unwrap();
    println!("{}", num);
    let mut max_seat: u64 = 0;
    for line in content.lines() {
        let row = &line[0..7].replace("B", "1")
              .replace("F", "0");
        let rown = u64::from_str_radix(&row, 2).unwrap();
        
        let col = &line[7..10].replace("R", "1")
              .replace("L", "0");
        let coln = u64::from_str_radix(&col, 2).unwrap();
        
        let seat: u64 = rown * 8 + coln;
        if seat > max_seat {
            max_seat = seat;
        }
        println!("{}: row {}, column {}, seat ID {}.", line, rown, coln, seat);
    }
    println!("{}", max_seat);
}


use std::cell::RefCell;
fn main() {
    for _ in 0..i().trim().parse().unwrap() {
        let mut buffer: (Vec<RefCell<String>>, &RefCell<String>) =
            (Vec::new(), &RefCell::new(String::new()));
        let mut p = buffer.1;
        for c in i().trim().chars() {
            match c {
                '[' => {
                    buffer.0.push(RefCell::new(String::new()));
                    p = buffer.0.last_mut().unwrap()
                }
                ']' => p = &buffer.1,
                '<' => {
                    p.borrow_mut().pop();
                }
                _ => p.borrow_mut().push(c),
            }
        }
        buffer.0.reverse();
        println!(
            "{}",
            buffer
                .0
                .iter()
                .fold(String::new(), |acc, x| acc + &x.borrow())
                + &buffer.1.borrow()
        );
    }
}

fn i() -> String {
    let b = &mut "".into();
    std::io::stdin().read_line(b).unwrap();
    return b.to_string();
}

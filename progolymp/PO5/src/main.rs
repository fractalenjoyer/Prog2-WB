
fn main() {
    let text = input().trim().to_string();
    let mut count = 0;
    for i in 0..(2 as usize).pow(text.len() as u32) {
        if find(mask(&text, i)) {
            count += 1;
        }
    }
    println!("{}", count - 1);    
}

fn mask(string: &String, mask: usize) -> String{
    let mut output = String::new();
    for (i, c) in string.chars().enumerate() {
        if mask >> i & 1 == 1 {
            output.push(c);
        }
        if mask >> i == 0 {
            break
        }
    }
    output
}

fn input() -> String {
    let b = &mut "".into();
    std::io::stdin().read_line(b).unwrap();
    return b.to_string();
}

fn find(string: String) -> bool {
    // test if string contains a vowel followed by two consonants
    let mut vowel = false;
    let mut consonant = 0;
    for c in string.chars() {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y' || c == ' ' {
            vowel = true;
            consonant = 0;
        } else {
            consonant += 1;
        }
        if vowel && consonant == 2 {
            return false;
        }
    }
    true
}
use std::fmt;
fn main() {
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");

    println!("{subject} {verb} {object}",
        object="the lazy dog",
        subject="the quick brown fox",
        verb="jumps over");

    println!("{:=<20}{:<}", "Base 10", 79213);
    println!("{:=<20}{:<#b}", "Base 2", 79213);
    println!("{:=<20}{:<#o}", "Base 8", 79213);
    println!("{:=<20}{:<#x}", "Base 16", 79213);

    let number: f32 = 3.1415926;
    let width: usize = 10;
    println!("\nNumber = {number:>width$.4}");
    // println!("Default {}", (3,4)); error - not implemented
    println!("Debug {:?}", (3,4));
    println!("Debug pretty {:#?}", (3,4));

    #[derive(Debug)]
    struct MyStruct {
        a: i32,
        b: f32,
        s: std::string::String,
    }

    impl fmt::Display for MyStruct {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(f, "({}: {}, {})", self.s, self.a, self.b);
        }
    }

    println!("Debug {:?}", MyStruct { a: 3, b: 4.0, s: "base".to_string()});
    println!("Debug pretty {:#?}", MyStruct { a: 3, b: 4.0, s: "base".to_string()});
    println!("Default {}", MyStruct { a: 9, b: 4.0*4.0, s: "square".to_string()});
}
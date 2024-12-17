fn reverse(pair: (i32, bool)) -> (bool, i32) {
    let (i, b) = pair;
    (b, i)
}

#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

impl std::fmt::Display for Matrix {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "({}, {})\n({}, {})", self.0, self.1, self.2, self.3)
    }
}

impl Matrix {
    fn transpose(&self) -> Matrix {
        return Matrix(self.0, self.2, self.1, self.3);
    }
}

fn main() {
    let pair = (1, true);
    println!("pair is {:?}", pair);
    println!("reversed pair is {:?}", reverse(pair));

    println!("One element tuple {:?}", (5u32,));
    println!("Just an integer {:?}", (5u32));

    println!("Just an integer {:?}", (5u32));

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("matrix = {:?}", matrix);
    println!("matrix =\n{}", matrix);
    println!("transpose =\n{}", matrix.transpose());

    let tuple = (1.1, 1.2, 2.1, 2.2);
    println!("tuple = {:?}", tuple);
}
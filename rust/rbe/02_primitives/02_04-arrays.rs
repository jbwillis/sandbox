fn analyze_slice(slice: &[i32]) {
    println!("First element of the slice: {}", slice[0]);
    println!("The slice has {} elements", slice.len());
}

fn main() {
    let xs: [i32; 5] = [1, 2, 3, 4, 5];
    let ys: [i32; 500] = [9; 500];

    println!("first element of {}: {}", stringify!(xs), xs[0]);
    println!("second element of {}: {}", stringify!(xs), xs[1]);
    println!("first element of {}: {}", stringify!(ys), ys[0]);
    println!("second element of {}: {}", stringify!(ys), ys[1]);

    analyze_slice(&xs);

    analyze_slice(&ys[5..20]);

    for i in 0..xs.len() + 1 {
        match xs.get(i) {
            Some(xval) => println!("{}: {}", i, xval),
            None => println!("{} is too far", i),
        }
    }
}
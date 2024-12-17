#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

#[derive(Debug)]
struct Unit;

#[derive(Debug)]
struct Pair(i32, f32);

#[derive(Debug)]
#[derive(Clone)]
struct Point {
    x: f32,
    y: f32,
}

#[derive(Debug)]
struct Rectangle {
   top_left: Point,
    bottom_right: Point,
}

impl Rectangle {
    fn area(&self) -> f32 {
        let Rectangle {
            top_left: Point{x: tl_x, y: tl_y},
            bottom_right: Point{x: br_x, y: br_y},
        } = self;

        let dx = (br_x - tl_x).abs();
        let dy = (br_y - tl_y).abs();
        return dx * dy;
    }
}

fn square(top_left: &Point, side_length: f32) -> Rectangle {
    return Rectangle {
        top_left: top_left.clone(),
        bottom_right: Point {x: top_left.x + side_length, y: top_left.y + side_length},
    };
}

fn main() {
    let name = String::from("Peter");
    let age = 31;
    let peter = Person { name, age };

    println!("{:?}", peter);

    let point: Point = Point { x: 5.2, y: 0.4};
    let another_point = Point { x: 5f32, y: 1.4 };

    let bottom_right  = Point { x: 10.9, ..another_point};

    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    let Point{ x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        top_left: Point {x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };
    println!("_rectangle = {:?}", _rectangle);
    println!("_rectangle.area() = {}", _rectangle.area());

    let _unit = Unit;

    println!("_unit = {:?}", _unit);

    let pair = Pair(1, 0.1);

    println!("pair == {:?}", pair);

    let Pair(integer, decimal) = pair;
    println!("pair == ({}, {})", integer, decimal);

    let sq = square(&Point { x: 0.0, y: 0.0 }, 5.0);
    println!("sq == {:?}", sq);
    println!("sq.area() is {}", sq.area());
}
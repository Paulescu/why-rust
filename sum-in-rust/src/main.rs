use clap::Parser;

use std::time::Instant;


/// Simple program to greet a person
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Number to count up to
    #[arg(short, long)]
    number: i64,
}

fn sum_up_to(number: i64) -> u128{
    let mut sum = 0;

    for i in 0..number {
        sum += (i + 1) as u128;
    }

    sum
}

fn main() {

    let args = Args::parse();

    // time the loop
    // get the current time in unix seconds
    // let start = Instant::now();
    
    let result = sum_up_to(args.number);

    // let duration = start.elapsed();
    println!("sum up to {} is {}", args.number, result);
}

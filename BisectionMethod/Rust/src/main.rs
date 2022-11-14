use kdam::{tqdm, BarExt};
use std::time::Instant;

#[derive(Debug)]
enum NUM {
    Positive,
    Negative,
    Zero,
}

impl NUM {
    fn ntype(num: f64) -> NUM {
        if num == 0. {
            return NUM::Zero;
        } else if num > 0. {
            // value is positive
            return NUM::Positive;
        } else {
            // Value is negative
            return NUM::Negative;
        }
    }
}

fn polynomial(x: f32) -> f64 {
    ((x * x * x) - x - 1.) as f64
}

// (BN) Bisection Number (nuber of simulaton)
// (RI) init Root in Interval
const BN: i128 = i128::pow(10, 6);
const RI: [f32; 2] = [1., 2.];

fn main() {
    let mut pb = tqdm!(total = BN as usize);
    pb.set_description(format!("{}", "num"));

    let mut rinterval: Vec<f32> = RI.to_vec();

    let now = Instant::now();

    for bn in 0..BN {
        let mid_point = (rinterval[0] + rinterval[1]) / 2.; //(rinterval.iter().sum::<f32>() as f32) / 2.;

        // println!("rinterval: {:?}", rinterval);

        if mid_point == 0. {
            println!(
                "Find the root att {}, (Bisection Number {})",
                rinterval[0], bn
            );
            break;
        }
        get_root_interval(&mut rinterval, mid_point);
        pb.update(1);
    }

    println!(
        "The root is between [{}, {}], (Bisection Number {})",
        rinterval[0], rinterval[1], BN
    );

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}

// Root in Interval
fn get_root_interval(rinterval: &mut Vec<f32>, x: f32) {
    use NUM::*;
    let y = polynomial(x);

    match NUM::ntype(y) {
        Positive => rinterval[1] = x,
        Negative => rinterval[0] = x,
        Zero => {
            rinterval[0] = x;
            rinterval[1] = x;
        }
    }
}

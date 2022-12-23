# pip install tqdm
# python -m pip install tqdm
from enum import Enum
from tqdm import tqdm
import time;

class NUM(Enum):
    Positive = "1",
    Negative = "-1",
    Zero = "0",

    @staticmethod
    def ntype(num):
        if num == 0:
            return NUM.Zero
        elif num > 0:
            # Value is positive
            return NUM.Positive
        else:
            # Value is negative
            return NUM.Negative


       
def polynomial(x):
    return ((x * x * x) - x - 1)

# (BN) Bisection Number (nuber of simulaton)
# (RI) init Root in Interval
BN = 10**6
rinterval = [1, 2]

def main():
    global rinterval

    now = time.perf_counter()

    for bn in tqdm(range(BN)):
        mid_point = (rinterval[0] + rinterval[1]) / 2

        if mid_point == 0:
            print(
                "Find the root att {}, (Bisection Number {})".format(
                rinterval[0], bn)
            )
            break
                
        get_root_interval(mid_point)
    
    print(
        "The root is between [{}, {}], (Bisection Number {})".format(
        rinterval[0], rinterval[1], BN)
    )

    
    elapsed = time.perf_counter() - now
    print("Time elapsed: ", elapsed, " seconds")


def get_root_interval(x):
    y = polynomial(x)

    # match NUM.ntype(y):
    #     case NUM.Positive:
    #         rinterval[1] = x
    #     case NUM.Negative:
    #         rinterval[0] = x
    #     case NUM.Zero:
    #         rinterval[0] = x
    #         rinterval[1] = x
        
    if NUM.ntype(y) == NUM.Positive:
        rinterval[1] = x
    elif NUM.ntype(y) == NUM.Negative:
        rinterval[0] = x
    elif NUM.ntype(y) == NUM.Zero:
        rinterval[0] = x
        rinterval[1] = x

             
    


if __name__ == "__main__":
    main()

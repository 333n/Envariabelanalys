#  Ett godtycklig gissning på x
x_gues = 2

# x^2 - x - 1 = 0 => x = 1 + (1/x)
def FixedPointIteration(xn, iteration):
    x = 1 + (1/xn)
    
    if iteration <= 0:
        return x
    else:
        return FixedPointIteration(x, iteration-1)



x = FixedPointIteration(x_gues, 10)
print(x)
import numpy as np
import matplotlib.pyplot as plt



"""
1	Topic Introduction
--------------------------
Given simultaneous nonlinear equations, find the roots using Newton-Rhapson.

2	Topic Theory/Approach
--------------------------
Algebrically manipulate the given functions to find a function of:
    x, y, u, v, dudx, dudy, dvdx, dvdy
    

Then use the lambda functions to perform the Newton-Rhapson and find the 
roots.

3	Problems
--------------------------
    (a)	Problem Statement
Determine the roots of the following simultaneous nonlinear equations:
(x 􀀀 4)2 + (y 􀀀 4)2 = 5
x2 + y2 = 16
Use a graphical approach to obtain your initial guesses. Determine rened estimates with the
two-equation Newton-Rhapson method

    (b)	Problem Approach
    
Algebrically manipulate the given functions to find a function of:
    x, y, u, v, dudx, dudy, dvdx, dvdy

Then use the lambda functions to perform the Newton-Rhapson and find the 
roots.

    (c)	Problem Results
Newton Estimate:	nan, nan

    (d)	Problem Discussion of Results
The Newton estimate resulted in nan because the two functions diverge and never cross each
other, thus no solution at any roots.
    
"""

def newtons_method(x, y):
    denom = ((dudx(x, y) * dvdy(x, y)) - (dudy(x, y) * dvdx(x, y)))
    for i in range(0, 10):
        denominator = denom + (denom == 0)
        x_1 = x - (((u(x, y) * dvdy(x, y)) - (v(x, y) * dudy(x, y))) / denominator)
        y_1 = y - (((v(x, y) * dudx(x, y)) - (u(x, y) * dvdx(x, y))) / denominator)

        x = x_1
        y = y_1

    print('Newton Estimate:\t' + str(round(x, 5)) + ', ' + str(round(y, 5)))
    plt.plot(x, y, marker='o', label='root')



if __name__ == "__main__":
    x_lower, x_upper = -10, 20
    num = 100
    stop_crit = .1

    x_plot = -1
    y_plot = np.linspace(-1, 5, 21)

    fx = lambda x, y: - np.sqrt(- y ** 2 + 8 * y - 11) + 4
    fy = lambda x, y: 4 - x

    plt.plot(fx(y_plot, y_plot))
    plt.plot(fy(y_plot, y_plot))

    u = lambda x, y: - x + np.sqrt(y ** 2 - 8 * y + 11) - 4
    v = lambda x, y: - y + x - 4

    dudx = lambda x, y: 2 * (x - 4)
    dudy = lambda x, y: 2 * (y - 4)

    dvdx = lambda x, y: 2 * x
    dvdy = lambda x, y: 2 * y


    newtons_method(1.2, 1.2)
    plt.grid(True)
    plt.xlim([x_lower, x_upper])
    plt.ylim([-10, 10])
    plt.show()

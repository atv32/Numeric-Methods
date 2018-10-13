import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray
from typing import Optional, Union, Tuple


"""
1	Topic Introduction
--------------------------
Given simultaneous nonlinear equations, find the roots using fixed point, Newton-Rhapson
given the initial guesses of x=y=1.2

2	Topic Theory/Approach
--------------------------
Algebrically manipulate the given functions to find a function of:
    x, y, u, v, dudx, dudy, dvdx, dvdy

Then use the lambda functions to perform the Newton-Rhapson and find the 
roots.

3	Problems
--------------------------
    (a)	Problem Statement
Determine the roots of the following simultaneous nonlinear equations using (a) xed point iteration,
and (b) the Newton-Rhapson method:
y = 􀀀x2 + x + 0:75
y + 5xy = x2
Employ inital guesses of x = y = 1:2 and discuss the results.

    (b)	Problem Approach
    
Algebrically manipulate the given functions to find a function of:
    x, y, u, v, dudx, dudy, dvdx, dvdy

Then use the lambda functions to perform the Newton-Rhapson and find the 
roots.

    (c)	Problem Results
    
Newton Estimate:    	2.12825, 0.16488
Fixed Point Estimate:	0.8899999999999999, 0.23999999999999977

    (d)	Problem Discussion of Results
The fixed-point method came relatively close to the solution given the parameters.
Newton-Raphson was not as accurate, but was in the same area.
    
"""


def fixed_point():
    fp_x = 1.2
    fp_y = .2

    for i in range(1, 3):
        ny = fy(fp_x, fp_y)
        nx = fx(fp_x, fp_y)

        y_n = ny
        x_n = nx
    print('Fixed Point Estimate:\t' + str(x_n) + ', ' + str(y_n))
    plt.plot(x_n, y_n, marker='*')


def newtons_method(x, y):
    denom = ((dudx(x, y) * dvdy(x, y)) - (dudy(x, y) * dvdx(x, y)))
    for i in range(0, 2):
        denominator = denom + (denom == 0)
        x_1 = x - (((u(x, y) * dvdy(x, y)) - (v(x, y) * dudy(x, y))) / denominator)
        y_1 = y - (((v(x, y) * dudx(x, y)) - (u(x, y) * dvdx(x, y))) / denominator)

        x = x_1
        y = y_1


    print('Newton Estimate:\t' + str(round(x, 5)) + ', ' + str(round(y, 5)))
    plt.plot(x, y, marker='o', label='root')

if __name__ == "__main__":
    x_lower, x_upper = -1, 7
    num = 100

    x_plot = -1
    y_plot = np.linspace(-1, 7, 21)

    fx = lambda x, y: y + (x ** 2) - 0.75
    fy = lambda x, y: (-5 * x * y) + (x ** 2)

    plt.plot(fx(x_plot, y_plot))
    plt.plot(fy(x_plot, y_plot))

    u = lambda x, y: - x ** 2 + x + 0.75 - y
    v = lambda x, y: y + 5 * x * y - x ** 2

    dudx = lambda x, y: -2 * x + 1
    dudy = lambda x, y: -1

    dvdx = lambda x, y: 5 * y - 2 * x
    dvdy = lambda x, y: 1 + 5 * x

    t: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(1, 7, num)

    x = 4
    y = 0

    zeros_array = np.linspace(0, 0, num=num)

    newtons_method(x, y)
    fixed_point()
    plt.grid(True)
    plt.xlim([x_lower, x_upper])
    plt.show()

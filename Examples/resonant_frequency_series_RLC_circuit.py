
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray
from typing import Optional, Union, Tuple


"""
1	Topic Introduction
--------------------------
Determine the value of R that causes the resonant frequency to be 1 kHz.

2	Topic Theory/Approach
--------------------------
Plot the resonant frequency of a series RLC circuit and graphically determine
where the roots reside and apply the root finding methods.

3	Problems
--------------------------
    (a)	Problem Statement
The resonant frequency of a series RLC circuit is

w = sqrt(1/LC - (R/2L)^2)

With L = 5 H and C = 10􀀀4 F, determine the value of R that causes the resonant frequency to
be 1 kHz. Use the Newton-Rhapson, bisection, and false position methods.

    (b)	Problem Approach
Use algebra to create a more usable function and find the derivative.
Apply root finding techniques.


    (c)	Problem Results
    
False Position Root Estimate:	nan, nan
Bisection Root Estimate:	100.0, nan
    
    (d)	Problem Discussion of Results

There are no answers to this problem as the reals of the function
do not cross over the x-axis, hence no solution.
    
    
"""


def newtons_method(f, df, xa):
    denom = df(xa)
    for i in range(0, 10):
        denominator = denom + (denom == 0)
        xa = xa - f(xa) / denominator

    if 0.5 < f(xa) > -0.5:
        print('Newton Estimate:\t' + str(xa) + ', ' + str(f(xa)))
        plt.plot(xa, f(xa), marker='o')
    else:
        return None


def bisection(f):
    x_lower = 1
    x_upper = 100
    x_r = x_lower
    for i in range(1, 100, 1):
        x_r_old = x_r
        x_r = ((x_upper + x_lower) / 2)

        x_r_new = x_r

        if (f(x_lower) * f(x_r) < 0):
            x_upper = x_r

        else:
            x_lower = x_r

        error_a = abs((x_r_new - x_r_old) / x_r_new)

        plt.plot(error_a, 'k*')
        plt.plot(x_r, f(x_r), 'g*')
    print('Bisection Root Estimate:\t' + str(round(x_r, 5)) + ', ' + str(round(f(x_r), 5)))


def false_position(f):
    x_lp = 1
    x_up = 1000
    x_rp_new = x_up
    x_rp_old = x_lp

    for i in range(1, 21, 1):
        x_rp = x_up - ((f(x_up) * (x_lp - x_up)) / (f(x_lp) - f(x_up)))

        x_rp_new = x_rp
        if f(x_lp) * f(x_rp) < 0:
            x_up = x_rp
        else:
            x_lp = x_rp

        error_fp = abs((x_rp_new - x_rp_old) / x_rp_new)

        plt.plot(error_fp, 'k*')
        plt.plot(x_rp, f(x_rp), 'r*')

    print('False Position Root Estimate:\t' + str(round(x_rp, 5)) + ', ' + str(round(f(x_rp), 5)))


if __name__ == "__main__":
    x_lower, x_upper = -20, 20
    y_lower, y_upper = 0, 50
    num = 100
    stop_crit = .1

    imped =  lambda R: np.sqrt(1999 - ((25 * (R ** 2)) / 4))
    dimped = lambda R: -(25 * R) / (2 * np.sqrt(7996 - 25 * (R ** 2)))

    L = 5
    C = 10 ** (-4)
    w = 1

    x_array: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(x_lower, x_upper, num)

    func, = plt.plot(x_array, imped(x_array), 'r')

    func.set_antialiased(False)  # turn off antialising

    xas = np.linspace(-5, 0, 1000)

    for value in x_array:
        newtons_method(imped, dimped, value)

    false_position(imped)
    bisection(imped)

    plt.setp(func, 'linewidth', 1.0)

    plt.grid(True)
    plt.xlim([x_lower, x_upper])
    plt.ylim([y_lower, y_upper])
    plt.show()

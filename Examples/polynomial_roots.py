
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray
from numpy import sign
from typing import Optional, Union, Tuple

"""
1	Topic Introduction
--------------------------
Determine the roots of f(x) = -12-21x-18x&2-2.75x^3 through various root finding techniques.

2	Topic Theory/Approach
--------------------------
Utilize incremental function to search the roots as a sense of where the roots are.
Use bisection and false position functions to estimate the roots.

3	Problems
--------------------------
    (a)	Problem Statement
    
Determine the roots of f(x) = 􀀀12 􀀀 21x 􀀀 18x2 􀀀 2:75x3 between xl = 􀀀10 and xu = 10, and a
stopping criterion of 0.1%. You should use your icremental function rst to nd all roots, and use
those ranges to get better results using the bisection and false position functions.

    (b)	Problem Approach
Utilize bisection and false position techinques with the lower x of -10 and upper x of 10 with a stopping
criterion of .001. The first 

    (c)	Problem Results

Incremental:	                -5.25000000000019, -5.24900000000019
Bisection Root Estimate:	    -5.24901, -0.0
False Position Root Estimate:	-5.25927, 0.61139
    
    (d)	Problem Discussion of Results
The incremental function returns the range in where the roots reside.

The Bisection Root result returns the estimated root of the function 
between the range of -10 and 10 and a stopping criteria of 100 iterations.

The False Position result of a trial and error technique to determine the root
of the function and adjusts the values until a criteria is met or if the root is found.

"""


def incremental(f, xa, xb, dx):
    x1 = xa
    f1 = f(xa)

    x2 = xa + dx
    f2 = f(x2)

    while sign(f1) == sign(f2):
        if x1 >= xb:
            return None, None
        x1 = x2
        f1 = f2
        x2 = x1 + dx
        f2 = f(x2)
    else:
        print('Incremental:\t' + str(x1) + ', ' + str(x2))
        return x1, x2


def false_position(f, xa, xb):
    x_lp = xa
    x_up = xb

    for i in range(1, 21, 1):
        x_rp = x_up - ((f(x_up) * (x_lp - x_up)) / (f(x_lp) - f(x_up)))
        if f(x_lp) * f(x_rp) < 0:
            x_up = x_rp
        else:
            x_lp = x_rp
    print('False Position Root Estimate:\t' + str(round(x_rp, 5)) + ', ' + str(round(f(x_rp), 5)))
    plt.plot(x_rp, f(x_rp), 'b*')


def bisection(f, xa, xb):
    x_lower = xa
    x_upper = xb
    x_r = x_lower
    for i in range(1, 100, 1):
        x_r = ((x_upper + x_lower) / 2)
        if (f(x_lower) * f(x_r) < 0):
            x_upper = x_r
        else:
            x_lower = x_r
    print('Bisection Root Estimate:\t' + str(round(x_r, 5)) + ', ' + str(round(f(x_r), 5)))
    plt.plot(x_r, f(x_r), 'g*')


if __name__ == "__main__":
    x: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(-10, 10)
    y = lambda x: -12 - 21 * x - 18 * (x ** 2) - 2.75 * (x ** 3)


    line, = plt.plot(x, y(x), 'r')
    line.set_antialiased(False)  # turn off antialising

    plt.setp(line, 'linewidth', 1.0)

    roots1, roots2 = incremental(y, -10, 10, .001)
    bisection(y, -10, 10)
    false_position(y, -10, 10)

    plt.legend((line, ), ('f(x) = -12 - 21x - 18x^2 - 2.75x^3',))
    plt.grid(True)
    plt.show()

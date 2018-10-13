import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray
from typing import Optional, Union, Tuple

"""
1	Topic Introduction
--------------------------
Find the depth of the water tank to be filled so it holds 30 m^3

2	Topic Theory/Approach
--------------------------
Manipulate the given function based off of the given variables and solve for the roots
when V = 30 using false position and midpoint root functions with the lower limit of 0
and upper limit as R.

3	Problems
--------------------------
    (a)	Problem Statement
You are designing a spherical tank to hold water for a small village in a developing country. The
volume of liquid it can hold can be computed as
V =          3R - h
    pi*h^2*___________
                3
Where V =volume (m3), h=depth of water in tank(m), and R=the tank radius(m). If R=3 m, to
what depth must the tank be lled so that it holds 30 m3? Calculate the answer using both the
false position and midpoint approaches. Employ a lower limit of xl = 0 and xu = R.

    (b)	Problem Approach
Enter the given variables in the function, rearrange the function to set equal to 0 and V = 30.
Graph the function to visually see how many roots there are.
Determine the solution through false position and midpoint approaches. 

    (c)	Problem Results
False Position Root Estimate:	-1.64081, -0.0
False Position Root Estimate:	2.02691, 0.0
False Position Root Estimate:	8.61391, 0.0

Midpoint Root Estimate:	-1.64081, 0.0
Midpoint Root Estimate:	2.02691, 0.0
Midpoint Root Estimate:	8.61391, -0.0

    (d)	Problem Discussion of Results
I set the ranges to check:
    [-2.5, 0]
    [0, 3]
    [7.5, 10]

These results returned the roots between the lower and upper limits.
These roots demonstrate where the depth can maintain 30 m^2

"""


def false_position(f, xa, xb):
    x_lp = xa
    x_up = xb

    for i in range(1, 21, 1):
        x_rp = x_up - ((f(x_up) * (x_lp - x_up)) / (f(x_lp) - f(x_up)))
        if f(x_lp) * f(x_rp) < 0:
            x_up = x_rp
        else:
            x_lp = x_rp
    plt.plot(x_rp, f(x_rp), 'y*')
    print('False Position Root Estimate:\t' + str(round(x_rp, 5)) + ', ' + str(round(f(x_rp), 5)))


def midpoint(f, xa, xb):
    x_lower = xa
    x_upper = xb
    x_r = x_lower
    for i in range(1, 100, 1):
        x_r = ((x_upper + x_lower) / 2)
        if (f(x_lower) * f(x_r) < 0):
            x_upper = x_r
        else:
            x_lower = x_r
    plt.plot(x_r, f(x_r), 'b*')
    print('Midpoint Root Estimate:\t' + str(round(x_r, 5)) + ', ' + str(round(f(x_r), 5)))


if __name__ == "__main__":
    h: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(-10, 10)

    V = lambda R, h: np.pi * h ** 2 * ((3 * R - h) / 3.0)
    V_new = lambda h: 9 * np.pi * h ** 2 - np.pi * h ** 3 - 90

    line, = plt.plot(h, V_new(h), 'r')

    false_position(V_new, -2.5, 0)
    false_position(V_new, 0, 3)
    false_position(V_new, 7.5, 10)

    midpoint(V_new, -2.5, 0)
    midpoint(V_new, 0, 3)
    midpoint(V_new, 7.5, 10)


    line.set_antialiased(False)  # turn off antialising

    plt.setp(line, 'linewidth', 2.0)
    plt.legend((line, ), ('V = pi * h ^ 2 * (3R-h/3)',))
    plt.grid(True)
    plt.show()

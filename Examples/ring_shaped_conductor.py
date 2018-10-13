
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray
from typing import Optional, Union, Tuple

"""
1	Topic Introduction
--------------------------
Find the distance x where the force is 1N for a ring.

2	Topic Theory/Approach
--------------------------
Use Newton-Rhapson, fixed point and secant to find the solution.

3	Problems
--------------------------
    (a)	Problem Statement
A total charge Q is uniformly distributed around a ring-shaped conductor with radius a. A charge
q is located at a distance x from the center of the ring. The force exerted on the charge by the ring
is given by:

F  = (1/(4*pi*(8.85*10^-12)))*(((2 * 10 ^ -5)*(2 * 10 ^ -5)*x)/((x^2 + (0.9)^2)^(3/2)))
F' = (2.91334 - 7.19344 x ^ 2) / (x ^ 2 + 0.81) ^ ( 5/2 ) 


where e0 = 8:85  10􀀀12 C2=(N m2). Find the distance x where the force is 1N if q and Q are
2  10􀀀5 C for a ring with a radius of 0.9 m. Use the Newton-Rhapson, xed point, and modied
secant approaches to nd the solution.


    (b)	Problem Approach
Plot F and find the appropriate range to use the root finding methods.

    (c)	Problem Results
Newton Estimate:	    (0.0, 0.0)
Secant Estimate:	    (1.7763568394002505e-15, 8.764144728422837e-15)
Fixed Point Estimate:	(0.0, 0.0)


    (d)	Problem Discussion of Results
The root estimators eventually found the root of the given function at (0,0) or close to it.
    
"""

def newtons_method(f, df, xa):
    denom = df(xa)
    for i in range(0, 10):
        denominator = denom + (denom == 0)
        xa = xa - f(xa) / denominator

    if f(xa) > -0.5 and f(xa) < 0.5:
        print('Newton Estimate:\t' + str(xa) + ', ' + str(f(xa)))
        plt.plot(xa, f(xa), marker='o')


def fixed_point(f, xa, xb):
    for i in np.arange(xa, xb, .01):
        xa = f(xa)
    print('fixed point:\t' + str(xa) + ', ' + str(f(xa)))
    plt.plot(xa, f(xa), marker='o')


def secant(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            denominator = float(f_x1 - f_x0)/(x1 - x0)
            denominator = denominator + (denominator == 0)
            x = x1 - float(f_x1)/denominator
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1
    # Here, either a solution is found, or too many iterations
    if abs(f_x1) > eps:
        iteration_counter = -1
    plt.plot(x, f(x), marker='*')
    print('Secant Estimate:\t' + str(x) + ', ' + str(f(x)))
    return x, iteration_counter


if __name__ == "__main__":
    x_lower = 0
    x_upper = 15

    F  = lambda x: (1 / (4 * np.pi * e_o)) * (((2 * 10 ** -5) * (2 * 10 ** -5) * x)/((x ** 2) + (a ** 2) ** (3/2)))
    dF = lambda x: ((2.91334 - 7.19344 * x ** 2) / ((x ** 2 + 0.81) ** (5 / 2)))

    e_o = 8.85 * 10 ** -12
    Q = q = 2 * 10 ** -5
    a = 0.9
    f = 1


    x: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(x_lower, x_upper)
    newton_xrange: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(0, 1)
    zeros_array = np.linspace(0, 0, num=50)

    secant_root = secant(F, x_lower, x_upper, .001)

    for value in newton_xrange:
        newtons_method(F, dF, value)


    fixed_point(F, 0, 15)

    func, = plt.plot(x, F(x), 'r')
    func.set_antialiased(False)  # turn off antialising
    plt.setp(func, 'linewidth', 2.0)

    plt.grid(True)
    plt.xlim([x_lower, x_upper])
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

"""
1	Topic Introduction
--------------------------
Use root finding techniques to determine the lowest value that t such that i = 3 A
of an oscillating current in an electric circuit.

2	Topic Theory/Approach
--------------------------
Plot the i(t) function when i = 3 A and use Newton-Rhapson, modified secant, and fixed position.


3	Problems
--------------------------
    (a)	Problem Statement
An oscillating current in an electric circuit is described by i'(t) = 9*e^-t * (2 *pi *cos(2 * pi * t) - sin( 2 * pi *t)), where t is in
seconds. Determine the lowest value of t such that i = 3 A. Use and compare the results using the
Newton-Rhapson, modied secant, and xed-point approaches.

    (b)	Problem Approach
Use the graphical approach to determine where the roots could be. Find the range and apply
appropriate ranges for each of the root finding techniques.

    (c)	Problem Results
Fixed Point root:	  -3.0, -3.0
Secant Root Estimate: 305.0, -3.0
Newton Estimate:	-4.99964241266, -2.07700523447e-12
Newton Estimate:	-4.50058900489, 2.32702745961e-12
Newton Estimate:	-4.50058900489, 2.32702745961e-12
Newton Estimate:	-3.99902737359, -3.09530179265e-13
Newton Estimate:	-3.99902737359, -3.09530179265e-13
Newton Estimate:	-3.50159948751, 2.77111666946e-13
Newton Estimate:	-3.50159948751, 2.77111666946e-13
Newton Estimate:	-2.99742208901, -0.0796481521771
Newton Estimate:	-2.99735158728, 2.33590924381e-13
Newton Estimate:	-2.99735158728, 2.33590924381e-13
Newton Estimate:	-2.50436651557, 0.0208938500777
Newton Estimate:	-2.50433643776, 8.08242361927e-14
Newton Estimate:	-2.50433643776, -6.00137717299e-11
Newton Estimate:	-1.99276918259, -0.00146573311628
Newton Estimate:	-1.99276561982, -1.36823885555e-12
Newton Estimate:	-1.99276561982, 8.28626056659e-12
Newton Estimate:	-1.51171357429, 0.000879311754175
Newton Estimate:	-1.51171017566, -2.62012633812e-14
Newton Estimate:	-1.51171017564, -6.27044061119e-09
Newton Estimate:	-0.980037614755, -5.77355136855e-06
Newton Estimate:	-0.980037575344, -1.34378286276e-10
Newton Estimate:	-0.980037575343, 4.03321820386e-12
Newton Estimate:	-0.531386769464, 5.09412733645e-05
Newton Estimate:	-0.531386246136, -3.99680288865e-15
Newton Estimate:	-0.531386242491, -3.54839384542e-07
Newton Estimate:	0.0574252336972, 0.0
Newton Estimate:	0.0574252279207, -2.71236472837e-07
Newton Estimate:	0.0574252336972, -4.4408920985e-16
Newton Estimate:	0.415718051612, 2.24104238278e-07
Newton Estimate:	0.415718057978, 4.4408920985e-16
Newton Estimate:	0.415718092972, -1.2319205025e-06
    
    (d)	Problem Discussion of Results
Due to the nature of an oscillating function, it is sinusoidal function. 
The fixed point method utilizes trial and error within the range and due to multiple roots
it seems to provide the wrong answer as there are multiple roots unless a specific range is 
specified. Secant method seems to return a similar answer to the fixed point.

However, the Newton-Rhapson method returns the correct answer of:
    approximately ~(0.0583636, -9.47091e-05)
                  ~(0.41416, -0.00185946)
    
"""


def newtons_method(f, df, xa):
    denom = df(xa)
    for i in range(0, 10):
        denominator = denom + (denom == 0)
        xa = xa - f(xa) / denominator

    if f(xa) > -0.5 and f(xa) < 0.5:
        print('Newton Estimate:\t' + str(xa) + ', ' + str(f(xa)))
        plt.plot(xa, f(xa), marker='o')


def secant(f, xa, xb, epsilon):
    f_xa = f(xa)
    f_xb = f(xb)
    iteration_counter = 0
    while abs(f_xb) > epsilon and iteration_counter < 100:
        try:
            denominator = float(f_xb - f_xa)/(xb - xa)
            denominator = denominator + (denominator == 0)
            x = xb - float(f_xb)/denominator
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
        xa = xb
        xb = x
        f_xa = f_xb
        f_xb = f(xb)
        iteration_counter += 1
    # Here, either a solution is found, or too many iterations
    if abs(f_xb) > epsilon:
        iteration_counter = -1
    plt.plot(x, f(x), marker='*')
    print('Secant Root:\t' + str(x) + ', ' + str(f(x)))
    return x, iteration_counter


def fixed_point(f, xa, xb):
    for i in np.arange(xa, xb, .01):
        xa = f(xa)
    print('fixed point:\t' + str(xa) + ', ' + str(f(xa)))
    plt.plot(xa, f(xa), marker='o')

if __name__ == "__main__":
    t = np.linspace(-5, 5, 100)

    ft  = lambda t: (9 * np.exp(-t) * np.sin(2 * np.pi * t)) - 3
    dft = lambda t: 9 * np.exp(-t) * (2 * np.pi * np.cos(2 * np.pi * t) - np.sin(2 * np.pi * t))

    ft_plt, = plt.plot(t, ft(t), 'r')

    xas = np.linspace(-5, 0, 1000)
    for value in t:
        newtons_method(ft, dft, value)

    secant(ft, 0, 5, .001)
    fixed_point(ft, 0, .14)


    plt.xlim([-5, 5])
    plt.ylim([-15, 15])
    plt.grid(True)

    plt.legend((ft_plt, ), ('i(t) = 9e^-tsin(2pit)',))

    plt.show()

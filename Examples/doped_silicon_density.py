import numpy as np
import matplotlib.pyplot as plt


"""
1	Topic Introduction
--------------------------
Determine the doping density, N of the given function to get a desired p of 6 * 10^6


2	Topic Theory/Approach
--------------------------
Manipulate the given functions to determine the appropriate function to plot and
determine the N value with the given parameters.


3	Problems
--------------------------
    (a)	Problem Statement
The resistivity p of doped silicon is based on the charge q on an electron, the electron density n,
and the electron mobility u. The electron density is given in terms of the doping density N and the
intrinsic carrier density ni. The electron mobility is described by the temperature T, the reference
temperature T0, and the reference mobility 0. The equations requried to compute the resistivity
are:

Equations required to compute resistivity
    p = 1 / qnu

Where,

    n = 1/2 ( N + sqrt(N^2 + 4n^2_i) )

and,

    u = u. (T/T.)^(-2.42)

Determine N, given T0 = 300 K, T = 1000 K, 0 = 1300 cm2(V s)􀀀1, q = 1:6  10􀀀19 C,
ni = 6:21 * 109 cm^3, and a desired  = 6  106 V s cm=C. Use (a)bisection, and (b) the modifed
secant approach.

    (b)	Problem Approach
Set up the equations to apply the root finding methods to find the solutions to the problem
statement.

    (c)	Problem Results

Secant Root Estimate:	    (12149881211.787176, -2.63564288616e-07)
Bisection Root Estimate:	(12149881211.78642, -0.0)

    (d)	Problem Discussion of Results
The secant and bisection estimates aligned with the root, but the bisection root estimate
provided a better solution as the p(n) answer is closer to 0.0.
    
"""


def bisection(f, xa, xb):
    x_lower = xa
    x_upper = xb
    x_r = x_lower
    for i in range(1, 100, 1):
        x_r = ((x_upper + x_lower) / 2)
        if f(x_lower) * f(x_r) < 0:
            x_upper = x_r
        else:
            x_lower = x_r
    plt.plot(x_r, f(x_r), 'b*')
    print('Bisection Root Estimate:\t' + str(round(x_r, 5)) + ', ' + str(round(f(x_r), 5)))


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


if __name__ == "__main__":
    N = np.linspace(1 * 10 ** 9, 15 * 10 ** 9, 16)

    T_o = 300
    T = 1000
    u_o = 1300
    q = 1.6 * 10 ** -19
    n_i = 6.21 * 10 ** 9
    desired_p = 6 * 10 ** 6

    u = u_o * ((T / T_o) ** -2.42)
    n = lambda N: .5 * (N + np.sqrt(N ** 2 + 4 * n_i ** 2))
    p = lambda N: (1.0 / (q * n(N) * u)) - desired_p

    sec_xa = secant(p, 0, 1.5 * 10 ** 10, .001)
    bisection(p, 0, 1.5 * 10 ** 10)

    fun_plot = plt.plot(N, p(N), 'r')
    plt.setp(fun_plot, 'linewidth', 2.0)

    plt.grid(True)
    plt.legend((fun_plot, ), ('p = 1/qnu',))
    plt.show()

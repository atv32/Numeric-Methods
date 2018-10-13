
import numpy as np
import matplotlib.pyplot as plt


"""
1	Topic Introduction
--------------------------
Use root finding methods to solve for angular frequency of the effective impedance
of a parallel RLC circuit.

2	Topic Theory/Approach
--------------------------
Rearrange the impedence equation to make it usable for the root finding method.
Find the roots for the angular frequency within the given parameters.

3	Problems
--------------------------
    (a)	Problem Statement
The eective impedance of a parallel RLC circuit is

1/Z = sqrt(1/R^2 + (wC - 1/wL)^2)

where Z=impedance (Ohms), and != the angular frequency (rad/s). Find the ! that results in an
impedance of 75
 using both bisection and false position with initial guesses of 1 and 1000 for the
following parmeters: R = 225 
, C = 0:6  10􀀀6 F, and L = 0:5 H. Ensure the absolute relative
error is no greater than 0.1%.

    
    (b)	Problem Approach
Use algebra:

    sqrt((1.0 / 225 ^ 2) + ((w * (0.6 * 10^(-6) )) - (1.0 / (w * 0.5))) ^2) - 75
    simplifies to :
    sqrt((1/225^2) + (w * (0.6/10^6) - (1/(w*0.5)))^2) - 75
Plot the function, apply the root finding methods.
    
    (c)	Problem Results
    
Bisection Root Estimate:	39.69953, 0.0
False Position Root Estimate:	39.69953, 0.0

    (d)	Problem Discussion of Results
The bisection and false position estimators agreed in results and found the 
angular frequency of 39.69953 rad/s

"""


def bisection(f, lower, upper):
    x_lower = lower
    x_upper = upper
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

        f_rp = f(x_rp)
        error_fp = abs((x_rp_new - x_rp_old) / x_rp_new)

    plt.plot(error_fp, 'k*')
    plt.plot(x_rp, f(x_rp), 'r*')

    print('False Position Root Estimate:\t' + str(round(x_rp, 5)) + ', ' + str(round(f(x_rp), 5)))



if __name__ == "__main__":
    x_lower, x_upper = 1, 1000
    num = 100
    stop_crit = .1

    Z = 75
    R = 225
    C = 0.6 * 10 ** -6
    L = 0.5
    w = np.linspace(1, 1000, 1001)


    imped_f = lambda w: 1.0 / (np.sqrt(1 / R ** 2 + (w * C - 1 / w * L) ** 2 )) - Z

    func, = plt.plot(w, imped_f(w), 'r')
    func.set_antialiased(False)

    plt.setp(func, 'linewidth', 2.0)
    bisection(imped_f, x_lower, x_upper)
    false_position(imped_f)
    plt.grid(True)
    plt.xlim([x_lower, x_upper])
    plt.show()

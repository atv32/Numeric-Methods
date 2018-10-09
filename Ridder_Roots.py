import math
from numpy import sign, linspace
import matplotlib.pyplot as plt
"""

Find root for f(x) = x^3 - 10x^2 + 5 = 0 within the range (0.6, 0.8) 
via Ridder's Method

"""
def ridder(f, a, b, stop_criterion):
    fa = f(a)

    if fa == 0.0:
        return a

    fb = f(b)

    if fb == 0.0:
        return b

    if sign(f2) is not sign(f3):
        x1 = x3
        f1 = f3

    for i in range(100):  # Compute the improved root x from Ridder’s formula
        c = 0.5*(a + b)
        fc = f(c)
        s = math.sqrt(fc**2 - fa*fb)

        if s == 0.0:
            return None

        dx = (c - a) * fc / s

        if (fa - fb) < 0.0:
            dx = -dx

        x = c + dx
        fx = f(x)

        if i > 0:  # test for convergence
            if abs(x - xOld) < stop_criterion * max(abs(x), 1.0):
                return x

        xOld = x

        if sign(fc) == sign(fx):  # rebracket the root
            if sign(fa) is not sign(fx):
                b = x
                fb = fx

            else:
                a = x
                fa = fx

        else:
            a = c
            b = x
            fa = fc
            fb = fx

    print('Too many iterations')
    return None


x_ax = linspace(0.6, 0.8, 100)

f = lambda x: x ** 3 - 10 * x ** 2 + 5

x1 = 0.6
x2 = 0.8
x3 = 0.7

f1 = f(x1)
f2 = f(x2)
f3 = f(x3)

root = ridder(f, 0.6, 0.8, 1.0e-10)

poly_func, = plt.plot(x_ax, f(x_ax), 'r--')
poly_func.set_antialiased(False)  # turn off antialising
plt.setp(poly_func, 'linewidth', 2.0)

ridder_root, = plt.plot([root], [0], marker='o', label='root')
plt.setp(ridder_root, 'color', 'g', 'linewidth', 2.0)

plt.title('Ridder Roots Solver')
plt.xlabel('X Values')
plt.ylabel('Y Values')

plt.legend((poly_func, ridder_root), ('f(x) = x^3 - 10x^2 + 5', 'Ridder root @ ' + str(round(root, 6))))

plt.grid(True)
plt.show()

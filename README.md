# Numeric-Methods
Scientific Computation for linear algebra, differentiation, integration, optimization

# Examples File : Finding Roots via Incremental, Bisection, Newton-Rhapson, Midpoint, Modified Secant, Fixed-Point Iteration and False Position of real world complex problems

polynomial_roots.py

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
doped_silicon_density.py


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
  effective_impedance_parallel_RLC_circuit,py

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
  
oscillating_current_electrical_circuit.py

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
resonant_frequency_series_RLC_circuit.py

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
ring_shaped_conductor.py

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
  
Simultaneous_nonlinear_equations.py

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
Simultaneous_nonlinear_equationsp2.py

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
sphereical_tank.py

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


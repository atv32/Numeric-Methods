function [results] = approx_first_der_poly(str_funct, str_der_funct, step, x_input)

der_funct=str2func(str_der_funct); % Convert inputs to functions
funct=str2func(str_funct);

f=@(x) funct;  % Handle functions
f_deriv=@(x) der_funct; 

x_init= x_initnput; % Initialize at point x
h= step;  % Assign step size

x_initnit_addone=x_init+h; % Determine x value for one step above/below
x_initnit_minusone=x_init-h;

actual=f_deriv(x_init); % Calculate actual

forward=(f(x_initnit_addone) - f(x_init))/h; % Forward Approximation

backward=(f(x_init)-f(x_initnit_minusone))/h; % Backward Approximation

center=(f(x_initnit_addone)-f(x_initnit_minusone))/(2*h); % Center Approximation

relative_error=abs((actual-[forward backward center].'))/actual*100;
results=[[forward backward center].' relative_error];
end


function [results] = est_err(point, step_size, funct,der_funct)
h=ste_size;
x_init=point;
x_initnit_addone=x_init+h;
x_initnit_minusone=x_init-h;

f=@(x) funct; 
f_deriv_truth=@(x) der_funct; 

center=(f(x_initnit_addone)-f(x_initnit_minusone))./(2*h); % Calculate center difference
total_error=abs(f_deriv_truth(x_init)-center);
results=[h center total_error]
figure
loglog(h,total_error,'Linewidth',2)
grid on
xlabel('Step Size')
ylabel('Total Error')
end


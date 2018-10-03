function [results] = taylor_series(init_pt, init_pt_plus_1)
x_init=init_pt; % Initial Point
x_init_plus_1=init_pt_plus_1; % Point of Interest
h=x_init_plus_1-x_init; % Step between points
f_n_xi=exp(x_init); % Value of derivatives
f_true=exp(x_init_plus_1); % True value
num_terms=6;
terms=zeros(num_terms,1);
for k=1:num_terms
terms(k)=f_n_xi*(h^(k-1))/factorial(k-1);
end
approx=cumsum(terms);
percent_relative_error=abs(f_true-approx)/f_true*100;
results=[(0:(num_terms-1)).' terms approx percent_relative_error];
end


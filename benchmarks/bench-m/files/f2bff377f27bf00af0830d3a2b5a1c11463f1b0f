a = 1;
b = 3;
f = @(x) (100./(x.^2)) .* sin(10./x);

eps = 1e-4;
exact = -1.4260247818;

n1 = 50;
n2 = 100;

aq1 = adquad(a,b, f, eps,n1)
aq2 = adquad(a,b, f, eps,n2)

s1 = simpson(f, a, b, n1)
s2 = simpson(f,a,b,n2)

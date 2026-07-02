def poly_term_derivative(c: float, x: float, n: float) -> float:
    return (c * n) * x**(n-1)
    
c = 3
x = 2
n = 3 
print(poly_term_derivative(c, x, n))
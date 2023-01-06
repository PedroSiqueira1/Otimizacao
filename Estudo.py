### Arquivo com Código Python


def derivative(f, x, dx=0.01):
    """Return the derivative of the function f at the point x.
    The optional argument dx is the small change in x used to compute the
    derivative.  The default value is 0.01.
    """
    return (f(x + dx) - f(x)) / dx

print(derivative(lambda x: x**2, 3, dx=0.0001))

def critical_points_of_function(f, xmin, xmax, dx=0.01):
    """Return the critical points of the function f in the interval [xmin, xmax].
    The optional argument dx is the small change in x used to compute the
    derivative.  The default value is 0.01.
    """
    critical_points = []
    x = xmin
    while x <= xmax:
        if derivative(f, x, dx) == 0:
            critical_points.append(x)
        x += dx
    return critical_points

    
print(critical_points_of_function(lambda x: x**2, -10, 10, dx=0.00001))
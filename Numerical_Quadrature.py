def Numerical_Quadrature(e, i, quad_type, h):
    # Define the basis functions associated with the element
    def phi(e, j):
        if j == 1:
            return 1 - e
        elif j == 2:
            return e
        else:
            return 0

    # Define the function f(x) to be integrated
    def f(x):
        return -12*x**2 + 18*x + 6

    # Calculate the nodes x_j and x_{j+1} for the element
    x_j = (i - 1) * h
    x_jplus1 = i * h

    # Perform numerical quadrature using the trapezoidal rule
    if quad_type == 1:
        if i == 1:
            fe_i = (h/2) * f(x_j) * phi(e, 1)
        elif i == 2:
            fe_i = (h/2) * f(x_jplus1) * phi(e, 2)
        else:
            fe_i = 0
    else:
        raise ValueError("Invalid quadrature. supports only: 'trapezoidal'")

    return fe_i
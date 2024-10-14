import numpy as np

def Jacobi_Iteration(A, B, C, f, x0, eps, max_iter=1000):
    N = len(f)
    x = np.copy(x0)
    r = np.zeros_like(x)
    
    for iteration in range(max_iter):
        x_new = np.zeros_like(x)
        
        # Update each component of x
        for i in range(N):
            sum_ = 0
            if i > 0:
                sum_ += B[i-1] * x[i-1]  # contribution from sub-diagonal
            if i < N-1:
                sum_ += C[i] * x[i+1]  # contribution from super-diagonal
            x_new[i] = (f[i] - sum_) / A[i]

        #the residual
        r = np.copy(f)  #start with the right-hand side
        for i in range(N):
            r[i] -= A[i] * x_new[i]
            if i > 0:
                r[i] -= B[i-1] * x_new[i-1]
            if i < N-1:
                r[i] -= C[i] * x_new[i+1]

        # Check convergence using the infinity norm
        norm = np.linalg.norm(r, ord=np.inf)
        if norm < eps:
            break
        
        x = x_new
    
    return x, norm, iteration + 1

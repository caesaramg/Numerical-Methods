import numpy as np

def Gaussian_Elimination(A,B,C, f):
    A2=np.copy(A)
    B2=np.copy(B)
    C2=np.copy(C)
    f2=np.copy(f)
    n=len(A)
    X=np.zeros(n)
    #first we will implement forward eliminition
    for i in range (1,n):
        div= B2[i-1]/A2[i-1]
        A2[i]-=  div*C2[i-1]
        f2[i]-= div*f2[i-1]
    #now time for backward sub
    X[n-1]=f2[n-1]/A2[n-1]
    for c in range(n-2,-1,-1):
        X[c]=(f2[c]-C2[c]*X[c+1])/A2[c]
    return(X)
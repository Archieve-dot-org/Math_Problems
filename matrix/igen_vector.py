import numpy as np

def igen_vector(a):
    A = np.array(a)
    t = A.T
    In = np.identity(2)
    print(A)

A = [[1,2],
     [3,4]]

igen_vector( A )

print(np.linalg.eig(A))

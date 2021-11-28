import numpy as np
import sympy as sp

def gauss_jordan(x, y, verbose=0):
    m, n = x.shape
    augmented_mat = np.zeros(shape=(m, n + 1))
    augmented_mat[:m, :n] = x
    augmented_mat[:, m] = y
    np.set_printoptions(precision=2, suppress=True)
    if verbose > 0:
        print('# Original augmented matrix')
        print(augmented_mat)
    outer_loop = [[0, m - 1, 1], [m - 1, 0, -1]]
    for d in range(2):
        for i in range(outer_loop[d][0], outer_loop[d][1], outer_loop[d][2]):
            inner_loop = [[i + 1, m, 1], [i - 1, -1, -1]]
            for j in range(inner_loop[d][0], inner_loop[d][1], inner_loop[d][2]):
                k = (-1) * augmented_mat[j, i] / augmented_mat[i, i]
                temp_row = augmented_mat[i, :] * k
                if verbose > 1:
                    print('# Use line %2i for line %2i' % (i + 1, j + 1))
                    print('k=%.2f' % k, '*', augmented_mat[i, :], '=', temp_row)
                augmented_mat[j, :] = augmented_mat[j, :] + temp_row
                if verbose > 1:
                    print(augmented_mat)
    for i in range(0, m):
        augmented_mat[i, :] = augmented_mat[i, :] / augmented_mat[i, i]
    if verbose > 0:
        print('# Normalize the rows')
        print(augmented_mat)
    return augmented_mat[:, n]

def jacobi(a, b, x0 = np.array([0,0,0]), tol = 0.00001, iter_max = 10):
    """
    Jacobi method: solve Ax = b given an initial approximation x0
    Parameters:
        a: Matrix A from system Ax=b
        b: Array containing b values
        x0: Initial approximation of solution
        tol: Tolerance
        iter_max: Maximum number of iterations
    Returns:
        x: Solution of linear system
        iter: Used iterations
    """

    # D and M matrices
    d = np.diag(np.diag(a))
    m = a - d

    # Iterative process
    i = 1
    x = None
    for i in range(1, iter_max + 1):
        x = np.linalg.solve(d, (b - np.dot(m, x0)))
        err = np.linalg.norm(x - x0, np.inf) / np.linalg.norm(x, np.inf)
        var = np.linalg.norm(x - x0, np.inf)
        print(f"iteration {i}: x = {x}; err = {err}; var = {var}")
        if np.linalg.norm(x - x0, np.inf) / np.linalg.norm(x, np.inf) <= tol:
            break
        x0 = x.copy()

    return [x, i]

def gauss_seidel(a, b, x0 = np.array([0,0,0]), tol = 0.00001, iter_max = 10):
    """
    Gauss-Seidel method: solve Ax = b given an initial approximation x0
    Parameters:
        a: Matrix A from system Ax=b
        b: Array containing b values
        x0: Initial approximation of solution
        tol: Tolerance
        iter_max: Maximum number of iterations
    Returns:
        x: Solution of linear system
        iter: Used iterations
    """

    # L and U matrices
    lower = np.tril(a)
    upper = a - lower

    # Iterative process
    i = 1
    x = None
    for i in range(1, iter_max + 1):
        x = np.linalg.solve(lower, (b - np.dot(upper, x0)))

        if np.linalg.norm(x - x0, np.inf) / np.linalg.norm(x, np.inf) <= tol:
            break
        x0 = x.copy()

    return [x, i]

def gauss_jordan2():
    m = sp.Matrix([[1, -1, 2, -1],
           [2, -1, 3, -3],
           [1,1,1, 0],
            [1, -1, 4, 3]])

    m_rref, pivots = m.rref() # Compute reduced row echelon form (rref).

    print(m_rref, pivots)

def main():
    a = np.array([[1, 1, 0.2], [0.3, 2, 2], [0.5, 0.1, 3]])
    b = np.array([1,7, 2])
    x = np.array([0, 0, 0])
    sol = jacobi(a, b, iter_max=16)
    print(sol)

if __name__ == '__main__':
    main()
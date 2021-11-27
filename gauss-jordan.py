import sympy as sp

m = sp.Matrix([[1, -1, 2, -1],
           [2, -1, 3, -3],
           [1,1,1, 0],
            [1, -1, 4, 3]])

m_rref, pivots = m.rref() # Compute reduced row echelon form (rref).

print(m_rref, pivots)
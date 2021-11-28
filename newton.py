import sympy as sym
from tabulate import tabulate

interval = sym.Interval(-0.1, 0.0)
x = sym.Symbol("x")
f_x = 6*x**2 + 9*x**2 + 15*x +1

def f(f_x, val):
    return f_x.evalf(subs={x: val})

def min(x, y):
    return abs(x) if abs(x) < abs(y) else abs(y)

def max(x, y):
    return abs(x) if abs(x) > abs(y) else abs(y)

def newton(f_x, x0, epsilon = 0.00001, max_iter = 10):
    xn = x0
    Dfxn = sym.diff(f_x, x)
    ddf = sym.diff(f_x, x, x)
    m_1 = min(sym.maximum(Dfxn, x, interval), sym.minimum(Dfxn, x, interval))
    M_2 = max(sym.maximum(ddf, x, interval), sym.minimum(ddf, x, interval))
    lst_x = []
    lst_e = []
    lst_e1 = []
    for n in range(0,max_iter):
        fxn = f(f_x, xn)
        lst_x.append(xn)
        lst_e1.append(abs(fxn/m_1))
        if n <=1:
            lst_e.append(0)
        else:
            lst_e.append((M_2/(2*m_1)) * (abs(lst_x[n] - lst_x[n - 1]) ** 2))
        #if abs(xn - (xn - fxn/f(Dfxn, xn))) < epsilon:
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            i = range(0, len(lst_x))
            table = zip(i , lst_x, lst_e1, lst_e)
            headers = ["i", "xn", "e1", "e2"]
            print(tabulate(table, headers=headers, tablefmt='pretty'))
            print()
            print("m1 = " + str(m_1) + " M_2 = " + str(M_2))
            return xn
        if f(Dfxn, xn) == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/f(Dfxn, xn)
    
    
    
    print('Exceeded maximum iterations. No solution found.')
    return None


def main():
    newton(f_x, 0)

if __name__ == '__main__':
    main()


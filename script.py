import sympy as sym
from tabulate import tabulate
x = sym.Symbol('x')

def eval(f, val):
    return f.evalf(subs={x: val})


def bi(f, a, b):
    lst_c = []
    lst_e = []
    a = 0
    b = 1
    for i in range(10):
        f_a = eval(f, a)
        f_b = eval(f, b)
        c = (a + b) / 2
        lst_c.append(float(c))
        f_c = eval(f, c)
        e = abs(b - a) / (2 ** (i + 1))
        lst_e.append(float(e))
        if f_c * f_a < 0:
            b = c
        else:
            a = c

    i = range(0, len(lst_c))
    table = zip(i, lst_c, lst_e)
    headers = ["i", "c", "e"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))

def f(f_x, val):
    return f_x.evalf(subs={x: val})


def fp(f_x, x0, x1, e=0.0001):
    step = 1
    diff_f = sym.diff(f_x, x)
    ivl = sym.Interval (x0, x1)
    if abs(sym.minimum(diff_f, x, ivl)) < abs(sym.maximum(diff_f, x, ivl)):
        m = abs(sym.minimum(diff_f, x, ivl))
        M = abs(sym.maximum(diff_f, x, ivl))
    else:
        m = abs(sym.maximum(diff_f, x, ivl))
        M = abs(sym.minimum(diff_f, x, ivl))

    print("\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***")
    condition = True
    lst_x = []
    lst_e1 = []
    lst_e2 = []
    while condition:
        x2 = x0 - (x1 - x0) * f(f_x, x0) / (f(f_x, x1) - f(f_x, x0))
        lst_x.append(x2)
        print("Iteration-%d, x2 = %0.8f and f(x2) = %0.8f" % (step, x2, f(f_x, x2)))
        # print()
        if f(f_x, x0) * f(f_x, x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(f_x, x2)) > e
        err_1 = abs(f(f_x, x2)) / m
        lst_e1.append(err_1)
        # lst_e2.append(err_2)

    print("\nRequired root is: %0.8f" % x2)
    print(f"f'x = {sym.diff(f_x, x)}")
    print(f"f\"x = {sym.diff(f_x, x, x)}")
    print(f"m = {m}, M = {M}")
    print("Error 1 is: %0.8f" %abs(f(f_x, x2)/m))


def min(x, y):
    return abs(x) if abs(x) < abs(y) else abs(y)

def max(x, y):
    return abs(x) if abs(x) > abs(y) else abs(y)

def nton(f_x, x0, a, b,  epsilon = 0.00001, max_iter = 10):
    xn = x0
    interval = sym.Interval(a, b)
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
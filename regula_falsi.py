import sympy as sym
from tabulate import tabulate
x = sym.Symbol("x")
f_x = 1.2 * x**5 - 2.57*x + 2


def f(f_x, val):
    return f_x.evalf(subs={x: val})


def falsePosition(f_x, x0, x1, e):
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
def main():
    
    # sol = sym.nsolve(f_x, -1.3)
    # print(sol)
    x0 = input("First Guess: ")
    x1 = input("Second Guess: ")
    e = input("Tolerable Error: ")

    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    if f(f_x, x0) * f(f_x, x1) > 0.0:
        print("Given guess values do not bracket the root.")
        print("Try Again with different guess values.")
    else:
        falsePosition(f_x, x0, x1, e)

if __name__ == '__main__':
    main()

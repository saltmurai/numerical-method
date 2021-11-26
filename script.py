import sympy as sym
from tabulate import tabulate

x = sym.Symbol("x")
f = 5 * x ** 3 - sym.cos(3 * x)


def eval(f, val):
    return f.evalf(subs={x: val})


def chia_doi(f):
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
        e = (1 - 0) / (2 ** (i + 1))
        lst_e.append(float(e))
        if f_c * f_a < 0:
            b = c
        else:
            a = c

    i = range(0, len(lst_c))
    table = zip(i, lst_c, lst_e)
    headers = ["i", "c", "e"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))


def main():
    chia_doi(f)


if __name__ == "__main__":
    main()

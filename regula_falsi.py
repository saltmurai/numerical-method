import sympy as sym


def eval(f):
    return


def f(x):
    return x ** 3 + 3 * x ** 2 - 1


def falsePosition(x0, x1, e):
    step = 1
    print("\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***")
    condition = True
    while condition:
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print("Iteration-%d, x2 = %0.6f and f(x2) = %0.6f" % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print("\nRequired root is: %0.8f" % x2)

def main():
    x0 = input("First Guess: ")
    x1 = input("Second Guess: ")
    e = input("Tolerable Error: ")

    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    if f(x0) * f(x1) > 0.0:
        print("Given guess values do not bracket the root.")
        print("Try Again with different guess values.")
    else:
        falsePosition(x0, x1, e)

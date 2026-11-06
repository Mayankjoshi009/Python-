import numpy as np

def f(x):
    return 1 / (1 + x**2)

def trapezoidal(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2.0) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson13(a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals 'n' must be even for Simpson's 1/3 rule.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3.0) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

a, b, n = 0.0, 1.0, 6
exact = np.pi / 4

i_trap = trapezoidal(a, b, n)
i_simp = simpson13(a, b, n)

print(f"Exact Analytical Integral (pi/4): {exact:.6f}")
print(f"Trapezoidal Rule (n={n}): {i_trap:.6f} | Error: {abs(i_trap - exact):.6f}")
print(f"Simpson's 1/3 Rule (n={n}): {i_simp:.6f} | Error: {abs(i_simp - exact):.6f}")
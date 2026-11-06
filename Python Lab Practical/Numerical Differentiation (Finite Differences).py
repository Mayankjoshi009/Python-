import numpy as np

def f(x):
    return np.sin(x)

def exact_df(x):
    return np.cos(x)

x_val = np.pi / 4   # 45 degrees
h = 0.1

df_forward  = (f(x_val + h) - f(x_val)) / h
df_backward = (f(x_val) - f(x_val - h)) / h
df_central  = (f(x_val + h) - f(x_val - h)) / (2 * h)
exact = exact_df(x_val)

print(f"Exact Derivative cos(pi/4): {exact:.6f}")
print(f"Forward Difference:  {df_forward:.6f} | Error: {abs(df_forward - exact):.6f}")
print(f"Backward Difference: {df_backward:.6f} | Error: {abs(df_backward - exact):.6f}")
print(f"Central Difference:  {df_central:.6f} | Error: {abs(df_central - exact):.6f}")




import matplotlib.pyplot as plt

hs = np.logspace(-6, 0, 50)
err_f = np.abs((f(x_val + hs) - f(x_val)) / hs - exact)
err_b = np.abs((f(x_val) - f(x_val - hs)) / hs - exact)
err_c = np.abs((f(x_val + hs) - f(x_val - hs)) / (2 * hs) - exact)

plt.loglog(hs, err_f, label="Forward")
plt.loglog(hs, err_b, label="Backward")
plt.loglog(hs, err_c, label="Central")
plt.xlabel("Step size h")
plt.ylabel("Absolute error")
plt.title("Error vs Step Size")
plt.legend()
plt.grid(True, which="both")
plt.show()
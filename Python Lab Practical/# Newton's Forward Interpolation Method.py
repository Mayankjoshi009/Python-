# Newton's Forward Interpolation Method

x = [0, 1, 2, 3]
y = [1, 2, 5, 10]

n = len(x)
diff = [y.copy()]

# Construct forward difference table
for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i - 1][j + 1] - diff[i - 1][j])
    diff.append(temp)

value = float(input("Enter the value of x: "))

h = x[1] - x[0]
u = (value - x[0]) / h

result = y[0]
u_term = 1
factorial = 1

for i in range(1, n):
    u_term *= (u - (i - 1))
    factorial *= i
    result += (u_term / factorial) * diff[i][0]

print("Interpolated value of y =", result)
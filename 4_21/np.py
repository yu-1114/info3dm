import numpy as np

a = np.array([[1], [1], [1], [1], [1]], dtype=float)
print("課題(1)\n", a)

a[2] = 3.14
print("課題(2)\n", a)

b = a
print("課題(3)\n", b.T)

ip = np.dot(a, b.T)
print("課題(4)\n", ip)

c = np.random.rand(10, 1)
print("課題(5)\n", c)

d = np.random.normal(10, 2, size=(2, 5))
print("課題(6)\n", d)

print("課題(7)\n", d[:, 1])
print("課題(8)\n", d[:, 3:5])

e = np.random.rand(5, 2)
pr = np.dot(d, e)
print("課題(9-1)\n", e)
print("課題(9-2)\n", pr)
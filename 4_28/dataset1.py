import numpy as np
import unittest
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

x = np.linspace(-1, 1, 500)
y = true_function(x)

plt.figure(figsize=(8, 6))

plt.plot(x, y, label=r'$y = 10 \sin(0.8 \pi x)$')

plt.title('True Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--')

plt.legend()

plt.savefig('ex1.1.png')

plt.show()

class TestTrueFunction(unittest.TestCase):
    def test_y_is_zero_when_x_is_zero(self):
        x = np.array([0.0])
        expected = 0.0
        
        actual = true_function(x)
        
        np.testing.assert_allclose(actual, expected, atol=1e-15)

if __name__ == '__main__':
    unittest.main()

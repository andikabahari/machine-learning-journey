import numpy as np
import random
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([2,5,6,7,8], dtype=np.float64)

def create_dataset(n, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(n):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
    m_numerator = np.mean(xs) * np.mean(ys) - np.mean(xs * ys)
    m_denumerator = np.mean(xs) ** 2 - np.mean(xs ** 2)
    m = m_numerator/m_denumerator
    b = np.mean(ys) - m * np.mean(xs)
    return m, b

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) ** 2)

def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [np.mean(ys_orig) for _ in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - squared_error_regr / squared_error_y_mean

xs, ys = create_dataset(40, 10, 2, correlation='pos')

m, b = best_fit_slope_and_intercept(xs, ys)

regression_line = [m * x + b for x in xs]

predict_x = 8
predict_y = m * predict_x + b

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, s=100, color='g')
plt.plot(xs, regression_line)
plt.show()

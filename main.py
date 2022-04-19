from src.spline import spline as spl
import numpy as np
import matplotlib.pyplot as plt


def plot_data(input_x, input_y, result_x, result_y):
    print("implement me!")
    plt.plot(input_x, input_y, "xb")
    plt.plot(result_x, result_y, "-r")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


def import_data() -> (list, list):
    print("implement me")
    x = [1, 2, 3]
    y = [4, 5, 4]
    return x, y


def calculate_by_cubic_spline(x, y) -> (list, list):
    print("implement me")
    spline = spl.new_spline(x, y)
    # todo how to define range?
    rx = np.arange(-2.0, 4, 0.01)
    ry = [spline.calc(i) for i in rx]
    return rx, ry


if __name__ == '__main__':
    x_input, y_input = import_data()
    x_res, y_res = calculate_by_cubic_spline(x_input, y_input)
    plot_data(x_input, y_input, x_res, y_res)

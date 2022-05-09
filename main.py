from src.spline import spline as spl
import numpy as np
import matplotlib.pyplot as plt


def plot_data(input_x, input_y, result_x, result_y):
    print("implement me!")
    plt.plot(input_x, input_y, "xb")
    plt.plot(result_x, result_y, "-r")
    plt.grid(True)
    plt.show()


def import_data() -> (list, list):
    print("implement me")
    x = [
        10, 11, 11.5, 12, 13,
        14, 15, 15.5, 16, 17,
        17.5, 18, 19, 20, 20.5,
        21, 21.5, 22, 23, 24,
        25, 26, 27, 28, 29,
        30, 31, 32, 33, 34,
        35, 35.5, 36, 37, 38,
        39, 39.5, 40, 41,
    ]

    y = [
        153, 122, 118, 117, 188,
        121, 124, 130, 121, 130,
        140, 134, 139, 142, 132,
        133, 128, 129, 128, 111,
        99, 109, 102, 133, 98,
        100, 118, 110, 140, 153,
        122, 118, 117, 188, 121,
        124, 130, 121, 130
    ]
    return x, y


def calculate_by_cubic_spline(x, y) -> (list, list):
    print("implement me")
    spline = spl.new_spline(x, y)
    # todo how to define range?
    rx = np.arange(1, 200, 0.01)
    ry = [spline.calc(i) for i in rx]
    return rx, ry


if __name__ == '__main__':
    x_input, y_input = import_data()
    x_res, y_res = calculate_by_cubic_spline(x_input, y_input)
    plot_data(x_input, y_input, x_res, y_res)

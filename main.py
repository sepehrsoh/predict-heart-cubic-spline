from src.spline import spline as spl
import numpy as np
import matplotlib.pyplot as plt


def plot_data(input_x, result_x, input_ymax, result_ymax, input_ymin, result_ymin):
    plt.plot(input_x, input_ymax, "xb")
    plt.plot(result_x, result_ymax, "-r")
    plt.plot(input_x, input_ymin, "xr")
    plt.plot(result_x, result_ymin, "-b")
    plt.grid(True)
    plt.show()


def import_data() -> (list, list, list):
    x = [
        10, 11, 11.5, 12, 13,
        14, 15, 15.5, 16, 17,
        17.5, 18, 19, 20, 20.5,
        21, 21.5, 22, 23, 24,
        25, 26, 27, 28, 29,
        30, 31, 32,
        33, 34, 35, 35.5, 36,
        37, 38, 39, 39.5, 40,
        41,
    ]

    ymax = [
        153, 122, 118, 117, 188,
        121, 124, 130, 121, 130,
        140, 134, 139, 142, 132,
        133, 128, 129, 128, 111,
        99, 109, 102, 133, 98,
        100, 118, 110,
        153, 122, 118, 117, 188,
        121, 124, 130, 121, 130,
        140,
    ]
    ymin = [
        110, 90, 77, 72, 88,
        80, 80, 90, 80, 88,
        100, 90, 92, 98, 80,
        80, 83, 80, 80, 58,
        69, 64, 65, 77, 65,
        67, 77, 70,
        110, 90, 77, 72, 88,
        80, 80, 90, 80, 88,
        100,
    ]
    return x, ymax, ymin


def calculate_by_cubic_spline(x, y) -> (list, list):
    spline = spl.new_spline(x, y)
    # todo how to define range?
    rx = np.arange(1, 200, 0.01)
    ry = [spline.calc(i) for i in rx]
    return rx, ry


if __name__ == '__main__':
    x_input, ymax_input, ymin_input = import_data()
    x_res, ymax_res = calculate_by_cubic_spline(x_input, ymax_input)
    x_res, ymin_res = calculate_by_cubic_spline(x_input, ymin_input)
    plot_data(x_input, x_res, ymax_input, ymax_res, ymin_input, ymin_res)

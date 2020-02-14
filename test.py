import matplotlib.pyplot as plt
import numpy as np

from tsp_solvers import solve_tsp
from mtsp_solvers import solve_mtsp

########################################## test functions #################################################

from utils import build_matrix, calc_len, plot_tour, plot_tours


def get_test_data(num=100):
    points = np.random.normal(size=(num, 2))
    matrix = build_matrix(points)

    return points, matrix


def test_tsp_concord(matrix, points):
    res = solve_tsp(matrix, 'concorde')
    points_res = points[res]
    print('Len:', calc_len(points_res))
    plot_tour(points_res, col='b')


def test_tsp_lkh(matrix, points):
    res = solve_tsp(matrix, 'lkh')
    points_res = points[res]
    print('Len:', calc_len(points_res))
    plot_tour(points_res, col='g')


def test_mtsp_lkh(matrix, points, m, depot=0):
    res = solve_mtsp(matrix, solver='lkh', m=m, depot=depot)
    plot_tours(res, points)


def test_mtsp_or_tools(matrix, points, m, depot=0):
    res = solve_mtsp(matrix, solver='ortools', m=m, depot=depot)
    plot_tours(res, points, col='g')


def test_mtsp_best(matrix, points, m, depot=0):
    res = solve_mtsp(matrix, solver='best', m=m, depot=depot)
    plot_tours(res, points)


if __name__ == '__main__':
    POINTS_NUM = 100
    num_vehicles = 4

    points, matrix = get_test_data(POINTS_NUM)
    # test_tsp_concord(matrix, points)
    # test_tsp_lkh(matrix, points)
    # test_mtsp_lkh(matrix, points, m=num_vehicles)
    test_mtsp_best(matrix, points, m=num_vehicles)

    plt.show()

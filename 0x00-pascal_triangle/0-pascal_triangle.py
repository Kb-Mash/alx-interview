#!/usr/bin/python3
""" Module for pascal_triangle function """


def pascal_triangle(n):
    """ Creates a pascal triangle """
    triangle = []
    if (n <= 0):
        return triangle
    triangle.append([1])
    for i in range(n - 1):
        triangle.append([1] + [triangle[i][j] + triangle[i][j + 1]
                    for j in range(len(triangle[i]) - 1)] + [1])
    return triangle

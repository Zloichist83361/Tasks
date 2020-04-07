def line_split(line):
    return list(map(float, line.strip().split(" ")))


rectangle_coordinates = []
with open('File1.txt') as f:
    for line in f:
        rectangle_coordinates.append(line_split(line))
print(rectangle_coordinates)

points = []
with open('File2.txt') as f:
    for line in f:
        points.append(line_split(line))
print(points)


def check(A, B, C):
    A = [float(item) for item in A]
    B = [float(item) for item in B]
    C = [float(item) for item in C]
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def point_location(P, A):
    if (check(P[0], P[1], A) > 0 or check(P[0], P[3], A) < 0 or check(P[2], P[1], A) < 0 or
            check(P[2], P[3], A) > 0):  # проверить вне фигуры
        return 3
    elif (check(P[0], P[1], A) < 0 and check(P[0], P[3], A) > 0) and (
            check(P[2], P[1], A) > 0 and check(P[2], P[3], A) < 0):  # проверить внутри фигуры
        return 2
    elif check(P[0], P[2], A) == 0 or check(P[1], P[3], A) == 0:
        return 0  # проверить угловые точки
    else:
        return 1  # точка на фигуре


for point in points:
    print(point_location(rectangle_coordinates, point))

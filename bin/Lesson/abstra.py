# x = 2, y = 2
point = 2, 3
x, y = point
symmetrical_point = x, -y

def get_middle_point(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

point1 = 2, 3
point2 = -4, 1
print(get_middle_point(point1, point2))

def calculate_distance(point1, point2) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
point1 = 0, 0
point2 = 3, 4
print(calculate_distance(point1, point2))

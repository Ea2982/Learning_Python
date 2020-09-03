import math


def make_descartes_point(x, y):
    return {
        'angle': math.atan2(y, x),
        'radius': math.sqrt(x ** 2 + y ** 2)
    }
def get_angle(point):
    return point['angle']

def get_radius(point):
    return point['radius']

def get_x(point):
    return get_radius(point) * math.cos(get_angle(point))

def get_y(point):
    return get_radius(point) * math.sin(get_angle(point))

x = 4
y = 8
point = make_descartes_point(x, y)
print(get_x(point))
print(get_y(point))
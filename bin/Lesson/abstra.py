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

point = {'x': 2, 'y': 3}
symmetrical_point = {
    'x': - point['x'],
    'y': point['y'],
}
print(symmetrical_point)

point1 = {'x': 3, 'y': 4}
point2 = {'x': -8, 'y': 10}
segment = {
    'begin_point': point1,
    'end_point': point2,
}
print(segment)
print(point1['x'])
print(point2['y'])
print(segment['begin_point'])
print(segment['begin_point']['x'])
print(segment['end_point'])
print(segment['end_point']['x'])
import math
def make_descartes_point(x, y):
    return {'x': x, 'y': y}
def make_descartes_point_rad(x, y):
    return {
        'angle': math.atan2(y, x),
        'radius': math.sqrt(x ** 2 + y ** 2)
    }
def get_x(point):
    return point['x']
def get_y(point):
    return point['y']
print('/' + '-' * 80 + '/\n')
point = make_descartes_point(3, 4)
print(get_y(point))
symmetrical_point = make_descartes_point(-get_x(point), get_y(point))
print(symmetrical_point)

def make_segment(point1, point2):
    return {
        'begin': {
            'x': get_x(point1),
            'y': get_y(point1),
        },
        'end': {
            'x': get_x(point2),
            'y': get_y(point2),
        }
    }
def get_mid_point_of_segment(segment):
    x1 = get_x(segment['begin'])
    x2 = get_x(segment['end'])
    y1 = get_y(segment['begin'])
    y2 = get_y(segment['end'])
    dct = {
        'x': (x1 + x2) / 2,
        'y': (y1 + y2) / 2,
    }
    print(dct)
    return dct
segment = make_segment(make_descartes_point(3, 2), make_descartes_point(0, 0))
print(segment)
get_mid_point_of_segment(segment)

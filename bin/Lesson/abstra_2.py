import math
def get_ang_rad(point):
    return {
        point['angle'],
        point['radius']
    }

def make_descartes_point(x, y):
    return {
        'angle': math.atan2(y, x),
        'radius': math.sqrt(x ** 2 + y ** 2)
    }
def get_x(point):
    radius, angle = get_ang_rad(point)
    return radius * math.cos(angle)

def get_y(point):
    radius, angle = get_ang_rad(point)
    return radius * math.sin(angle)

x = 4
y = 8
point = make_descartes_point(x, y)
print(get_x(point))
print(get_y(point))
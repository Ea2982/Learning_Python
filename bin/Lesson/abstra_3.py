import math

def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None

def make_rectangle(point, width, height):
    return {
        'start_point': point,
        'width': width,
        'height': height,
    }

def get_width(rectangles):
    return rectangles['width']

def get_height(rectangles):
    return rectangles['height']

def get_start_point(rectangles):
    return rectangles['start_point']

def contains_origin(rectangles):
    w = get_width(rectangles)
    h = get_height(rectangles)

    point1 = get_start_point(rectangles)
    print('point1: ', point1, 'get_quadrant: ', get_quadrant(point1))
    point2 = make_decart_point(
        get_x(point1) + w,
        get_y(point1)
    )
    print('point2: ', point2, 'get_quadrant: ', get_quadrant(point2))
    point3 = make_decart_point(
        get_x(point1) + w,
        get_y(point1) - h
    )
    print('point3: ', point3, 'get_quadrant: ', get_quadrant(point3))
    point4 = make_decart_point(
        get_x(point1),
        get_y(point1) - h
    )
    print('point4: ', point4, 'get_quadrant: ', get_quadrant(point4))
    p = list()
    p.append(get_quadrant(point1))
    p.append(get_quadrant(point2))
    p.append(get_quadrant(point3))
    p.append(get_quadrant(point4))
    if None in p:
        return False
    return True
p = make_decart_point(-4, 3)
rectangles = make_rectangle(p, 5, 4)
print(rectangles)
print(contains_origin(rectangles))
rectangles = make_rectangle(p, 5, 2)
print(rectangles)
print(contains_origin(rectangles))
rectangles = make_rectangle(p, 2, 2)
print(rectangles)
print(contains_origin(rectangles))
rectangles = make_rectangle(p, 4, 3)
print(rectangles)
print(contains_origin(rectangles))
point = make_decart_point(0, 1)
rectangles = make_rectangle(point, 4, 5)
print(rectangles)
print(contains_origin(rectangles))



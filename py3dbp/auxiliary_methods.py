from decimal import Decimal
from .constants import Axis


def rect_intersect(item1, item2, x, y):
    d1 = item1.get_dimension()
    d2 = item2.get_dimension()

    cx1 = item1.position[x] + d1[x]/2
    cy1 = item1.position[y] + d1[y]/2
    cx2 = item2.position[x] + d2[x]/2
    cy2 = item2.position[y] + d2[y]/2

    ix = max(cx1, cx2) - min(cx1, cx2)
    iy = max(cy1, cy2) - min(cy1, cy2)

    return ix < (d1[x]+d2[x])/2 and iy < (d1[y]+d2[y])/2

def intersection_area(a, b):  # calculate intersection area of 2 rectanglees

    dimension_A = a.get_dimension()
    dimension_B = b.get_dimension()
    
    dx = min(float(a.position[0])+float(dimension_A[0]), float(b.position[0])+float(dimension_B[0])) - max(float(a.position[0]), float(b.position[0]))
    dy = min(float(a.position[2])+float(dimension_A[2]), float(b.position[2])+float(dimension_A[2])) - max(float(a.position[2]), float(b.position[2]))

    if (dx>=0) and (dy>=0):
        return dx*dy
    return 0

def intersect(item1, item2):
    return (
        rect_intersect(item1, item2, Axis.WIDTH, Axis.HEIGHT) and
        rect_intersect(item1, item2, Axis.HEIGHT, Axis.DEPTH) and
        rect_intersect(item1, item2, Axis.WIDTH, Axis.DEPTH)
    )


def get_limit_number_of_decimals(number_of_decimals):
    return Decimal('1.{}'.format('0' * number_of_decimals))


def set_to_decimal(value, number_of_decimals):
    number_of_decimals = get_limit_number_of_decimals(number_of_decimals)

    return Decimal(value).quantize(number_of_decimals)

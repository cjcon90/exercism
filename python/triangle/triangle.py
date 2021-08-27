def equilateral(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_valid_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 3

def is_valid_triangle(sides):
    for side in sides:
        if not side or side > sum(sides) - side:
            return False
    return True

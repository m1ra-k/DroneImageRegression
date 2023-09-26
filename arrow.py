import math

def calculate_endpoint(starting_point, length, rotation):
    radians = math.radians(90-rotation)
    x = int(starting_point[0] + length * math.cos(radians))
    y = int(starting_point[1] - length * math.sin(radians))
    return [x, y]
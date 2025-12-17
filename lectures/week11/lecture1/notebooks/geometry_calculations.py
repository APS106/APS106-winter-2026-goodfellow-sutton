import math


def rectangle_area(length, width):
    """
    (number, number) -> number
    Calculate the area of a rectangle.
    """
    return length * width


def circle_area(radius):
    """
    (number) -> number
    Calculate the area of a circle.
    """
    return math.pi * radius**2


def cylinder_volume(radius, height):
    """
    (number, number) -> number
    Calculate the volume of a cylinder.
    """
    return math.pi * radius**2 * height


def rectangular_prism_volume(length, width, height):
    """
    (number, numner, number) -> number
    Calculate the volume of a rectangular prism (3D rectangle).
    """
    return length * width * height


def cylinder_surface_area(radius, height):
    """
    (number, number) -> number
    Calculate the surface area of a cylinder.
    """
    return 2 * math.pi * radius * (radius + height)


def rectangular_prism_surface_area(length, width, height):
    """
    (number, number, number) -> number
    Calculate the surface area of a rectangular prism (3D rectangle).
    """
    return 2 * (length*width + length*height + width*height)

"""
The intention of this file is to hold the logic of all possible card attributes
which means: Shape, Color, Quantity and Shade.
"""
from utils import prepare_text


class Attribute(object):
    """Common class to hold constants and value validation of each card"""

    def __init__(self, constants, value):
        self.__constants = constants
        self.value = self.__valid_value(value)

    def __valid_value(self, value):
        value = prepare_text(value)
        if value in self.__constants:
            return value
        else:
            raise ValueError(f'Invalid Input:{value}')

    def __str__(self):
        return f'{self.value}'


class Shape(Attribute):
    """
    Representaion of the three possible shapes:
    Ovals, Diamonds and Squiggles.
    """

    SHAPES = ['ovals', 'diamonds', 'squiggles']

    def __init__(self, value):
        super(Shape, self).__init__(self.SHAPES, value)


class Color(Attribute):
    """
    Representaion of the three possible colors:
    Red, Green and Purple.
    """

    COLORS = ['red', 'green', 'purple']

    def __init__(self, value):
        super(Color, self).__init__(self.COLORS, value)


class Quantity(Attribute):
    """
    Representaion of the three possible Quantities:
    One, Two and Three.
    """

    QUANTITIES = ['one', 'two', 'three']

    def __init__(self, value):
        super(Quantity, self).__init__(self.QUANTITIES, value)


class Shade(Attribute):
    """
    Representaion of the three possible shades:
    Solid, Striped and Open (or None).
    """

    SHADES = ['solid', 'striped', 'open']

    def __init__(self, value):
        super(Shade, self).__init__(self.SHADES, value)

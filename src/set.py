import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from attribute import Shape, Color, Quantity, Shade
from itertools import combinations


class SetEvaluator(object):
    """Evaluate if the selected cards are a 'set' or not"""

    def is_set(self, cards):
        NUMBER_OF_REQUIRED_CARDS = 3

        if len(cards) != NUMBER_OF_REQUIRED_CARDS:
            return 'You must provide 3 cards'

        shapes, colors, quantities, shades = self._get_cards_attributes(cards)

        # If they are all equal, the set of an array should contain only 1 element
        # If they are all different, the set of an array should be equal to its original version.
        valid_shape = len(set(shapes)) == 1 or len(shapes) == len(set(shapes))
        valid_color = len(set(colors)) == 1 or len(colors) == len(set(colors))
        valid_quantity = len(set(quantities)) == 1 or len(quantities) == len(set(quantities))
        valid_shade = len(set(shades)) == 1 or len(shades) == len(set(shades))

        is_set = all([valid_shape, valid_color, valid_quantity, valid_shade])
        return is_set

    # TODO: Improve the funciont to avoid using .value.
    def _get_cards_attributes(self, cards):
        shapes = [cards[0].shape.value, cards[1].shape.value, cards[2].shape.value]
        colors = [cards[0].color.value, cards[1].color.value, cards[2].color.value]
        quantities = [cards[0].quantity.value, cards[1].quantity.value, cards[2].quantity.value]
        shades = [cards[0].shade.value, cards[1].shade.value, cards[2].shade.value]

        return shapes, colors, quantities, shades


class Card(object):
    """
    Represent a card with all 4 characteristics:
    Shape, Color, Quantity and Shade.
    """

    def __init__(self, shape, color, quantity, shade):
        self.shape = Shape(shape)
        self.color = Color(color)
        self.quantity = Quantity(quantity)
        self.shade = Shade(shade)

    def __str__(self):
        return f'Shape: {self.shape} | ' \
               f'Color: {self.color} | ' \
               f'Quantity: {self.quantity} | ' \
               f'Shade: {self.shade}'

import unittest

from set import SetEvaluator, Card


class SetEvaluatorTest(unittest.TestCase):
    """Test several scenarios for the SetEvaluator"""

    def test_equal_cards_should_be_true(self):
        card1 = Card('ovals', 'red', 'two', 'solid')
        card2 = Card('ovals', 'red', 'two', 'solid')
        card3 = Card('ovals', 'red', 'two', 'solid')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_different_shapes_should_be_true(self):
        card1 = Card('squiggles', 'red', 'one', 'solid')
        card2 = Card('diamonds', 'red', 'one', 'solid')
        card3 = Card('ovals', 'red', 'one', 'solid')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_different_colors_should_be_true(self):
        card1 = Card('ovals', 'red', 'two', 'solid')
        card2 = Card('ovals', 'green', 'two', 'solid')
        card3 = Card('ovals', 'purple', 'two', 'solid')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_different_quanitites_should_be_true(self):
        card1 = Card('ovals', 'red', 'one', 'solid')
        card2 = Card('ovals', 'red', 'two', 'solid')
        card3 = Card('ovals', 'red', 'three', 'solid')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_different_shades_should_be_true(self):
        card1 = Card('ovals', 'red', 'two', 'open')
        card2 = Card('ovals', 'red', 'two', 'striped')
        card3 = Card('ovals', 'red', 'two', 'solid')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_all_different_attributes_should_be_true(self):
        card1 = Card('ovals', 'red', 'one', 'open')
        card2 = Card('diamonds', 'purple', 'two', 'striped')
        card3 = Card('squiggles', 'green', 'three', 'solid')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_wrong_shapes_should_be_false(self):
        card1 = Card('ovals', 'red', 'one', 'open')
        card2 = Card('ovals', 'purple', 'two', 'striped')
        card3 = Card('squiggles', 'green', 'three', 'solid')
        cards = [card1, card2, card3]

        self.assertFalse(SetEvaluator().is_set(cards))

    def test_wrong_colors_should_be_false(self):
        card1 = Card('ovals', 'red', 'one', 'open')
        card2 = Card('ovals', 'red', 'two', 'striped')
        card3 = Card('squiggles', 'green', 'three', 'solid')
        cards = [card1, card2, card3]

        self.assertFalse(SetEvaluator().is_set(cards))

    def test_wrong_quantities_should_be_false(self):
        card1 = Card('ovals', 'red', 'one', 'open')
        card2 = Card('ovals', 'purple', 'one', 'striped')
        card3 = Card('squiggles', 'green', 'three', 'solid')
        cards = [card1, card2, card3]

        self.assertFalse(SetEvaluator().is_set(cards))

    def test_wrong_shades_should_be_false(self):
        card1 = Card('ovals', 'red', 'one', 'open')
        card2 = Card('diamonds', 'purple', 'two', 'open')
        card3 = Card('squiggles', 'green', 'three', 'solid')
        cards = [card1, card2, card3]

        self.assertFalse(SetEvaluator().is_set(cards))

    def test_capitalized_letters_should_be_true(self):
        card1 = Card('Ovals', 'RED', 'tWo', 'soLID')
        card2 = Card('Ovals', 'RED', 'tWo', 'soLID')
        card3 = Card('Ovals', 'RED', 'tWo', 'soLID')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_spaced_attributes_should_be_true(self):
        card1 = Card(' ovals', 'red ', ' two ', 'solid')
        card2 = Card(' ovals', 'red ', ' two ', 'solid')
        card3 = Card(' ovals', 'red ', ' two ', 'solid')
        cards = [card1, card2, card3]

        self.assertTrue(SetEvaluator().is_set(cards))

    def test_find_any_combination_should_be_true(self):
        card1 = Card('ovals', 'red', 'two', 'solid')
        card2 = Card('ovals', 'green', 'two', 'solid')
        card3 = Card('ovals', 'purple', 'two', 'solid')

        card4 = Card('squiggles', 'green', 'one', 'open')
        card5 = Card('diamonds', 'red', 'two', 'solid')
        card6 = Card('ovals', 'purple', 'three', 'striped')

        cards = [card1, card2, card3, card4, card5, card6]

        self.assertTrue(SetEvaluator().is_there_any_combination(cards))

    def test_find_any_combination_should_be_false(self):
        card1 = Card('ovals', 'green', 'two', 'solid')
        card2 = Card('ovals', 'green', 'two', 'solid')
        card3 = Card('ovals', 'purple', 'two', 'solid')

        card4 = Card('squiggles', 'green', 'one', 'open')
        card5 = Card('diamonds', 'green', 'two', 'solid')
        card6 = Card('ovals', 'purple', 'three', 'striped')

        cards = [card1, card2, card3, card4, card5, card6]

        self.assertFalse(SetEvaluator().is_there_any_combination(cards))

    def test_find_the_next_possible_set(self):
        card1 = Card('ovals', 'red', 'two', 'solid')
        card2 = Card('ovals', 'green', 'two', 'solid')
        card3 = Card('ovals', 'purple', 'two', 'solid')

        card4 = Card('squiggles', 'red', 'one', 'open')
        card5 = Card('diamonds', 'green', 'two', 'solid')
        card6 = Card('ovals', 'purple', 'three', 'striped')

        cards = [card1, card2, card3, card4, card5, card6]

        # Check if all 3 cards are a Card instance
        self.assertIsInstance(SetEvaluator().find_a_set(cards)[0], Card)
        self.assertIsInstance(SetEvaluator().find_a_set(cards)[1], Card)
        self.assertIsInstance(SetEvaluator().find_a_set(cards)[2], Card)

    def test_find_the_next_possible_set_when_there_is_no_available_set(self):
        card1 = Card('ovals', 'red', 'two', 'solid')
        card2 = Card('ovals', 'red', 'two', 'solid')
        card3 = Card('ovals', 'purple', 'two', 'solid')

        card4 = Card('squiggles', 'red', 'one', 'open')
        card5 = Card('diamonds', 'red', 'two', 'solid')
        card6 = Card('ovals', 'purple', 'three', 'striped')

        cards = [card1, card2, card3, card4, card5, card6]

        self.assertFalse(SetEvaluator().find_a_set(cards))


if __name__ == '__main__':
    unittest.main()

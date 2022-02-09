from src.set import SetEvaluator, Card

if __name__ == '__main__':
    # -------------- Testing if the selected cards "is a set". --------------
    # Set for successful examples:
    card1 = Card('squiggles', 'green', 'one', 'open')
    card2 = Card('diamonds', 'red', 'two', 'solid')
    card3 = Card('ovals', 'purple', 'three', 'striped')

    # Set for failure example
    # card1 = Card('squiggles', 'red', 'one', 'solid')
    # card2 = Card('ovals', 'red', 'one', 'solid')
    # card3 = Card('ovals', 'red', 'one', 'solid')

    cards = [card1, card2, card3]

    print(f'Is it a set?\n{SetEvaluator().is_set(cards)}\n')

    # ------------- Testing if the is any combination available -------------
    # Successful example:
    card1 = Card('squiggles', 'green', 'one', 'open')
    card2 = Card('diamonds', 'red', 'two', 'solid')
    card3 = Card('ovals', 'purple', 'three', 'striped')

    # Failure example
    card4 = Card('squiggles', 'red', 'one', 'solid')
    card5 = Card('diamonds', 'red', 'one', 'solid')
    card6 = Card('ovals', 'green', 'one', 'solid')

    cards = [card1, card2, card3, card4, card5, card6]

    print(f'Is there a possible combination? \n {SetEvaluator().is_there_any_combination(cards)}\n')

    # ---------- Getting the next possible pack of cards for a set ----------
    # Successful example:
    card1 = Card('squiggles', 'green', 'one', 'open')
    card2 = Card('diamonds', 'red', 'two', 'solid')
    card3 = Card('ovals', 'purple', 'three', 'striped')

    # Failure example
    card4 = Card('squiggles', 'red', 'one', 'solid')
    card5 = Card('diamonds', 'red', 'one', 'solid')
    card6 = Card('ovals', 'green', 'one', 'solid')

    cards = [card1, card2, card3, card4, card5, card6]

    print(f'Here is the next cards that make a set:\n {SetEvaluator().find_a_set(cards)}\n')

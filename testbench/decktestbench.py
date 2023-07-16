from testbench.testbench import Testbench, Test
from deck.deck import Deck, FullDeck
##################
# Full deck test #
##################
def test1():
    full_deck = FullDeck(4)
    print(full_deck)    
    print(f"Nombre of cards: {len(full_deck.full_deck)}")
    return True

def test2():
    full_deck = FullDeck(6)
    print(full_deck)
    print(f"Nombre of cards: {len(full_deck.full_deck)}")    
    return True

def deckTestbench_main():
    deckTestbench_test1 = Test(order=1, name="Full Deck Init", desc="Test the full deck initialisation", func=test1)
    deckTestbench_test2 = Test(order=2, name="More Players", desc="Test for 6 players", func=test2)

    deckTestbench = Testbench(name = "Deck testbench", desc = "Testbench for Deck", tests = [deckTestbench_test1, deckTestbench_test2])
    print(deckTestbench)
    for test in deckTestbench.tests:
        print(test)
        test.runTest()
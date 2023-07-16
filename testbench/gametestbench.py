from testbench.testbench import Testbench, Test
from game.game import Game
##################
# Full deck test #
##################
def test1():
    try:
        full_deck = Game()
    except Exception as e:
        return e 
    return True


def gameTestbench_main():
    gameTestbench_test1 = Test(order=1, name="Full Game Init", desc="Test the game initialisation", func=test1)

    gameTestbench = Testbench(name = "Game testbench", desc = "Testbench for game", tests = [gameTestbench_test1])
    print(gameTestbench)
    for test in gameTestbench.tests:
        print(test)
        test.runTest()
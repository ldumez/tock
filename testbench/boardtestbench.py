from testbench.testbench import Testbench, Test
from board.board import Board
##################
# Full deck test #
##################
def test1():
    b = Board()
    print(b)
    return True

def test2():   
    b = Board(board_configuration_path = "configurations/boardconf2.json")
    print(b)
    return True

def boardTestbench_main():
    boardTestbench_test1 = Test(order=1, name="Board Generation", desc="Test the full deck initialisation", func=test1)
    boardTestbench_test2 = Test(order=2, name="More Players", desc="Test for 6 players", func=test2)

    boardTestbench = Testbench(name = "Board testbench", desc = "Testbench for Boards", tests = [boardTestbench_test1, boardTestbench_test2])
    print(boardTestbench)
    for test in boardTestbench.tests:
        print(test)
        test.runTest()
import pytest
from classes.Game import Game
#from classes.Brick import Brick
from  classes.BrickArray import bricks

#@pytest.mark.skip(reason="The free version of git hub does not support video device testing")
def test_game_over():
    game = Game([800, 600])
    game.ball.position = [100, 700]
    assert game.check_game_over() == True

#@pytest.mark.skip(reason="The free version of git hub does not support video device testing")
def test_game_over_blocks():
    game = Game([800, 600])
    bricks = bricks
    for bricks in bricks:
        bricks.destroy()
    assert game.check_game_over() == True

if __name__ == "__main__":
    pytest.main()
import unittest
from a2_test import A2Test
from block import random as player_random
import block
from player import *
from goal import *
SEED_NUMBER = 1214
from unittest.mock import patch


class A2TestPlayerTopLevel(A2Test):
    def setUp(self) -> None:
        player_random.seed(SEED_NUMBER)
        super().setUp()

    def tearDown(self) -> None:
        player_random.seed(SEED_NUMBER)
        super().tearDown()

    def do_action(self, block: Block, action: Tuple[str, Optional[int]],
                   target_color: Tuple[int, int, int]) -> bool:
        move_successful = False
        direction = action[1]
        if action in [ROTATE_CLOCKWISE, ROTATE_COUNTER_CLOCKWISE]:
            move_successful = block.rotate(direction)
        elif action in [SWAP_HORIZONTAL, SWAP_VERTICAL]:
            move_successful = block.swap(direction)
        elif action == SMASH:
            move_successful = block.smash()
        elif action == PAINT:
            move_successful = block.paint(target_color)
        elif action == COMBINE:
            move_successful = block.combine()
        elif action == PASS:
            move_successful = True
        return move_successful

    def test_create_player(self) -> None:
        players1 = create_players(1, 0, [i for i in range(3)])
        self.assert_player_equal(players1, 1, 0, [i for i in range(3)])
        players2 = create_players(1, 3, [])
        self.assert_player_equal(players2, 1, 3, [])
        players3 = create_players(0, 0, [i for i in range(4)])
        self.assert_player_equal(players3, 0, 0, [i for i in range(4)])

    def assert_player_equal(self, players: List[Player], num_humans: int,
                            num_random: int, smart_players: List[int]) -> None:
        for player_i in range(len(players)):
            self.assertEqual(players[player_i].id, player_i,
                             "id should start at 0 and add in sequence")
        for player in players[: num_humans]:
            self.assertTrue(isinstance(player, HumanPlayer),
                            "should start with human players")
        for player in players[num_humans: num_humans + num_random]:
            self.assertTrue(isinstance(player, RandomPlayer))
        for player in players[num_humans + num_random:
        num_random + num_humans + len(smart_players)]:
            self.assertTrue(isinstance(player, SmartPlayer))

    def test_random_player_generate_move_internal(self):
        broad = self.one_internal
        target_color = (50, 50, 50)
        goal = BlobGoal(target_color)
        rplayer1 = RandomPlayer(0, goal)
        rplayer1._proceed = True
        move = rplayer1.generate_move(broad)
        self.assertTrue(self.do_action(move[2],(move[0], move[1]), target_color),
                        "the move should be successful")

    def test_random_player_generate_move_level(self):
        broad = self.one_level
        target_color = (10, 10, 10)
        goal = BlobGoal(target_color)
        rplayer1 = RandomPlayer(0, goal)
        rplayer1._proceed = True
        move = rplayer1.generate_move(broad)
        self.assertTrue(
            self.do_action(move[2], (move[0], move[1]), target_color),
            "the move should be successful")

    @patch("block.Block.paint", return_value = False)
    def test_smart_player_do_pass(self, mock_paint):
        """
        (0, 0, (30， 30， 30))      (5, 0， (20, 20, 20))
                        ___________________________
                        |            |             |
                        |            |             |
                        |            |             |
            (0, 5, (40, 40, 40))           (5, 5, (50, 50, 50))
                        |____________|____________ |
                        |            |             |
                        |            |             |
                        |            |             |
                        |____________|_____________|
        We mock paint to return False.  You can pretend that in this case calling paint is an invalid move even though
        technically it is a valid move.  So that you have 4 valid moves that are rotating and swaping.  But none of them
        can increase the score so you have to return pass
        """
        board = self.one_level
        target_color = (10, 10, 10)
        goal = BlobGoal(target_color)
        for i in range(1, 5):
            splayer1 = SmartPlayer(0, goal, i)
            splayer1._proceed = True
            move = splayer1.generate_move(board)
            self.assertEqual('pass', move[0], "There is no better move on"
                                              " this broad")


if __name__ == "__main__":
    unittest.main(exit=False)

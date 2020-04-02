"""CSC148 Assignment 2

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, David Liu, Mario Badr, Sophia Huynh, Misha Schwartz,
and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) Diane Horton, David Liu, Mario Badr, Sophia Huynh,
Misha Schwartz, and Jaisie Sin.

=== Module Description ===

This file contains the hierarchy of player classes.
"""
from __future__ import annotations
from typing import List, Optional, Tuple
import random
import pygame

from block import Block
from goal import Goal, generate_goals

from actions import KEY_ACTION, ROTATE_CLOCKWISE, ROTATE_COUNTER_CLOCKWISE, \
    SWAP_HORIZONTAL, SWAP_VERTICAL, SMASH, PASS, PAINT, COMBINE


def create_players(num_human: int, num_random: int, smart_players: List[int]) \
        -> List[Player]:
    """Return a new list of Player objects.

    <num_human> is the number of human player, <num_random> is the number of
    random players, and <smart_players> is a list of difficulty levels for each
    SmartPlayer that is to be created.

    The list should contain <num_human> HumanPlayer objects first, then
    <num_random> RandomPlayer objects, then the same number of SmartPlayer
    objects as the length of <smart_players>. The difficulty levels in
    <smart_players> should be applied to each SmartPlayer object, in order.
    """
    all_players = []
    goals = generate_goals(num_human + num_random + len(smart_players))
    for i in range(num_human):
        all_players.append(HumanPlayer(i, goals[i]))
    for i in range(num_human, num_human + num_random):
        all_players.append(RandomPlayer(i, goals[i]))
    for i in range(num_human + num_random,
                   num_human + num_random + len(smart_players)):
        all_players.append(SmartPlayer(i, goals[i],
                                       smart_players[
                                           i - (num_human + num_random)]))
    return all_players


def _get_block(block: Block, location: Tuple[int, int], level: int) -> \
        Optional[Block]:
    """Return the Block within <block> that is at <level> and includes
    <location>. <location> is a coordinate-pair (x, y).

    A block includes all locations that are strictly inside of it, as well as
    locations on the top and left edges. A block does not include locations that
    are on the bottom or right edge.

    If a Block includes <location>, then so do its ancestors. <level> specifies
    which of these blocks to return. If <level> is greater than the level of
    the deepest block that includes <location>, then return that deepest block.

    If no Block can be found at <location>, return None.

    Preconditions:
        - 0 <= level <= max_depth
    """
    if block.position[0] <= location[0] < block.position[0] + block.size and \
            block.position[1] <= location[1] < block.position[1] + block.size \
            and block.level == level:
        return block
    elif location[0] < block.position[0] or location[0] >= block.position[0] + \
            block.size or location[1] < block.position[1] or location[1] >= \
            block.position[1] + block.size:
        return None
    elif block.children:
        for child in block.children:
            if _get_block(child, location, level) is not None:
                return _get_block(child, location, level)
    else:
        return block
    return None


class Player:
    """A player in the Blocky game.

    This is an abstract class. Only child classes should be instantiated.

    === Public Attributes ===
    id:
        This player's number.
    goal:
        This player's assigned goal for the game.
    """
    id: int
    goal: Goal

    def __init__(self, player_id: int, goal: Goal) -> None:
        """Initialize this Player.
        """
        self.goal = goal
        self.id = player_id

    def get_selected_block(self, board: Block) -> Optional[Block]:
        """Return the block that is currently selected by the player.

        If no block is selected by the player, return None.
        """
        raise NotImplementedError

    def process_event(self, event: pygame.event.Event) -> None:
        """Update this player based on the pygame event.
        """
        raise NotImplementedError

    def generate_move(self, board: Block) -> \
            Optional[Tuple[str, Optional[int], Block]]:
        """Return a potential move to make on the game board.

        The move is a tuple consisting of a string, an optional integer, and
        a block. The string indicates the move being made (i.e., rotate, swap,
        or smash). The integer indicates the direction (i.e., for rotate and
        swap). And the block indicates which block is being acted on.

        Return None if no move can be made, yet.
        """
        raise NotImplementedError


def _create_move(action: Tuple[str, Optional[int]], block: Block) -> \
        Tuple[str, Optional[int], Block]:
    return action[0], action[1], block


class HumanPlayer(Player):
    """A human player.
    """
    # === Private Attributes ===
    # _level:
    #     The level of the Block that the user selected most recently.
    # _desired_action:
    #     The most recent action that the user is attempting to do.
    #
    # == Representation Invariants concerning the private attributes ==
    #     _level >= 0
    _level: int
    _desired_action: Optional[Tuple[str, Optional[int]]]

    def __init__(self, player_id: int, goal: Goal) -> None:
        """Initialize this HumanPlayer with the given <renderer>, <player_id>
        and <goal>.
        """
        Player.__init__(self, player_id, goal)

        # This HumanPlayer has not yet selected a block, so set _level to 0
        # and _selected_block to None.
        self._level = 0
        self._desired_action = None

    def get_selected_block(self, board: Block) -> Optional[Block]:
        """Return the block that is currently selected by the player based on
        the position of the mouse on the screen and the player's desired level.

        If no block is selected by the player, return None.
        """
        mouse_pos = pygame.mouse.get_pos()
        block = _get_block(board, mouse_pos, self._level)

        return block

    def process_event(self, event: pygame.event.Event) -> None:
        """Respond to the relevant keyboard events made by the player based on
        the mapping in KEY_ACTION, as well as the W and S keys for changing
        the level.
        """
        if event.type == pygame.KEYDOWN:
            if event.key in KEY_ACTION:
                self._desired_action = KEY_ACTION[event.key]
            elif event.key == pygame.K_w:
                self._level = max(0, self._level - 1)
                self._desired_action = None
            elif event.key == pygame.K_s:
                self._level += 1
                self._desired_action = None

    def generate_move(self, board: Block) -> \
            Optional[Tuple[str, Optional[int], Block]]:
        """Return the move that the player would like to perform. The move may
        not be valid.

        Return None if the player is not currently selecting a block.
        """
        block = self.get_selected_block(board)

        if block is None or self._desired_action is None:
            return None
        else:
            move = _create_move(self._desired_action, block)

            self._desired_action = None
            return move


def _get_random_block(board: Block) -> Block:
    """Return a random block for RandomPlayer with the board given.

    This is a helper method for generate_move.
    """
    return _get_block(board, (
        random.randint(board.position[0], board.position[0] + board.size - 1),
        random.randint(board.position[0], board.position[0] + board.size - 1)),
                      random.randint(0, board.max_depth))


class RandomPlayer(Player):
    """A random player.

    It will perform a random move every time it is its turn.
    """
    # === Private Attributes ===
    # _level:
    #     The level of the Block that the user selected most recently.
    # _desired_action:
    #     The most recent action that the user is attempting to do.
    #
    # == Representation Invariants concerning the private attributes ==
    #     _level >= 0
    # === Private Attributes ===
    # _proceed:
    #   True when the player should make a move, False when the player should
    #   wait.
    _proceed: bool

    def __init__(self, player_id: int, goal: Goal) -> None:
        Player.__init__(self, player_id, goal)
        self._proceed = False

    def get_selected_block(self, board: Block) -> Optional[Block]:
        return None

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._proceed = True

    def generate_move(self, board: Block) -> \
            Optional[Tuple[str, Optional[int], Block]]:
        """Return a valid, randomly generated move.

        A valid move is a move other than PASS that can be successfully
        performed on the <board>.

        This function does not mutate <board>.
        """
        if not self._proceed:
            return None  # Do not remove
        copy_board = board.create_copy()
        select_block = _get_random_block(copy_board)
        select_swap_direction = random.choice([0, 1])
        select_rotate_direction = random.choice([1, 3])
        possible_movement = ['smash', 'swap', 'rotate', 'combine', 'paint']
        flag = False
        while not flag:
            if possible_movement:
                random_move = random.choice(possible_movement)
            else:
                select_block = _get_random_block(copy_board)
                possible_movement = ['smash', 'swap', 'rotate', 'combine',
                                     'paint']
                continue
            if random_move == 'smash':
                if select_block.smash():
                    self._proceed = False
                    return 'smash', None, _get_block(board,
                                                     select_block.position,
                                                     select_block.level)
                else:
                    possible_movement.remove('smash')
                    continue
            elif random_move == 'swap':
                if select_block.swap(select_swap_direction):
                    self._proceed = False
                    return 'swap', select_swap_direction, \
                           _get_block(board, select_block.position,
                                      select_block.level)
                else:
                    possible_movement.remove('swap')
                    continue
            elif random_move == 'rotate':
                if select_block.rotate(select_rotate_direction):
                    self._proceed = False
                    return 'rotate', select_rotate_direction, \
                           _get_block(board, select_block.position,
                                      select_block.level)
                else:
                    possible_movement.remove('rotate')
                    continue
            elif random_move == 'combine':
                if select_block.combine():
                    self._proceed = False
                    return 'combine', None, _get_block(board,
                                                       select_block.position,
                                                       select_block.level)
                else:
                    possible_movement.remove('combine')
                    continue
            elif random_move == 'paint':
                if select_block.paint(self.goal.colour):
                    self._proceed = False
                    return 'paint', None, _get_block(board,
                                                     select_block.position,
                                                     select_block.level)
                else:
                    possible_movement.remove('paint')
                    continue
        return None


class SmartPlayer(Player):
    """A smart player.

    It will give a relatively smart move when it is its turn.
    """
    # === Private Attributes ===
    # _level:
    #     The level of the Block that the user selected most recently.
    # _desired_action:
    #     The most recent action that the user is attempting to do.
    #
    # == Representation Invariants concerning the private attributes ==
    #     _level >= 0
    # === Private Attributes ===
    # _proceed:
    #   True when the player should make a move, False when the player should
    #   wait.
    # _difficulty:
    #   An integer representing what the difficult level this smart player is.
    _proceed: bool
    _difficulty: int

    def __init__(self, player_id: int, goal: Goal, difficulty: int) -> None:
        Player.__init__(self, player_id, goal)
        self._difficulty = difficulty
        self._proceed = False

    def get_selected_block(self, board: Block) -> Optional[Block]:
        return None

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._proceed = True

    def generate_move(self, board: Block) -> \
            Optional[Tuple[str, Optional[int], Block]]:
        """Return a valid move by assessing multiple valid moves and choosing
        the move that results in the highest score for this player's goal (i.e.,
        disregarding penalties).

        A valid move is a move other than PASS that can be successfully
        performed on the <board>. If no move can be found that is better than
        the current score, this player will pass.

        This function does not mutate <board>.
        """
        if not self._proceed:
            return None
        all_move = []
        all_score = []
        cur_score = self.goal.score(board)
        for _ in range(self._difficulty):
            self._helper(board, all_move, all_score, cur_score)
        all_negative = True
        for score in all_score:
            if score > 0:
                all_negative = False
        if not all_negative:
            best_index = all_score.index(max(all_score))
            self._proceed = False
            return all_move[best_index]
        else:
            self._proceed = False
            return PASS[0], PASS[1], board

    def _helper(self, board: Block,
                all_move: List[Tuple[str, Optional[int], Block]],
                all_score: List[int], cur_score: int) -> None:
        """
        It method takes the board, all_move, all_score and cur_score
        and mutate all_move and all_score and return nothing.

        A helper method for generate_move

        """
        new_copy = board.create_copy()
        select_block = _get_random_block(new_copy)
        select_swap_direction = random.choice([0, 1])
        select_rotate_direction = random.choice([1, 3])
        possible_movement = ['smash', 'swap', 'rotate', 'combine', 'paint']
        flag = False
        while not flag:
            if possible_movement:
                random_move = random.choice(possible_movement)
            else:
                select_block = _get_random_block(new_copy)
                possible_movement = ['smash', 'swap', 'rotate', 'combine',
                                     'paint']
                continue
            if random_move == 'smash':
                if select_block.smash():
                    all_score.append(self.goal.score(new_copy) - cur_score)
                    all_move.append(('smash', None,
                                     _get_block(board, select_block.position,
                                                select_block.level)))
                    flag = True
                else:
                    possible_movement.remove('smash')
                    continue
            if random_move == 'swap':
                if select_block.swap(select_swap_direction):
                    all_score.append(self.goal.score(new_copy) - cur_score)
                    all_move.append(('swap', select_swap_direction,
                                     _get_block(board,
                                                select_block.position,
                                                select_block.level)))
                    flag = True
                else:
                    possible_movement.remove('swap')
                    continue
            if random_move == 'rotate':
                if select_block.swap(select_rotate_direction):
                    all_score.append(self.goal.score(new_copy) - cur_score)
                    all_move.append(('rotate', select_rotate_direction,
                                     _get_block(board,
                                                select_block.position,
                                                select_block.level)))
                    flag = True
                else:
                    possible_movement.remove('rotate')
                    continue
            if random_move == 'combine':
                if select_block.combine():
                    all_score.append(self.goal.score(new_copy) - cur_score)
                    all_move.append(('combine', None,
                                     _get_block(board, select_block.position,
                                                select_block.level)))
                    flag = True
                else:
                    possible_movement.remove('combine')
                    continue
            if random_move == 'paint':
                if select_block.paint(self.goal.colour):
                    all_score.append(self.goal.score(new_copy) - cur_score)
                    all_move.append(('paint', None,
                                     _get_block(board, select_block.position,
                                                select_block.level)))
                    flag = True
                else:
                    possible_movement.remove('paint')
                    continue


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-io': ['process_event'],
        'allowed-import-modules': [
            'doctest', 'python_ta', 'random', 'typing', 'actions', 'block',
            'goal', 'pygame', '__future__'
        ],
        'max-attributes': 10,
        'generated-members': 'pygame.*'
    })

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
Misha Schwartz, and Jaisie Sin

=== Module Description ===

This file contains the hierarchy of Goal classes.
"""
from __future__ import annotations
import math
import random
from typing import List, Tuple
from block import Block
from settings import colour_name, COLOUR_LIST


def generate_goals(num_goals: int) -> List[Goal]:
    """Return a randomly generated list of goals with length num_goals.

    All elements of the list must be the same type of goal, but each goal
    must have a different randomly generated colour from COLOUR_LIST. No two
    goals can have the same colour.

    Precondition:
        - num_goals <= len(COLOUR_LIST)
    """
    result = []
    copy_colour_list = COLOUR_LIST[:]
    goal = random.choice(['Per', 'Blob'])
    for _ in range(num_goals):
        ran_col = random.choice(copy_colour_list)
        copy_colour_list.remove(ran_col)
        if goal == 'Per':
            result.append(PerimeterGoal(ran_col))
        else:
            result.append(BlobGoal(ran_col))
    return result


def _flatten(block: Block) -> List[List[Tuple[int, int, int]]]:
    """Return a two-dimensional list representing <block> as rows and columns of
    unit cells.

    Return a list of lists L, where,
    for 0 <= i, j < 2^{max_depth - self.level}
        - L[i] represents column i and
        - L[i][j] represents the unit cell at column i and row j.

    Each unit cell is represented by a tuple of 3 ints, which is the colour
    of the block at the cell location[i][j]

    L[0][0] represents the unit cell in the upper left corner of the Block.
    """
    full_unit = 2 ** (block.max_depth - block.level)
    res = [[-1 for _ in range(full_unit)] for _ in range(full_unit)]
    if block.children:
        _helper_flatten(block, full_unit, res)
    else:
        res = [[block.colour for _ in range(full_unit)] for _ in
               range(full_unit)]
    return res


def _helper_flatten(block: Block, full_unit: int, res: List[List[int]]) -> None:
    """ This is a helper function for _flatten. This method mutate the matrix
    <res> under multiple conditions.
    """
    top_left = _flatten(block.children[1])
    top_right = _flatten(block.children[0])
    bottom_left = _flatten(block.children[2])
    bottom_right = _flatten(block.children[3])
    half_unit = int(math.floor(full_unit / 2))
    for i in range(full_unit):
        for j in range(full_unit):
            if (i < half_unit) and (j < half_unit):
                res[i][j] = top_left[i][j]
            elif i >= half_unit > j:
                res[i][j] = top_right[i - half_unit][j]
            elif i < half_unit <= j:
                res[i][j] = bottom_left[i][j - half_unit]
            else:
                res[i][j] = bottom_right[i - half_unit][j - half_unit]


class Goal:
    """A player goal in the game of Blocky.

    This is an abstract class. Only child classes should be instantiated.

    === Attributes ===
    colour:
        The target colour for this goal, that is the colour to which
        this goal applies.
    """
    colour: Tuple[int, int, int]

    def __init__(self, target_colour: Tuple[int, int, int]) -> None:
        """Initialize this goal to have the given target colour.
        """
        self.colour = target_colour

    def score(self, board: Block) -> int:
        """Return the current score for this goal on the given board.

        The score is always greater than or equal to 0.
        """
        raise NotImplementedError

    def description(self) -> str:
        """Return a description of this goal.
        """
        raise NotImplementedError


class PerimeterGoal(Goal):
    """A player goal in the game of Blocky, which is a Perimeter Goal.

    This is a child class of Goal.

    Only unit-cell-sized portions on the perimeter count and corner cell count
    twice.
    """

    def score(self, board: Block) -> int:
        """Return the current score of the board given with the perimeter goal.
        """
        res = 0
        flattened = _flatten(board)
        for i in range(0, len(flattened)):
            if flattened[0][i] == self.colour:
                res += 1
            if flattened[i][0] == self.colour:
                res += 1
            if flattened[i][len(flattened) - 1] == self.colour:
                res += 1
            if flattened[len(flattened) - 1][i] == self.colour:
                res += 1
        return res

    def description(self) -> str:
        """Return the string representation of the current Perimeter Goal with
        the target colour.
        """
        return 'Your Goal is a Perimeter Goal, COLOUR: ' + \
               colour_name(self.colour)


class BlobGoal(Goal):
    """A player goal in the game of Blocky, which is a Blob Goal.

    This is a child class of Goal.

    It will count the largest blob of the current board with the target colour.
    """

    def score(self, board: Block) -> int:
        """Return the current score of the board given with the blob goal.
        """
        res = 0
        flattened = _flatten(board)
        lst = [[-1 for _ in range(len(flattened))] for _ in
               range(len(flattened))]
        for i in range(len(flattened)):
            for j in range(len(flattened)):
                res = max(res, self._undiscovered_blob_size((i, j), flattened,
                                                            lst))
        return res

    def _undiscovered_blob_size(self, pos: Tuple[int, int],
                                board: List[List[Tuple[int, int, int]]],
                                visited: List[List[int]]) -> int:
        """Return the size of the largest connected blob that (a) is of this
        Goal's target colour, (b) includes the cell at <pos>, and (c) involves
        only cells that have never been visited.

        If <pos> is out of bounds for <board>, return 0.

        <board> is the flattened board on which to search for the blob.
        <visited> is a parallel structure that, in each cell, contains:
            -1 if this cell has never been visited
            0  if this cell has been visited and discovered
               not to be of the target colour
            1  if this cell has been visited and discovered
               to be of the target colour

        Update <visited> so that all cells that are visited are marked with
        either 0 or 1.
        """
        target_colour = self.colour
        if pos[0] >= len(board) or pos[0] < 0 or pos[1] >= len(board) or \
                pos[1] < 0:
            return 0
        elif board[pos[0]][pos[1]] != target_colour:
            visited[pos[0]][pos[1]] = 0
            return 0
        else:
            size = 1
            visited[pos[0]][pos[1]] = 1
            right_pos = (pos[0] + 1, pos[1])
            left_pos = (pos[0] - 1, pos[1])
            up_pos = (pos[0], pos[1] + 1)
            down_pos = (pos[0], pos[1] - 1)
            if pos[0] + 1 < len(board) and visited[pos[0] + 1][pos[1]] == -1:
                size += self._undiscovered_blob_size(right_pos, board, visited)
            if pos[0] - 1 >= 0 and visited[pos[0] - 1][pos[1]] == -1:
                size += self._undiscovered_blob_size(left_pos, board, visited)
            if pos[1] + 1 < len(board) and visited[pos[0]][pos[1] + 1] == -1:
                size += self._undiscovered_blob_size(up_pos, board, visited)
            if pos[1] - 1 >= 0 and visited[pos[0]][pos[1] - 1] == -1:
                size += self._undiscovered_blob_size(down_pos, board, visited)

            return size

    def description(self) -> str:
        """Return the string representation of the current Perimeter Goal with
        the target colour.
        """
        return 'Your Goal is a Blob Goal, COLOUR: ' + colour_name(self.colour)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-import-modules': [
            'doctest', 'python_ta', 'random', 'typing', 'block', 'settings',
            'math', '__future__'
        ],
        'max-attributes': 15
    })

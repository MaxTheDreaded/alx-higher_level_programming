#!/usr/bin/python3
"""
Module 101-nqueens
"""


import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == col - i:
            return False
    return True


def solve_nqueens_util(board, col, N, solutions, current_solution):
    if col == N:
        solutions.append(list(current_solution))
        return
    for i in range(N):
        if is_safe(current_solution, i, col, N):
            current_solution.append(i)
            solve_nqueens_util(board, col + 1, N, solutions, current_solution)
            current_solution.pop()


def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve_nqueens_util([], 0, N, solutions, [])
    for solution in solutions:
        for row in solution:
            print([i, row] for i in range(N))
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])

from typing import List

class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.blank_position = self.find_blank()

    def find_blank(self):
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[0])):
                if self.puzzle[row][col] == 0:
                    return (row, col)

    def is_goal(self, goal_state):
        return self.puzzle == goal_state

    def generate_neighbors(self):
        neighbors = []
        row, col = self.blank_position
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < len(self.puzzle) and 0 <= new_col < len(self.puzzle[0]):
                new_puzzle = [list(row) for row in self.puzzle]
                new_puzzle[row][col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[row][col]
                neighbors.append(PuzzleState(new_puzzle))

        return neighbors

def manhattan_distance(tile_value, current_position, goal_position):
    if tile_value == 0:
        return 0  # Manhattan distance for the blank tile is 0

    row1, col1 = current_position
    row2, col2 = goal_position
    return abs(row1 - row2) + abs(col1 - col2)

def heuristic_manhattan(current_state, goal_state):
    total_distance = 0

    for row in range(len(current_state.puzzle)):
        for col in range(len(current_state.puzzle[0])):
            tile_value = current_state.puzzle[row][col]
            if tile_value != goal_state.puzzle[row][col]:
                goal_position = goal_state.find_blank() if tile_value == 0 else ((tile_value - 1) // len(current_state.puzzle[0]), (tile_value - 1) % len(current_state.puzzle[0]))
                total_distance += manhattan_distance(tile_value, (row, col), goal_position)

    return total_distance

def dfs_solver(initial_state, goal_state):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()
        visited.add(tuple(map(tuple, current_state.puzzle)))

        if current_state.is_goal(goal_state):
            return current_state

        neighbors = current_state.generate_neighbors()
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor.puzzle)) not in visited:
                stack.append(neighbor)

    return None

def depth_search(puzzle: List[List[int]]):
    initial_state = PuzzleState(puzzle)

    goal_puzzle = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    goal_state = PuzzleState(goal_puzzle)

    solution = dfs_solver(initial_state, goal_state)

    if solution:
        print("Solution found:")
        for row in solution.puzzle:
            print(row)
    else:
        print("No solution found.")

    # Calculate and print the Manhattan distance heuristic
    heuristic_value = heuristic_manhattan(initial_state, goal_state)
    print("Manhattan Distance Heuristic:", heuristic_value)

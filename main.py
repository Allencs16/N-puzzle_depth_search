from typing import List

import algoritmos

if __name__ == '__main__':
    print('TDE2 IA N-Puzzle')

    puzzle: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

    algoritmos.depth_search(puzzle)

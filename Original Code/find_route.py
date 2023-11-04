from collections import deque
import sys

def find_route(current_location, final_location):
    """Finds the route from the current location to the final location.

    Args:
        current_location: A tuple of (row, col) representing the current location.
        final_location: A tuple of (row, col) representing the final location.

    Returns:
        A list of directions, where each direction is a string representing one of
        the following characters: '^', 'v', '<', or '>'.
    """

    movements = [(0, 1, '>'), (0, -1, '<'), (1, 0, 'v'), (-1, 0, '^')]
    # 7 x 7 City Grid
    city_grid = [
        # [0, 1, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0, 0],
        # [0, 1, 0, 1, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 0, 0, 1, 0, 0],
        # [0, 0, 0, 0, 1, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0]

        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    rows, cols = len(city_grid), len(city_grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = {}

    current_row, current_col = current_location
    final_row, final_col = final_location

    if (0 <= current_row < rows and 0 <= current_col < cols and
        0 <= final_row < rows and 0 <= final_col < cols and
        city_grid[current_row][current_col] == 0 and
        city_grid[final_row][final_col] == 0):

        queue = deque([(current_row, current_col)])
        visited[current_row][current_col] = True

        while queue:
            row, col = queue.popleft()

            if (row, col) == (final_row, final_col):
                break

            for dr, dc, direction in movements:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < rows and 0 <= new_col < cols and
                    city_grid[new_row][new_col] == 0 and
                    not visited[new_row][new_col]):
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = True
                    parent[(new_row, new_col)] = (row, col)

        path = []
        current = (final_row, final_col)
        while current != (current_row, current_col):
            path.append(current)
            current = parent[current]
        path.append((current_row, current_col))
        path.reverse()

        directions = []
        for i in range(1, len(path)):
            row, col = path[i]
            prev_row, prev_col = path[i - 1]

            direction = None
            for dr, dc, dir in movements:
                if (row - prev_row == dr and col - prev_col == dc):
                    direction = dir
                    break

            directions.append(direction)

        return directions

    else:
        return None

if __name__ == '__main__':
    current_location = tuple(map(int, sys.argv[1].split(',')) if len(sys.argv) > 1 else (1, 1))
    final_location = tuple(map(int, sys.argv[2].split(',')) if len(sys.argv) > 2 else (6, 6))

    directions = find_route(current_location, final_location)

    if directions:
        print("".join(directions))
    else:
        print("None")

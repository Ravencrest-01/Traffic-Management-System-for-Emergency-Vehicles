from collections import deque

def print_arrows(path, movements):
    arrow_symbols = {'^': (1, 0), 'v': (-1, 0), '>': (0, 1), '<': (0, -1)}
    for i in range(1, len(path)):
        row, col = path[i]
        prev_row, prev_col = path[i - 1]
        direction = None
        for dir, (dr, dc) in arrow_symbols.items():
            if (row - prev_row == dr and col - prev_col == dc):
                direction = dir
                break
        print(direction, end=' ')

def find_route(current_location, final_location):
    movements = [(0, 1, '>'), (0, -1, '<'), (1, 0, 'v'), (-1, 0, '^')]

    city_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0]
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

        print("Starting from", (current_row, current_col))
        print("Going to", (final_location))
        print("Directions:")
        print_arrows(path, movements)
        print("\nDestination reached")

    else:
        print("Invalid current or final location.")

# Example usage:
current_location = (0, 0)
final_location = (4, 4)
find_route(current_location, final_location)

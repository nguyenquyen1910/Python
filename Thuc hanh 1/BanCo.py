from collections import deque

def get_empty_position(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return (i, j)
    return None

def get_neighbors(state, empty_pos):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
    neighbors = []
    empty_x, empty_y = empty_pos

    for dx, dy in directions:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 4 and 0 <= new_y < 4:
            # Create a new state by swapping the empty space with the adjacent one
            new_state = [row[:] for row in state]  # Deep copy of the state
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            neighbors.append(((new_x, new_y), new_state))
    return neighbors

def bfs(start, target):
    queue = deque([(start, get_empty_position(start), [])])
    visited = set()
    visited.add(tuple(map(tuple, start)))  # Store the state as a tuple of tuples for immutability

    while queue:
        current_state, empty_pos, path = queue.popleft()

        if current_state == target:
            return path

        for new_empty_pos, new_state in get_neighbors(current_state, empty_pos):
            state_tuple = tuple(map(tuple, new_state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                # Record the move
                move = (empty_pos[0] + 1, empty_pos[1] + 1, new_empty_pos[0] + 1, new_empty_pos[1] + 1)  # Convert to 1-based
                queue.append((new_state, new_empty_pos, path + [move]))

    return []

def main():
    start = [list(map(int, input().strip())) for _ in range(4)]
    target = [list(map(int, input().strip())) for _ in range(4)]
    
    move_path = bfs(start, target)
    print(len(move_path))
    for move in move_path:
        print(" ".join(map(str, move)))

if __name__ == "__main__":
    main()

#BREADTH FIRST SEARCH (BFS) for Queue, FIFO. Level-by-level traversal
#NOTE: for Stack: Depth First Search (DFS) Goes deep before backtracking, LIFO
'''BFS is a graph traversal algorithm used to explore nodes level by level. 
It is commonly used for finding the shortest path'''
#QUEUE IMPLEMENTATION
'''The knight moves in L-shapes (8 possible moves).
Use a queue to explore moves level by level from initial position (sx,sy).
Track visited positions using a set to avoid cycles.
If the knight reaches target at (tx, ty), return True.
Edge Case:
If (sx, sy) == (tx, ty), return True.'''

from collections import deque

def is_knight_reachable(m, n, sx, sy, tx, ty):
    """Returns True if the knight can reach (tx, ty) from (sx, sy) in an m x n grid."""
    
    # Possible moves for a knight (dx, dy)
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # BFS queue: (current_x, current_y)
    queue = deque([(sx, sy)])
    visited = set([(sx, sy)])  # Track visited positions

    while queue:
        x, y = queue.popleft()
        
        # If reached target
        if (x, y) == (tx, ty):
            return True

        # Explore all possible knight moves
        for dx, dy in moves:
            nx, ny = x + dx, y + dy  # New position
            
            # Check if within grid bounds and not visited
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))  # Mark as visited
                
    return False  # If BFS completes without reaching target

# m, n = 8, 8  # Chessboard size
# sx, sy = 0, 0  # Starting position
# tx, ty = 7, 7  # Target position

print("Select Chessboard size: ")
m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))
print("Set starting position of the Knight: ")
sx=int(input("Enter x cordinate: "))
sy=int(input("Enter y cordinate: "))
print("Set target's position: ")
tx=int(input("Enter x cordinate: "))
ty=int(input("Enter y cordinate: "))

print(is_knight_reachable(m, n, sx, sy, tx, ty))  

'''Sample Case
TRUE: m=8, n=4, sx=2, sy=1, tx=7, ty=3
FALSE: m=8, n=4, sx=2, sy=1, tx=1, ty=4'''
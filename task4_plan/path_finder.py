import sys
from collections import deque
from typing import List, Tuple, Optional

def read_map(file_path: str) -> List[List[int]]:
    try:
        with open(file_path, 'r') as f:
            map_data = []
            for line in f:
                row = [int(x) for x in line.strip().split()]
                map_data.append(row)
            return map_data
    except FileNotFoundError:
        print(f"错误：地图文件 '{file_path}' 未找到。")
        sys.exit(1)
    except Exception as e:
        print(f"读取地图文件时发生错误：{e}")
        sys.exit(1)

def is_valid(map_data: List[List[int]], x: int, y: int) -> bool:

    return (0 <= x < len(map_data) and 
            0 <= y < len(map_data[0]) and 
            map_data[x][y] == 0)

def bfs_find_path(map_data: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    if not is_valid(map_data, start[0], start[1]):
        return None
    
    if not is_valid(map_data, goal[0], goal[1]):
        return None
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    queue = deque([start])
    visited = {start: None} 
    
    while queue:
        current = queue.popleft()

        if current == goal:
 
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1] 
        
        for dx, dy in directions:
            next_x, next_y = current[0] + dx, current[1] + dy
            
            if is_valid(map_data, next_x, next_y) and (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                visited[(next_x, next_y)] = current
    
    return None

def print_map_with_path(map_data: List[List[int]], path: List[Tuple[int, int]]):

    path_set = set(path) if path else set()
    
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if (i, j) in path_set:
                print('*', end=' ')
            else:
                print(map_data[i][j], end=' ')
        print()

def main():

    if len(sys.argv) != 6:
        print("用法: python path_finder.py <map_file> <start_x> <start_y> <goal_x> <goal_y>")
        print("示例: python path_finder.py map.txt 0 0 4 4")
        sys.exit(1)
    
    try:

        map_file = sys.argv[1]
        start_x, start_y = int(sys.argv[2]), int(sys.argv[3])
        goal_x, goal_y = int(sys.argv[4]), int(sys.argv[5])
        
        start = (start_x, start_y)
        goal = (goal_x, goal_y)
        

        map_data = read_map(map_file)
        

        if not (0 <= start_x < len(map_data) and 0 <= start_y < len(map_data[0])):
            print(f"错误：起点坐标 ({start_x}, {start_y}) 超出地图范围。")
            sys.exit(1)
        
        if not (0 <= goal_x < len(map_data) and 0 <= goal_y < len(map_data[0])):
            print(f"错误：终点坐标 ({goal_x}, {goal_y}) 超出地图范围。")
            sys.exit(1)
        
        path = bfs_find_path(map_data, start, goal)
        
        if path:
            print("找到路径！")
            print_map_with_path(map_data, path)
            print(f"\n路径长度: {len(path) - 1} 步")
            print("路径坐标:", " -> ".join(f"({x},{y})" for x, y in path))
        else:
            print(f"I can't go to the postion ({goal_x},{goal_y}).")
            
    except ValueError:
        print("错误：坐标参数必须是整数。")
        sys.exit(1)
    except Exception as e:
        print(f"程序执行时发生错误：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
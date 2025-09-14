# 机器人路径规划程序

## 功能
使用BFS算法在二维网格地图中寻找从起点到终点的最短路径，0代表可通行区域，1代表障碍物。

## 文件结构
```
.
├── path_finder.py    # 主程序
├── map.txt          # 测试地图文件
└── README.md        # 说明文档
```

## 使用方法

### 基本用法
```bash
python path_finder.py <map_file> <start_x> <start_y> <goal_x> <goal_y>
```

示例：
```bash
python path_finder.py map.txt 0 0 4 4
```

### 参数说明
- `<map_file>`: 地图文件路径
- `<start_x> <start_y>`: 起点坐标（行，列）
- `<goal_x> <goal_y>`: 终点坐标（行，列）

**注意**：坐标从0开始，左上角为(0,0)

### 运行测试

```bash
python path_finder.py map.txt 0 0 4 4
```

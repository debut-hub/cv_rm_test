# 机器人视觉任务解决方案

本项目包含两个机器人视觉任务：敌方机器人颜色识别和能量机关定位。

## 项目结构
```
VisionTasks/
├── color_detector.py    # 任务一：颜色识别程序
├── rune_locator.py      # 任务二：能量机关定位程序
├── test_red_armor.jpg   # 任务一测试图片
├── test_rune.png        # 任务二测试图片
└── README.md            # 说明文档
```

## 环境要求
- Python 3.x
- OpenCV 库: `pip install opencv-python`
- NumPy 库: `pip install numpy`

---

## 任务一：识别敌方机器人颜色

### 功能描述
使用OpenCV和HSV色彩空间识别图像中的红色区域，生成二值化掩码。

### 使用方法
```bash
python color_detector.py <图片路径>
```

### 示例命令
```bash
python color_detector.py test_red_armor.jpg
```


### 预期输出
显示两个窗口：
1. **Original Image**: 原始输入图像
2. **Red Mask**: 二值化掩码，白色区域表示检测到的红色区域

---

## 任务二：定位能量机关（ROI与形状检测）

### 功能描述
通过轮廓分析和几何特征检测，定位图像中的圆形能量机关并用矩形框标记。

### 使用方法
```bash
python rune_locator.py <图片路径>
```

### 示例命令
```bash
python rune_locator.py test_rune.png
```

### 手动验证

```bash
# 任务一验证
python color_detector.py test_red_armor.jpg

# 任务二验证
python rune_locator.py test_rune.png
```

import cv2
import numpy as np
import sys

def detect_circle(image_path):
    # 加载图片
    image = cv2.imread(image_path)
    if image is None:
        print(f"无法加载图片: {image_path}")
        return
    
    # 灰度化处理
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 高斯模糊减少噪声
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny 边缘检测
    edges = cv2.Canny(blurred, 50, 150)  # 可根据实际情况调整阈值
    
    # 寻找所有轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    best_circle = None
    best_circularity = 0
    
    # 筛选圆形轮廓
    for contour in contours:
        # 计算轮廓面积
        area = cv2.contourArea(contour)
        if area < 100:  # 过滤过小的轮廓
            continue
        
        # 计算轮廓周长
        perimeter = cv2.arcLength(contour, True)
        if perimeter == 0:  # 避免除零错误
            continue
        
        # 计算圆度 (圆的圆度接近1)
        circularity = 4 * np.pi * area / (perimeter * perimeter)
        
        # 寻找圆度最高的轮廓
        if circularity > best_circularity and circularity > 0.7:
            best_circularity = circularity
            best_circle = contour
    
    # 标记找到的圆形
    if best_circle is not None:
        x, y, w, h = cv2.boundingRect(best_circle)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("找到圆形轮廓并标记")
    else:
        print("未找到符合条件的圆形轮廓")
    
    # 显示 Canny 边缘检测结果和标记后的原图
    cv2.imshow('Canny Edges', edges)
    cv2.imshow('Circle Detection Result', image)
    cv2.waitKey(0)  # 等待用户按键
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python circle_detector.py <图片路径>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    detect_circle(image_path)
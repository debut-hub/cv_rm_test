import cv2
import numpy as np
import sys
import argparse

def detect_red_color(image_path):
    """
    检测图像中的红色区域
    
    Args:
        image_path (str): 图像文件路径
        
    Returns:
        tuple: (原始图像, 红色掩码图像)
    """
    # 读取图像
    try:
        original_image = cv2.imread(image_path)
        if original_image is None:
            raise ValueError("无法读取图像文件，请检查路径是否正确")
    except Exception as e:
        print(f"错误：读取图像时发生错误 - {e}")
        sys.exit(1)
    
    # 将图像从BGR转换到HSV色彩空间
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    
    # 定义红色的HSV阈值范围
    # 红色在HSV中有两个范围（因为红色在色相环的两端）
    
    # 红色范围1 (0-10)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    
    # 红色范围2 (160-180)
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    # 创建两个红色区域的掩码
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    
    # 合并两个掩码
    red_mask = cv2.bitwise_or(mask1, mask2)
    
    # 可选：进行形态学操作来去除噪声和填充空洞
    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    
    return original_image, red_mask

def display_results(original_image, red_mask):
    """
    显示原始图像和红色掩码
    
    Args:
        original_image: 原始BGR图像
        red_mask: 红色区域的二值化掩码
    """
    # 创建显示窗口
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Red Mask', cv2.WINDOW_NORMAL)
    
    # 调整窗口大小
    cv2.resizeWindow('Original Image', 800, 600)
    cv2.resizeWindow('Red Mask', 800, 600)
    
    # 显示图像
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Red Mask', red_mask)
    
    print("按任意键关闭窗口...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='识别图像中的红色区域')
    parser.add_argument('image_path', help='输入图像的路径')
    parser.add_argument('--save', '-s', action='store_true', 
                       help='保存处理结果到文件')
    
    # 解析参数
    args = parser.parse_args()
    
    # 检测红色区域
    original_image, red_mask = detect_red_color(args.image_path)
    
    # 显示结果
    display_results(original_image, red_mask)
    
    # 如果需要保存结果
    if args.save:
        cv2.imwrite('original_image.jpg', original_image)
        cv2.imwrite('red_mask.jpg', red_mask)
        print("结果已保存为 'original_image.jpg' 和 'red_mask.jpg'")

if __name__ == "__main__":
    main()
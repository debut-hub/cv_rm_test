import json
import sys
import argparse

def load_config(config_path):
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"错误：无法加载配置文件 '{config_path}' - {e}")
        sys.exit(1)
        
def print_formatted_config(config_data):

    print("=== 机器人状态配置 ===")
    print(f"机器人名称: {config_data.get('robot_name', '未设置')}")
    print(f"生命值: {config_data.get('health', 0)}")
    print(f"弹药量: {config_data.get('ammo', 0)}")
    

    modules = config_data.get('enabled_modules', [])
    if modules:
        print(f"启用模块: {', '.join(modules)}")
    else:
        print("启用模块: 无")

def main():
    parser = argparse.ArgumentParser(description='读取并打印机器人配置JSON文件')
    parser.add_argument('config_path', help='JSON配置文件的路径')
    
    args = parser.parse_args()
    
    config_data = load_config(args.config_path)
    
    print_formatted_config(config_data)

if __name__ == "__main__":
    main()
# 这是打印文件

def print_file():
    """读取并打印当前文件内容"""
    try:
        with open('test.py', 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)  # 修复：将 printf 改为 print
    except FileNotFoundError:
        print("错误：文件 test.py 不存在")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

def main():
    """主函数"""
    print("开始执行程序...")
    print_file()
    print("程序执行完成！")

if __name__ == "__main__":
    main()
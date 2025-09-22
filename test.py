# 这是打印文件

def print_file():
    with open('test.py', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

def main():
    print_file()
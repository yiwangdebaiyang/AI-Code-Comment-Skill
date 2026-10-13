"""
AI Code Comment Skill

功能：
输入代码文件
自动生成代码解释和注释
"""


def analyze_code(code):

    print("====== Code Analysis ======")

    print("\n代码内容：")
    print(code)

    print("\n代码功能分析：")

    if "def" in code:
        print("- 检测到函数定义")
        print("- 该代码包含函数结构")

    if "for" in code:
        print("- 检测到循环结构")
        print("- 程序可能进行数据遍历")

    print("\n优化建议：")
    print("- 增加函数注释")
    print("- 增加变量说明")
    print("- 提高代码可读性")



if __name__ == "__main__":


    example = """

def add(a,b):
    return a+b

"""


    analyze_code(example)

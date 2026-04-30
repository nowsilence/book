```python

class MyDataFrame:
    def __init__(self, data, age):
        self.data = data  # 存数据
        self.age = age

    # 支持 obj [key]
    def __getitem__(self, key):
        print("你传入的 key =", key, "类型 =", type(key))

        # 如果 key 是列表 → 返回多列
        if isinstance(key, list):
            result = {}
            for col in key:
                result[col] = self.data[col]
            return result

        # 如果 key 是字符串 → 返回单列
        else:
            return self.data[key]

    # 支持 obj [key] = xxx
    def __setitem__(self, key, value):
        self.data[key] = value

    # 让对象能像函数一样调用 obj(5)
    def __call__(self, x):
        return x * 2

    # 重写+操作符号
    def __add__(self, other):
        return self.age + other.age

    # 重写== 操作符号
    def __eq__(self, other):
        return self.id == other.id

    # 重写 < 操作符号
    def __lt__(self, other):
        return self.age < other.age
    
    # 迭代符号 使对象支持for
    def __iter__(self):
        yield from self.data

if __name__ == "__main__":

    # 只有直接运行文件时才执行
    print("我被直接运行了")
    # 魔法变量

    # 直接运行文件 __name__为__main__
    print("__name__")
    # 当前文件的绝对路径
    print(__file__)
    # 文档注释
    print(__doc__)
    # 当前文件所属的包名
    print(__package__)
    # 类型注解信息
    print(__annotations__)
            # 构造数据
    data = {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9]
    }

    df = MyDataFrame(data, 1)

    # ✅ 现在你可以这样用！
    print("\n取单列：")
    print(df["A"])

    print("\n取多列（关键！）：")
    print(df[["B", "A"]])  # 🔥 这里 [] 里是 list！
```
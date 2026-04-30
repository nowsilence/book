```python
def add(a, b):
    return a + b

def info(name, age):
    print(name, age)

def say_hello(name, msg="你好"):
    print(name, msg)

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    print(kwargs)

def func(a, b, c):
    print(a, b, c)


# 按位置传：a=1, b=2
print(add(1, 2))  # 3

# 关键字传参，顺序无关
info(age=20, name="小明")

# 默认参数
say_hello("小红")          # 使用默认 msg
say_hello("小刚", "早上好") # 覆盖默认值

# 可变参数（打包成元组）
print(sum_all(1,2,3,4))

# 可变参数（打包成字典）
print_info(name="张三", age=25, city="北京")

# 列表解包
lst = [1,2,3]
func(*lst)  # 等价 func(1,2,3)

# 字典解包
dic = {"a":10, "b":20, "c":30}
func(**dic) # 等价 func(a=10,b=20,c=30)
```
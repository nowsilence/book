lst = [1, 2, 3]

# 切片 lst[start : end : step]

# 索引
# 切片：lst[1:3]、lst[::2] 都由 __getitem__ 支持
# 切片语法 [start:stop:step] 会被 Python 解释器自动封装成一个 slice 对象
'''
slice 对象结构
slice(start, stop, step) 就是存 3 个值的简单对象：
start：起始索引（默认 None → 0）
stop：结束索引（默认 None → 列表长度）
step：步长（默认 None → 1）
'''
lst[0]        # lst.__getitem__()
lst[0] = 99   # lst.__setitem__()
del lst[1]    # lst.__delitem__()

# 长度 / 包含
len(lst)      # lst.__len__()
2 in lst      # lst.__contains__()

bool(lst)     # list.__bool__()（空列表为 False）

# 运算
[1]+[2]       # __add__ [1, 2]
lst*3         # __mul__ [1, 2, 3, 1, 2, 3, 1, 2, 3] 三倍
lst += [4]    # __iadd__ [1, 2, 3, 4]

# 比较操作符，按元素顺序逐位比较，最短长度逐一对比
'''
== → __eq__
!= → __ne__
<  → __lt__
<= → __le__
>  → __gt__
>= → __ge__
'''
[1,2] < [1,3] # __lt__
[1] == [1]    # __eq__



'''
[1,2,3]  < [1,2,4]   # True  第三位 3<4
[1,5]    < [1,2,3]   # False 第二位5>2
[1,2]    < [1,2,3]   # True  前缀相同，短更小
[1,2,3]  < [1,2]     # False
[]       < [1]       # True
'''
def __lt__(self, other):
    # 遍历最短长度内的所有元素
    for x, y in zip(self, other):
        if x != y:
            return x < y
    # 前面全都一样，比长度
    return len(self) < len(other)

'''
zip 内置函数 返回迭代器对象 把多个列表「一一配对、打包捆绑」在一起
a = [1,2,3]
b = ['x','y','z']
zip(a,b)
list(zip(a,b))
'''

def tts(n):
    print(n)

tts(it) for it in lis
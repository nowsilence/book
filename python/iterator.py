# 迭代器三种创建方式

# 1 用yield→自动变成迭代器（最简单）

def fn(lst):
    for i in lst:
        yield i

# 2. 手动返回迭代器对象
def fn1(lst):
    return iter(lst)

# 3. 类手动实现原生迭代器协议 __iter__ + __next__

'''
myIter = MyIter()
for i in myIter:
    print(i)

# Python 发现 in myIter
# 自动执行 → my.__iter__()
# 返回 self（迭代器本身）
# 直调用 __next__() 取值
'''
class MyIter:
    def __init__(self):
        # 类里面保存一个列表
        self.lst = [1, 2, 3]
        # 游标，记录当前走到第几个
        self.index = 0

    # 返回迭代器对象（自己）
    def __iter__(self):
        return self

    # 返回下一个元素值
    def __next__(self):
        # 没元素了就终止迭代
        if self.index >= len(self.lst):
            raise StopIteration
        
        # 取出当前元素
        value = self.lst[self.index]
        # 游标往后移动
        self.index += 1

        return value
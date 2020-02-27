# 斐波那契(fibonacci)数列模块

if __name__ == '__main__':
   print('在mypkg包里的主程序')
else:
   print('在mypkg包里的另一模块')

def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

fib(100)
# 競技プログラミングで使う、標準入力のチートシート

# 文字列
# abc
S = input().strip()

# 整数
# 123
N = int(input().strip())

# 浮動小数点数
# 1.23
L = float(input().strip())


# 2つの文字列
# Hello World
S1, S2 = input().strip().split(' ')

# 複数の文字列
# Hello World python 
array = input().strip().split(' ')

# 複数の整数を配列として扱う
# 1 2 3 4 5 
array = list(map(int, input().strip().split(' ')))

# ２つの数値
# 12 34 
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]

# 行数
N = int(input().strip())

# 2次元配列
grid = []
for i in range(N):
    array = list(map(int, input().strip().split(' ')))
    grid.append(array)

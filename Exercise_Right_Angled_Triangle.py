# 设置三角形的总行数（图中为 10 行）
rows = 10

# 外层循环：控制行数（1 到 10 行）
for i in range(1, rows + 1):
    # 内层循环：控制每行打印的星号数量（第 i 行打印 i 个星号）
    for j in range(1, i + 1):
        print("*", end=" ")  # end=" " 保证星号同行打印且用空格隔开
    print()  # 换行
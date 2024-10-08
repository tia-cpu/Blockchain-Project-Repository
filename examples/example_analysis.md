# Example Analysis

# 导入 Matplotlib 库
import matplotlib.pyplot as plt

# 创建数据
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 15, 10]

# 创建图表
plt.plot(x, y, marker='o', linestyle='-', color='b', label='数据线')

# 添加标题和标签
plt.title('简单折线图')
plt.xlabel('X 轴')
plt.ylabel('Y 轴')

# 显示图例
plt.legend()

# 显示图表
plt.show()




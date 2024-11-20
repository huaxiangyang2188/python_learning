import matplotlib.pyplot as plt
from random_walk import RandomwWalk
# 只要程序处于运行的状态，不断模拟漫步随机
while True:
# 创建 RandomWalk 实例，并绘制出点图
    rw = RandomwWalk(5000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,linewidth=5)
    
    plt.show()
    
    
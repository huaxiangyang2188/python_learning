import matplotlib.pyplot as plt
x_values = list(range(1, 5001))
y_vaules = [x**3 for x in x_values]
plt.scatter(x_values,y_vaules,c=y_vaules,cmap=plt.cm.Reds,
            edgecolor='none',s=40)
# 设置图表标题和给坐标加上标签
plt.title('Cube Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Cube',fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0,5000,0,130000000000])
plt.show()
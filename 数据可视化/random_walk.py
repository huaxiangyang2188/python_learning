from random import choice
class RandomwWalk:
    """生成随机漫步的类"""
    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]
    def get_step(self):
        """确定每次漫步的方向及距离"""
        direction = choice([1, -1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = direction * distance
        return step

    def fill_walk(self):
        """计算随机漫步的点并绘制其图形"""
        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿着这个方向前进的距离
            
            x_step = self.get_step()
            
            y_step  = self.get_step()
            # 拒绝原地踏步
            if x_step ==0 and y_step==0:
                continue
            # 计算下一个点的x和y坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


      


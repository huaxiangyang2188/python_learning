from random import randint
class Die:
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        """初始化骰子属性"""
        self.num_sides = num_sides
    def roll(self):
        """随机输出一个1到骰子面数之间的整数"""
        return randint(1,self.num_sides)
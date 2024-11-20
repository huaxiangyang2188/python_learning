class Restaurant():
    """一次餐厅的简单描述，包括餐厅的名称和菜系类型"""
    def __init__(self, name, cuisine_type):
        """初始化餐厅的名称和菜系类型"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """打印餐厅的描述信息"""
        print("\nThis restaurant is called " + self.name.title() + " .")
        print("It's a " + self.cuisine_type.title() + " restaurant.")
    def open_restaurant(self):
        """餐厅营业中"""
        print("The restaurant is now opening!")
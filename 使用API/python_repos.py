import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:",r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])
# 探索有关仓库的情况
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))
# 研究第一个仓库
repo_dict = repo_dicts[0]
names, plot_dicts = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink':repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
# 创建柱状图
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()  #建立实例
my_config.x_label_rotation = 45
my_config.show_legend = False  #上面两个是实例的属性
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18  #确定标签字体大小
my_config.truncate_label = 15   #截断标签，约束为15个字符。
my_config.shouw_y_guides = False  #隐藏y轴水平线
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)  #通过实参传递配置实例，从而如果调整配置
                                                 #通过my_config就能改变图表

chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
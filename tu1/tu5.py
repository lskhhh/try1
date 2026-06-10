import matplotlib.pyplot as plt

# 修复中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据（论文统一数据）
labels = ["18-25岁", "26-35岁", "36-45岁", "45岁以上"]
size = [45, 32, 15, 8]

# 严格黑白配色（无彩色，灰度渐变）
colors = ['#222222', '#555555', '#888888', '#bbbbbb']

plt.figure(figsize=(9, 9), dpi=150)
# 环形图（中间空心）
plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%',
        wedgeprops={'width': 0.5, 'edgecolor': 'white'},
        startangle=90, textprops={'fontsize': 12})

plt.title("传统文化内容受众年龄分布", fontsize=15, pad=20)

# 导出矢量图
plt.savefig("图5_受众年龄分布环形图.svg", format="svg", bbox_inches="tight")
plt.close()

print("✅ 图5黑白矢量图生成完成！文件：图5_受众年龄分布环形图.svg")
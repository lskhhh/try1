import matplotlib.pyplot as plt

# 修复中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ["非遗民俗", "传统饮食", "古风音乐", "传统艺术", "古典文学哲学"]
sizes = [32, 25, 21, 14, 8]

# ===================== 1. 设置黑白/灰度配色 =====================
# 使用从深到浅的灰色，确保打印出来的区分度
colors = ['#4D4D4D', '#737373', '#999999', '#BFBFBF', '#E6E6E6']

plt.figure(figsize=(9, 9), dpi=150)

# ===================== 2. 绘图设置 =====================
# 💡 关键修改：添加 wedgeprops={'edgecolor': 'black', 'linewidth': 1} 增加黑边框
# 这样即使灰色比较接近，扇区之间也有明确的分界线
plt.pie(sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=120,
        textprops={'fontsize': 12, 'color': 'black'},
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.title("传统文化内容类型占比分布图", fontsize=15, pad=20)

# ===================== 3. 导出SVG矢量图 =====================
plt.savefig("图4_内容类型占比饼图_黑白版.svg", format="svg", bbox_inches="tight")
plt.close()

print("✅ 图4黑白矢量图生成完成！文件：图4_内容类型占比饼图_黑白版.svg")
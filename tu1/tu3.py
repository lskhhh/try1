import matplotlib.pyplot as plt

# ===================== 1. 修复中文显示 =====================
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows黑体，中文全正常
plt.rcParams['axes.unicode_minus'] = False

# ===================== 2. 数据（完全匹配论文分析内容） =====================
platform_name = ["抖音", "B站", "微博", "视频号"]  # 平台名称
heat_index = [92, 85, 63, 41]                   # 综合传播热度指数

# ===================== 3. 绘图设置（已改为黑白色调） =====================
plt.figure(figsize=(10, 6), dpi=150)

# 💡 修改1：将 color 改为 '#808080' (中 grey)，添加 'edgecolor="black"' (黑边框) 和 'linewidth=1' (线宽)
bars = plt.bar(platform_name, heat_index, color='#808080', edgecolor="black", linewidth=1)

# 柱子上方标注数值 (将字体颜色改为黑色)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1.2,
             f'{height}', ha='center', va='bottom', fontsize=11, color='black') # 💡 修改2：指定 color='black'

# 标题、坐标轴
plt.title("主流新媒体平台传统文化传播热度对比图", fontsize=15, pad=20, color='black') # 💡 修改3：指定 color='black'
plt.xlabel("新媒体平台", fontsize=12, color='black') # 💡 修改4：指定 color='black'
plt.ylabel("综合传播热度指数", fontsize=12, color='black') # 💡 修改5：指定 color='black'
plt.ylim(0, 105)

# 💡 修改6：网格线颜色改为稍深的灰色 '#bfbfbf' (即灰色 191)，并将透明度 'alpha' 调高到 0.5
plt.grid(axis='y', alpha=0.5, color='#bfbfbf')

# ===================== 4. 导出SVG矢量图（老师要求！无限放大清晰） =====================
plt.savefig("图3_平台热度对比柱状图.svg", format="svg", bbox_inches="tight")
plt.close()

print("✅ 图3矢量图生成完成！文件：图3_平台热度对比柱状图.svg (已改为黑白色)")
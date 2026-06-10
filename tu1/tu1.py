import matplotlib.pyplot as plt

# ===================== 修复中文显示 =====================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# ===================== 数据（和你原图完全一样） =====================
years = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
count = [1,1,2,5,5,7,12,12,11,30,29,33,57,76,95,91,76,84,98,120]

# ===================== 绘图 =====================
plt.figure(figsize=(10, 5), dpi=150)
plt.plot(years, count, marker='o', color='black', linewidth=1.5)

# 标注数值
for x, y in zip(years, count):
    plt.text(x, y + 3, str(y), ha='center', fontsize=10)

# 标题与坐标轴
plt.title("2005-2024 年传统文化传播领域年度发文量趋势图", fontsize=14)
plt.xlabel("年份", fontsize=12)
plt.ylabel("发文量/篇", fontsize=12)
plt.xticks(years, rotation=45)
plt.grid(alpha=0.3)

# ===================== 直接导出矢量图（不弹窗，不报错） =====================
plt.savefig("图1_发文趋势矢量图.svg", format="svg", bbox_inches="tight")
plt.close()  # 不显示窗口，彻底避免报错

print("✅ 矢量图已生成：图1_发文趋势矢量图.svg")
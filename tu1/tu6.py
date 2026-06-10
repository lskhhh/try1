from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 修复中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 论文高频情感词（传统文化领域）
text = """
优秀 经典 传承 文化自信 国风 好看 震撼 感动 喜欢 热爱
精彩 温暖 治愈 用心 唯美 大气 高级 有底蕴 有内涵 传统
中华文化 民族 骄傲 自豪 感动 震撼 传承下去 太美了 支持
非遗 民俗 古风 艺术 历史 厚重 典雅 韵味 动人 共鸣
"""

# 纯黑白词云（论文专用）
wc = WordCloud(
    width=1000,
    height=600,
    background_color="white",    # 白底
    colormap="gray",             # 纯黑白色调
    font_path="simhei.ttf",      # 中文黑体
    max_words=100,
    prefer_horizontal=0.9
)

wc.generate(text)

# 保存矢量图
plt.figure(figsize=(10, 6), dpi=150)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

plt.savefig("图6_传统文化情感词云_黑白矢量.svg", format="svg", bbox_inches="tight")
plt.close()

print("✅ 图6 黑白词云矢量图生成完成！")
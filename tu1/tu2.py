import matplotlib.pyplot as plt
import networkx as nx

# ===================== 1. 修复中文显示 =====================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ===================== 2. 节点与权重数据 =====================
nodes = {
    "传统文化": 35, "文化传播": 28, "文化传承": 26, "国际传播": 22,
    "传播": 18, "文化自信": 15, "新媒体": 12, "传播策略": 10,
    "对外传播": 9, "茶文化": 7, "传承": 6
}
edges = [
    ("传统文化", "文化传播"), ("传统文化", "文化传承"), ("传统文化", "文化自信"),
    ("传统文化", "传播"), ("文化传播", "国际传播"), ("文化传播", "新媒体"),
    ("文化传播", "传播策略"), ("文化传承", "对外传播"), ("文化传承", "茶文化"),
    ("文化传承", "传承"), ("传播", "传播策略"), ("文化自信", "新媒体"),
]

# ===================== 4. 构建网络图 =====================
G = nx.Graph()
for node, size in nodes.items():
    G.add_node(node, size=size)
G.add_edges_from(edges)

# 生成原始布局坐标
pos = nx.spring_layout(G, k=3.5, iterations=50, seed=10)

# 💡 【核心修改】：创建专门用于标签的坐标字典，将 y 轴向上平移
# 偏移量 0.08 可以根据球的大小微调，如果球太大压到字，就改成 0.1
pos_labels = {}
for node, coords in pos.items():
    pos_labels[node] = (coords[0], coords[1] + 0.08)

# ===================== 5. 绘图（黑白风格） =====================
plt.figure(figsize=(12, 10), dpi=150)

# 画连线
nx.draw_networkx_edges(G, pos, edge_color='#bfbfbf', alpha=0.8, width=1.2)

# 分别绘制核心节点和外围节点（小球）
core_nodes = ["传统文化", "文化传播", "文化传承", "国际传播", "传播", "文化自信"]
for node in G.nodes:
    size = G.nodes[node]['size'] * 35
    color = 'black' if node in core_nodes else '#e6e6e6'
    nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=size,
                            node_color=color, node_shape='o',
                            edgecolors='black', linewidths=1.0)

# 💡 【核心修改】：使用偏移后的坐标 pos_labels 绘制文字标签
nx.draw_networkx_labels(G, pos_labels, font_size=11, font_family='SimHei', font_color='black')

plt.axis('off')
plt.title("传统文化传播研究关键词共现知识图谱", fontsize=15, pad=20)

# ===================== 6. 导出SVG =====================
plt.savefig("图2_关键词共现图_标签置顶.svg", format="svg", bbox_inches="tight")
plt.close()

print("✅ 生成完成！文字标签已移动至小球上方。")
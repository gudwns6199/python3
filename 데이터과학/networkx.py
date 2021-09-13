import networkx as nx

G = nx.Graph()

G.add_edge("A","B")
G.add_edge("B",'C')
G.add_edge("B","D")

pos = nx.spring_layout(G)

nx.draw(G,pos,with_labels = True)
plt.show()

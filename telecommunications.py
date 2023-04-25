import networkx as nx
import matplotlib.pyplot as plt

# Criando uma nova rede
G = nx.Graph()

# Adicionando cinco nós à rede
G.add_node('Inova', visitors=2000)
G.add_node('Finaxi', visitors=800)
G.add_node('Luxe', visitors=300)
G.add_node('Tech', visitors=1500)
G.add_node('Foodie', visitors=700)

# Adicionando cinco arestas entre os nós
G.add_edge('Inova', 'Finaxi')
G.add_edge('Inova', 'Luxe')
G.add_edge('Finaxi', 'Tech')
G.add_edge('Luxe', 'Tech')
G.add_edge('Tech', 'Foodie')

# Visualizando a rede
nx.draw(G, with_labels=True, node_size=[v*10 for v in nx.get_node_attributes(G, 'visitors').values()])
plt.show()

import networkx as nx
import matplotlib.pyplot as plt
import random

NUM_NODES = 7
EDGE_PROB = 0.3
# continua a creare un grafo con 
#   - n nodi
#   - probabilità p che tra due nodi ci sia un arco
# fino a che non è connesso
def connected_erdos_renyi(n, p, directed=False):
    while True:
        G = nx.erdos_renyi_graph(n, p, directed=directed)
        if nx.is_connected(G):
            return G

def naive_mst(graph: nx.Graph) -> nx.Graph:
    soluzione_corrente = nx.Graph()
    soluzione_corrente.add_node(list(graph.nodes())[0])

    while soluzione_corrente.number_of_nodes() < graph.number_of_nodes():
        # itero su tutti i lati di frontiera per trovare quello più corto
        best_node = -1
        best_edge = (-1, -1)
        min = 100000

        for n in list(soluzione_corrente.nodes()):
            # NB: graph.adj[n] mi restituisce una mappa {nodo_adj: dict_attrs sull'arco}
            for neighbor, attrs in graph.adj[n].items():
                if neighbor not in list(soluzione_corrente.nodes()) and attrs['weight'] < min:
                    min = attrs['weight']
                    best_node = neighbor
                    best_edge = (n, neighbor)

        soluzione_corrente.add_node(best_node)
        soluzione_corrente.add_edge(*best_edge)

        print(soluzione_corrente.nodes(), soluzione_corrente.edges())

    return soluzione_corrente





G = connected_erdos_renyi(NUM_NODES, EDGE_PROB)

print("nodes", G.number_of_nodes(), G.nodes())
print("edges", G.number_of_edges(), G.edges())

# Aggiungo pesi casuali agli archi
for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)  # peso casuale tra 1 e 10

mst = naive_mst(G)


### disegno

# Creo la figura con 2 subplot affiancati
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
# Layout comune per entrambi i grafi
# pos = nx.spring_layout(G)
# pos = nx.kamada_kawai_layout(G)
pos = nx.shell_layout(G)

nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', ax=ax1)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1)
ax1.set_title("Grafo originale")

# Disegno tutti i nodi come prima
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', ax=ax2)
# Evidenzio solo gli archi del MST in rosso e più spessi
nx.draw_networkx_edges(mst, pos, edge_color='red', width=2, ax=ax2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax2)
ax2.set_title("MST")

plt.show()






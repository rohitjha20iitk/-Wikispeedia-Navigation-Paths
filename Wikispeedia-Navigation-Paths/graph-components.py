import csv
from collections import defaultdict
import networkx as nx

graph = nx.Graph()
with open('edges.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict2 = defaultdict(list)
    for row in data:
        graph.add_edge(row["From_ArticleID"],row["To_ArticleID"])

d = list()
components = (graph.subgraph(c).copy() for c in nx.connected_components(graph))

for c in components:
    d.append((nx.number_of_nodes(c),nx.number_of_edges(c),nx.diameter(c)))

for i in range(12):
    d.append((1,0,0))


fields = ['Nodes', 'Edges', 'Diameter']
filename = "graph-components.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(d)

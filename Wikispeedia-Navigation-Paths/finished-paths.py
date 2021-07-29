import csv
import networkx as nx
from collections import defaultdict

m1 = list()
m2 = list()

tsv_file = open("paths_finished.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
dict1 = dict()
count = 0
for row in read_tsv:
    if row:
        if not row[0].startswith("#"):
            count += 1
            dict1[count] = row[3]


with open('article-ids.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict2 = dict()
    for row in data:
        dict2[row["Article_Name"]] = row["Article_ID"]



graph = nx.DiGraph()
with open('edges.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        graph.add_edge(row["From_ArticleID"],row["To_ArticleID"])

for count,path in dict1.items():
    counter = 0
    l = path.split(";")
    if "<" in l:
        for article in l:
            if article == "<":
                counter += 1
        humanpathnotcounted = len(l) - 1 - 2*counter
        humanpathcounted = len(l) - 1
        start = l[0]
        end = l[-1]
        idstart = dict2[start]
        idend = dict2[end]
        shortestpath = len(nx.shortest_path(graph, idstart, idend)) - 1
        rationotcounted = humanpathnotcounted / shortestpath
        ratiocounted = humanpathcounted / shortestpath
        m1.append((humanpathnotcounted, shortestpath, rationotcounted))
        m2.append((humanpathcounted, shortestpath, ratiocounted))

    else:
        humanpath = len(l) - 1
        start = l[0]
        end = l[-1]
        idstart = dict2[start]
        idend = dict2[end]

        shortestpath = len(nx.shortest_path(graph, idstart, idend)) - 1
        ratio = humanpath / shortestpath
        m1.append((humanpath, shortestpath, ratio))
        m2.append((humanpath, shortestpath, ratio))



fields = ['Human_Path_Length', 'Shortest_Path_Length', 'Ratio']
filename = "finished-paths-back.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(m2)


fields = ['Human_Path_Length', 'Shortest_Path_Length', 'Ratio']
filename = "finished-paths-no-back.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(m1)
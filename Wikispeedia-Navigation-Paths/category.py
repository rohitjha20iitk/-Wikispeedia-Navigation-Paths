import csv
from collections import defaultdict

graph = defaultdict(list)
visited = []
queue = []
d = []

def addEdge(u, v):
    graph[u].append(v)


def bfs(visited, graph, node):
  count = 0
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    count += 1
    if count <= 9:
        str1 = "C000" + str(count)
    elif count <= 99:
        str1 = "C00" + str(count)
    elif count <= 999:
        str1 = "C0" + str(count)
    else:
        str1 = "C" + str(count)
    d.append((s,str1))


    for neighbour in sorted(graph[s]):
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


tsv_file = open("categories.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
counter = 0
for row in read_tsv:
  if row:
    if not row[0].startswith("#"):
        str0 = row[1]
        str1 = str0.split(".")
        second = str1[0] + "." + str1[1]
        addEdge(str1[0],second)
        try:
            third = second + "." + str1[2]
            addEdge(second, third)
        except:
            pass
        try:
            fourth = third + "." + str1[3]
            addEdge(third, fourth)
        except:
            pass
bfs(visited, graph, 'subject')

fields = ['Category_Name', 'Category_ID']
filename = "category-ids.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(sorted(d))



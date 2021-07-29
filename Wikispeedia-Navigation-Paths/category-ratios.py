import csv
import networkx as nx
from collections import defaultdict
from functools import reduce

d = list()
mydict1 = defaultdict(list)


graph = nx.DiGraph()
with open('edges.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        graph.add_edge(row["From_ArticleID"],row["To_ArticleID"])

tsv_file = open("paths_finished.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
dict1 = dict()
count = 0
for row in read_tsv:
    if row:
        if not row[0].startswith("#"):
            count += 1
            dict1[count] = row[3]


tsv_file = open("paths_unfinished.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
dict6 = dict()
dict51 = dict()
count = 0
for row in read_tsv:
    if row:
        if not row[0].startswith("#"):
            count += 1
            dict6[count] = row[3]
            dict51[count] = row[4]


with open('category-ids.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict2 = dict()
    for row in data:
        dict2[row["Category_ID"]] = row["Category_Name"]



with open('category-ids.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict9 = dict()
    for row in data:
        dict9[row["Category_Name"]] = row["Category_ID"]


with open('article-ids.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict3 = dict()
    for row in data:
        dict3[row["Article_Name"]] = row["Article_ID"]


with open('article-categories.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict4 = dict()
    for row in data:
        dict4[row["Article_ID"]] = row["Category_ID"]



def findparent(categoryfullname):
    categoryidslist = ['C0001']
    categoriess = categoryfullname.split(".")
    name = "subject."
    for x in categoriess:
        if name != categoryfullname:
            if x != categoriess[0]:
                name += x
                categoryidslist.append(dict9[name])
                name += "."
    return categoryidslist


for x in dict1.values():
    sourcelist1 = list()
    destlist1 = list()
    articles = x.split(";")
    l = list()
    for article in articles:
        if article != "<":
            l.append(article)
        else:
            l.pop(-1)
    source = dict3[l[0]]
    destination = dict3[l[-1]]
    str11 = dict4[source][1:-1]
    str12 = dict4[destination][1:-1]
    str1 = str11[1:6]
    categoryidslist1 = findparent(dict2[str1])
    for id1 in categoryidslist1:
        sourcelist1.append(id1)
    try:
        if str11[10] == "C":
            str2 = str11[10:15]
            categoryidslist2 = findparent(dict2[str2])
            for id1 in categoryidslist2:
                sourcelist1.append(id1)
            try:
                if str11[19] == "C":
                    str3 = str11[19:24]
                    categoryidslist3 = findparent(dict2[str2])
                    for id1 in categoryidslist3:
                        sourcelist1.append(id1)
            except:
                pass
    except:
        pass

    str7 = str12[1:6]
    categoryidslist7 = findparent(dict2[str7])
    for id1 in categoryidslist7:
        destlist1.append(id1)
    try:
        if str12[10] == "C":
            str8 = str12[10:15]
            categoryidslist8 = findparent(dict2[str8])
            for id1 in categoryidslist8:
                destlist1.append(id1)
            try:
                if str12[19] == "C":
                    str9 = str12[19:24]
                    categoryidslist9 = findparent(dict2[str9])
                    for id1 in categoryidslist9:
                        destlist1.append(id1)
            except:
                pass
    except:
        pass

    for p in sourcelist1:
        for q in destlist1:
            ratio = (len(l) - 1) / (len(nx.shortest_path(graph, source, destination)) - 1)
            mydict1[(p, q)].append(ratio)




m = list()
for x,y in mydict1.items():
    sum = 0
    count = 0
    for z in y:
        sum += z
        count += 1
    if count != 0:
        m.append((x[0], x[1], sum / (count)))



fields = ['From_Category', 'To_Category', 'Ratio_of_human_to_shortest']
filename = "category-ratios.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(sorted(m))
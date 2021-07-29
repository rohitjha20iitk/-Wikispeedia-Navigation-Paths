import csv
from collections import defaultdict
import networkx as nx


mydict1 = dict()
mydict2 = dict()
mydict3 = dict()
mydict4 = dict()
mydict5 = dict()
mydict6 = dict()
for i in range(1,147):
    mydict1[i] = 0
    mydict2[i] = 0
    mydict3[i] = 0
    mydict4[i] = 0
    mydict5[i] = 0
    mydict6[i] = 0



graph = nx.DiGraph()
with open('edges.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict2 = defaultdict(list)
    for row in data:
        graph.add_edge(row["From_ArticleID"],row["To_ArticleID"])


d = list()

tsv_file = open("paths_finished.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
dict1 = dict()
count = 0
for row in read_tsv:
    if row:
        if not row[0].startswith("#"):
            count += 1
            dict1[count] = row[3]



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

for path in dict1.values():
    l = list()
    str = path.split(";")
    for article in str:
        if article != "<":
            l.append(article)
        else:
            l.pop(-1)


    for y in l:
        articleid = dict3[y]
        str4 = dict4[articleid][1:-1]
        str1 = str4[2:6]
        str10 = str4[1:6]
        categoryidslist1 = findparent(dict2[str10])
        for id1 in categoryidslist1:
            id2 = id1
            id3 = int(id2[1:])
            mydict2[id3] += 1
        if mydict5[int(str1)]  == 0:
            for id1 in categoryidslist1:
                id2 = id1
                id3 = int(id2[1:])
                if mydict5[id3] == 0:
                    mydict1[id3] += 1
                    mydict5[id3] = 1
        try:
            if str4[10] == "C":
                str2 = str4[11:15]
                str20 = str4[10:15]
                categoryidslist2 = findparent(dict2[str20])
                for id1 in categoryidslist2:
                    id2 = id1
                    id3 = int(id2[1:])
                    mydict2[id3] += 1
                if mydict5[int(str2)] == 0:
                    for id1 in categoryidslist2:
                        id2 = id1
                        id3 = int(id2[1:])
                        if mydict5[id3] == 0:
                            mydict1[id3] += 1
                            mydict5[id3] = 1
                try:
                    if str4[19] == "C":
                        str3 = str4[20:24]
                        str30 = str4[19:24]
                        categoryidslist3 = findparent(dict2[str30])
                        for id1 in categoryidslist3:
                            id2 = id1
                            id3 = int(id2[1:])
                            mydict2[id3] += 1
                        if mydict5[int(str3)] == 0:
                            for id1 in categoryidslist3:
                                id2 = id1
                                id3 = int(id2[1:])
                                if mydict5[id3] == 0:
                                    mydict1[id3] += 1
                                    mydict5[id3] = 1
                except:
                    pass
        except:
            pass


    source = dict3[l[0]]
    destination = dict3[l[-1]]
    for f in nx.shortest_path(graph, source, destination):
        str5 = dict4[f][1:-1]
        str7 = str5[2:6]
        str70 = str5[1:6]
        categoryidslist7 = findparent(dict2[str70])
        for id1 in categoryidslist7:
            id2 = id1
            id3 = int(id2[1:])
            mydict4[id3] += 1
        if mydict6[int(str7)] == 0:
            for id1 in categoryidslist7:
                id2 = id1
                id3 = int(id2[1:])
                if mydict6[id3] == 0:
                    mydict3[id3] += 1
                    mydict6[id3] = 1
        try:
            if str5[10] == "C":
                str8 = str5[11:15]
                str80 = str5[10:15]
                categoryidslist8 = findparent(dict2[str80])
                for id1 in categoryidslist8:
                    id2 = id1
                    id3 = int(id2[1:])
                    mydict4[id3] += 1
                if mydict6[int(str8)] == 0:
                    for id1 in categoryidslist8:
                        id2 = id1
                        id3 = int(id2[1:])
                        if mydict6[id3] == 0:
                            mydict3[id3] += 1
                            mydict6[id3] = 1
                try:
                    if str5[19] == "C":
                        str9 = str5[20:24]
                        str90 = str5[19:24]
                        categoryidslist9 = findparent(dict2[str90])
                        for id1 in categoryidslist9:
                            id2 = id1
                            id3 = int(id2[1:])
                            mydict4[id3] += 1
                        if mydict6[int(str9)] == 0:
                            for id1 in categoryidslist9:
                                id2 = id1
                                id3 = int(id2[1:])
                                if mydict6[id3] == 0:
                                    mydict3[id3] += 1
                                    mydict6[id3] = 1
                except:
                    pass
        except:
            pass

    for i in range(1, 147):
        mydict5[i] = 0
        mydict6[i] = 0


for x,y in mydict1.items():
    if x <= 9:
        id5 = "C000"
    elif x <= 99:
        id5 = "C00"
    elif x <= 999:
        id5 = "C0"
    else:
        id5 = "C"
    stry = "{id}{number}".format(id=id5, number=x)
    d.append((stry,mydict1[x],mydict2[x],mydict3[x],mydict4[x]))



fields = ['Category_ID', 'Number_of_human_paths_traversed', 'Number_of_human_times_traversed' , 'Number_of_shortest_paths_traversed', 'Number_of_shortest_times_traversed']
filename = "category-subtree-paths.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(d)
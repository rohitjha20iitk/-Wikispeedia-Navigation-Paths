import csv
from collections import defaultdict
from functools import reduce

d = list()
mydict1 = dict()
mydict2 = dict()

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
    source = dict3[articles[0]]
    destination = dict3[articles[-1]]
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

    for x in sourcelist1:
        for y in destlist1:
            try:
                mydict1[(x, y)] = mydict1.get((x, y)) + 1
            except:
                mydict1[(x, y)] = mydict1.get((x, y),0) + 1


for y,x in dict6.items():
    sourcelist1 = list()
    destlist1 = list()
    try:
        articles = x.split(";")
        source = dict3[articles[0]]
        destination = dict3[dict51[y]]
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

    except:
        sourcelist1.append("C0001")
        destlist1.append("C0001")


    for x in sourcelist1:
        for y in destlist1:
            try:
                mydict2[(x, y)] = mydict2.get((x, y)) + 1
            except:
                mydict2[(x, y)] = mydict2.get((x, y), 0) + 1


alldict = [mydict1, mydict2]
allkey = reduce(set.union, map(set, map(dict.keys, alldict)))


for x in allkey:
    try:
        a = mydict1[x]
    except:
        a = 0
    try:
        b = mydict2[x]
    except:
        b = 0
    first = (a/(a+b)) * 100
    d.append((x[0], x[1], first, 100-first))




fields = ['From_Category', 'To_Category', 'Percentage_of_finished_paths' , 'Percentage_of_unfinished_paths']
filename = "category-pairs.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(sorted(d))

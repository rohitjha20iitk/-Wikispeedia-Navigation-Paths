import csv
from collections import defaultdict

d = list()

tsv_file = open("categories.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
dict1 = defaultdict(list)
for row in read_tsv:
    if row:
        if not row[0].startswith("#"):
            dict1[row[0]].append(row[1])


with open('article-ids.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict2 = dict()
    for row in data:
        dict2[row["Article_Name"]] = row["Article_ID"]


with open('category-ids.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict3 = dict()
    for row in data:
        dict3[row["Category_Name"]] = row["Category_ID"]



for x,y in dict2.items():
    m = list()
    if x in dict1.keys():
        for z in dict1[x]:
                m.append(dict3[z])

    m = list(dict.fromkeys(m))
    if len(m) != 0:
        d.append((y, m))
    else:
        d.append((y, ['C0001']))



fields = ['Article_ID', 'Category_ID']
filename = "article-categories.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(d)

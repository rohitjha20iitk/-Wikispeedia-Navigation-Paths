import csv

d = list()

def find(s,ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

with open("shortest-path-distance-matrix.txt", 'r') as f:
    wordlist = f.read().splitlines()
f.close()
edge = 0
for strings in wordlist:
    if len(strings) == 4604:
        edge += 1
        if edge <= 9:
            str1 = "A000" + str(edge)
        elif edge <= 99:
            str1 = "A00" + str(edge)
        elif edge <= 999:
            str1 = "A0" + str(edge)
        else:
            str1 = "A" + str(edge)


        m = find(strings,"1")
        for y in m:
            x = y + 1
            if x <= 9:
                str2 = "A000" + str(x)
            elif x <= 99:
                str2 = "A00" + str(x)
            elif x <= 999:
                str2 = "A0" + str(x)
            else:
                str2 = "A" + str(x)
            d.append((str1, str2))
fields = ['From_ArticleID', 'To_ArticleID']
filename = "edges.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(d)


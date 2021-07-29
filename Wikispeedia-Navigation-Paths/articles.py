import csv

d = list()

tsv_file = open("articles.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
count = 0
for row in read_tsv:
  if row:
    if not row[0].startswith("#"):
      count += 1
      if count <= 9:
          str1 = "A000" + str(count)
      elif count <= 99:
          str1 = "A00" + str(count)
      elif count <= 999:
          str1 = "A0" + str(count)
      else:
          str1 = "A" + str(count)
      d.append((str(row[0]),str1))

fields = ['Article_Name', 'Article_ID']
filename = "article-ids.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(sorted(d))


import csv
from _csv import reader
from collections import defaultdict

count = 0
with open('finished-paths-no-back.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict1 = defaultdict(list)
    for row in data:
        count += 1
        dict1[count].append((row["Human_Path_Length"],row["Shortest_Path_Length"]))




count = 0
with open('finished-paths-back.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    dict2 = defaultdict(list)
    for row in data:
        count += 1
        dict2[count].append((row["Human_Path_Length"],row["Shortest_Path_Length"]))

total1 = len(dict1.keys())

same = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
more = 0

for x,y in dict1.items():
    if int(y[0][0]) - int(y[0][1]) == 0:
        same += 1
    elif int(y[0][0]) - int(y[0][1]) == 1:
        one += 1
    elif int(y[0][0]) - int(y[0][1]) == 2:
        two += 1
    elif int(y[0][0]) - int(y[0][1]) == 3:
        three += 1
    elif int(y[0][0]) - int(y[0][1]) == 4:
        four += 1
    elif int(y[0][0]) - int(y[0][1]) == 5:
        five += 1
    elif int(y[0][0]) - int(y[0][1]) == 6:
        six += 1
    elif int(y[0][0]) - int(y[0][1]) == 7:
        seven += 1
    elif int(y[0][0]) - int(y[0][1]) == 8:
        eight += 1
    elif int(y[0][0]) - int(y[0][1]) == 9:
        nine += 1
    elif int(y[0][0]) - int(y[0][1]) == 10:
        ten += 1
    else:
        more += 1

first = ((same/total1)*100)
first = round(first,2)

second = ((one/total1)*100)
second = round(second,2)

third = ((two/total1)*100)
third = round(third,2)

fourth = ((three/total1)*100)
fourth = round(fourth,2)

fifth = ((four/total1)*100)
fifth = round(fifth,2)

sixth = ((five/total1)*100)
sixth = round(sixth,2)

seventh = ((six/total1)*100)
seventh = round(seventh,2)

eighth = ((seven/total1)*100)
eighth = round(eighth,2)

ninth = ((eight/total1)*100)
ninth = round(ninth,2)

tenth = ((nine/total1)*100)
tenth = round(tenth,2)

eleventh = ((ten/total1)*100)
eleventh = round(eleventh,2)

twelfth = ((more/total1)*100)
twelfth = round(twelfth,2)

m1 = list()
m1.append((first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,tenth,eleventh,twelfth))



total2 = len(dict2.keys())

same = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
more = 0

for x,y in dict2.items():
    if int(y[0][0]) == int(y[0][1]):
        same += 1
    elif int(y[0][0]) - int(y[0][1]) == 1:
        one += 1
    elif int(y[0][0]) - int(y[0][1]) == 2:
        two += 1
    elif int(y[0][0]) - int(y[0][1]) == 3:
        three += 1
    elif int(y[0][0]) - int(y[0][1]) == 4:
        four += 1
    elif int(y[0][0]) - int(y[0][1]) == 5:
        five += 1
    elif int(y[0][0]) - int(y[0][1]) == 6:
        six += 1
    elif int(y[0][0]) - int(y[0][1]) == 7:
        seven += 1
    elif int(y[0][0]) - int(y[0][1]) == 8:
        eight += 1
    elif int(y[0][0]) - int(y[0][1]) == 9:
        nine += 1
    elif int(y[0][0]) - int(y[0][1]) == 10:
        ten += 1
    else:
        more += 1

first = ((same/total2)*100)
first = round(first,2)

second = ((one/total2)*100)
second = round(second,2)

third = ((two/total2)*100)
third = round(third,2)

fourth = ((three/total2)*100)
fourth = round(fourth,2)

fifth = ((four/total2)*100)
fifth = round(fifth,2)

sixth = ((five/total2)*100)
sixth = round(sixth,2)

seventh = ((six/total2)*100)
seventh = round(seventh,2)

eighth = ((seven/total2)*100)
eighth = round(eighth,2)

ninth = ((eight/total2)*100)
ninth = round(ninth,2)

tenth = ((nine/total2)*100)
tenth = round(tenth,2)

eleventh = ((ten/total2)*100)
eleventh = round(eleventh,2)

twelfth = ((more/total2)*100)
twelfth = round(twelfth,2)

m2 = list()
m2.append((first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,tenth,eleventh,twelfth))

fields = ['Equal_Length', 'Larger_by_1', 'Larger_by_2', 'Larger_by_3', 'Larger_by_4', 'Larger_by_5', 'Larger_by_6',
          'Larger_by_7', 'Larger_by_8', 'Larger_by_9', 'Larger_by_10', 'Larger_by_more_than_10']
filename = "percentage-paths-no-back.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(m1)


fields = ['Equal_Length', 'Larger_by_1', 'Larger_by_2', 'Larger_by_3', 'Larger_by_4', 'Larger_by_5', 'Larger_by_6',
          'Larger_by_7', 'Larger_by_8', 'Larger_by_9', 'Larger_by_10', 'Larger_by_more_than_10']
filename = "percentage-paths-back.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(m2)






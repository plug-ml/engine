import csv
import random
import math

with open('sinedata.csv', 'w', newline='') as sinedata:
    datawriter = csv.writer(sinedata, delimiter=' ')
    for i in range(1000):
        n = 200*random.random() - 100
        datawriter.writerow([str(n)] + [str(math.sin(n))])


with open('lindata.csv', 'w', newline='') as lindata:
    lindatawriter = csv.writer(lindata, delimiter=' ')
    for i in range(1000):
        n = 2000*random.random() - 1000
        lindatawriter.writerow([str(n)] + [str(-1.7*n + 20.513)])
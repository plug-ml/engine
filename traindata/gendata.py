import csv
import random
import math

with open('sine_test_data.csv', 'w', newline='') as sinetestdata:
    datawriter = csv.writer(sinetestdata, delimiter=' ')
    for i in range(1000):
        n = 8*random.random() - 4
        datawriter.writerow([str(n)] + [str(math.sin(n))])


with open('lin_test_data.csv', 'w', newline='') as lindata:
    lindatawriter = csv.writer(lindata, delimiter=' ')
    for i in range(1000):
        n = 2000*random.random() - 1000
        lindatawriter.writerow([str(n)] + [str(-1.7*n + 20.513)])

with open('sine_train_data.csv', 'w', newline='') as sinetestdata:
    datawriter = csv.writer(sinetestdata, delimiter=' ')
    for i in range(1000):
        n = 8*random.random() - 4
        datawriter.writerow([str(n)] + [str(math.sin(n))])


with open('lin_train_data.csv', 'w', newline='') as lindata:
    lindatawriter = csv.writer(lindata, delimiter=' ')
    for i in range(1000):
        n = 2000*random.random() - 1000
        lindatawriter.writerow([str(n)] + [str(-1.7*n + 20.513)])
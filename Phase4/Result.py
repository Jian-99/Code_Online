#Author: Jian Gao
#Date: July, 2019
#University of British Columbia
#All rights reserved

import numpy as np
import csv

def Get_result():
    #test_data = pd.read_csv("./Test/Test.csv")
    #y_pred = classifier.predict(test_data)
    #np.savetxt("result.csv", y_pred, delimiter=",")

    with open('result.csv', 'r') as csvfile:
        first_line = csvfile.readline()
        data = csvfile.readlines()
    
    #Count the number of columns
    ncol = first_line.count(',') + 1
    row = []
    for element in range (1,ncol+1):
        row.append(element)

    #Insert the labels in the first row
    with open('result.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines.insert(0, row)

    with open('result.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    readFile.close()
    writeFile.close()

    print ("Result is now out")

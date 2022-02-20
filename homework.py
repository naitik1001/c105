import math
import csv

from numpy import number
with open("C:/Users/gogof/Desktop/coding/hi-main/c105/homework.csv", newline = '' ) as f:   
    reader =  csv.reader(f)
    file_data = list(reader)
data = file_data[0]
def mean{data}:
    n = data
    total = 0
    for n in data:
        total = int(x)
        mean = total/n
        return mean
        squared list = []
        for number in range:
            a = int(number)-data
            a = a**2
            squaredlist.append(a)
            sum = 0
            for i in squared_list:
    sum = sum + i
result = sum/(len(data)-1)
standard_deviation =  math.sqrt(result)
print(standard_deviation)
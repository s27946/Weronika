import matplotlib
import numpy as np

import pandas as pd

# zad1
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

av_height = np.average(heights)
print("Mean height: {} ".format(round(av_height, 2)))

std_height = np.std(heights)
print("Standard deviation: {} ".format(std_height))

max_height = np.max(heights)
print("Maximum height: {} ".format(max_height))

min_height = np.min(heights)
print("Minimum height: {} ".format(min_height))

percentile_height_25 = np.percentile(heights, 25)
print("25th percentile: {} ".format(percentile_height_25))

percentile_height_75 = np.percentile(heights, 75)
print("75th percentile: {} ".format(percentile_height_75))

mediana = np.median(heights)
print("Median: {}".format(mediana))
print('--------')
# zad2

zad2 = pd.read_csv('Zadanie_2.csv')
array_zad2 = np.array(zad2)
# tworzenie macierzy z ciągu znaków
matrix_zad2 = np.genfromtxt('Zadanie_2.csv', delimiter=";", dtype=int)
print(matrix_zad2)
a, b = np.linalg.eig(matrix_zad2)
print(a)
print('---')
print(b)
reverse_matrix = np.linalg.inv(matrix_zad2)
print(reverse_matrix)

print("------------")

# zad3

rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0
inches.shape

import matplotlib.pyplot as plt
import seaborn;

seaborn.set()
plt.hist(inches, 40)
print("Number days without rain: {}".format(np.sum(inches != 0)))
print("Number days with rain: {}".format(np.sum(inches == 0)))
print("Days with more than 0.5 inches: {}".format(np.sum(inches > 0.5)))
print("Rainy days with < 0.2 inches: {}".format(np.sum(np.logical_and(inches > 0, inches < 0.2))))
print("Median precip on rainy days in 2014  (inches): {}".format(np.median(inches[inches != 0])))
summerDays = inches[172:262]
notSummer_1 = inches[:172]
notSummer_2 = inches[262:]
notSummer = np.concatenate([notSummer_2, notSummer_1])
maska = (notSummer > 0)  # tworzymy maskę wartości logicznych, która pozwoli nam odfiltrować dane,
# gdy nie padało
notSummer_vals = notSummer[maska]  # nakładamy maskę na wartości i zapisujemy do nowej zmiennej
print("Median precip on summer days in 2014 (inches) {}".format(np.median(summerDays)))
print("Maximum precip on summer days in 2014 (inches) {}".format(np.max(summerDays)))
print("Median precip on non-summer rainy days (inches) {}".format(np.median(notSummer_vals)))
print('-------')
# zad4
A = [0, 3, 2, 5]
B = [0, 3, 1, 4]

print(np.add(A,B))
print(np.subtract(B,A))
a = 4
print(np.multiply(A,a))
print(np.dot(A,B))
print(np.linalg.norm(B))

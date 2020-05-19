import math
from knn import KnN


#we use the rssi values-per-meter

#we find the most valueabe players (k mumber)


import math
from Distance import Distance

knn = KnN(3)
a = []
b = []
c = []
b_total = 0
c_total = 0

A_rssi = 0
B_rssi = 0
C_rssi = 0

j,k,m = 0,0,0


with open("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D1.txt") as rssiValues:
    for line in rssiValues:
        if line[5] == "A":
            a.append(line[9]+line[10])

        if line[5] == "B":
            b.append(line[9]+line[10])

        if line[5] == "C":
            c.append(line[9] + line[10])


#A(0,0), B(d,0), C(d,1)

#Tested points
p = 3
q = 3
r = 3

#Real position
(u, v) = (1.5, 0)


x = knn.knnAlgo(a)*0 + knn.knnAlgo(b)*p + knn.knnAlgo(c)*q
y = knn.knnAlgo(a)*0 + knn.knnAlgo(b)*0 + knn.knnAlgo(c)*r

error = pow((pow((x-u), 2)+pow((y-v), 2)), 0.5)

print("real position {},{}".format(u, v))
print("estimated position {},{}".format(x, y))
print("error {}".format(error))

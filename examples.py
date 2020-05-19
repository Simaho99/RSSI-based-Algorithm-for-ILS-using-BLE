from Distance import Distance
import math

class KnN(object):

    def __init__(self, k):
        self.k = k

    def knnAlgo(self, rs):
        rs_sorted = sorted(rs, reverse=True)
        rs_total1 = 0
        rs_total = 0
        rs_average = 0
        rs_average1 = 0
        rs_corr = 0
        dist_total = 0
        dist_average = 0
        rs_new_avg = 0
        rs_new_tot = 0
        rs_new = 0
        rs_sorted1 = 0
        rs_var = 1
        rs_std = 0
        rs_gaussian_tot = 0
        rs_gaussian_average = 0

        for i in range(0, self.k):
            rs_sorted1 = int(rs_sorted[i]) * -1         # Change string to int, mind the negative sign
            dist = Distance(rs_sorted1).get_distance()   # Calculate their respective distances
            rs_total = rs_total + rs_sorted1            # Calculate its total
            rs_average = rs_total / (i + 1)             # Calculate average

# # Standard Deviation
#         for i in range(0, self.k):
#             rs_sorted1 = int(rs_sorted[i]) * -1
#             rs_var = 1/(self.k - 1) * pow((rs_sorted1 - rs_average), 2)
#             rs_std = pow(rs_var, 2)
#             print(rs_std)
#             print("*"*30)
#             print(rs_var)
#             print(rs_sorted1)
#             print(rs_average)

        for i in range(0, self.k):
            rs_sorted1 = int(rs_sorted[i]) * -1
            rs_corr = rs_sorted1 + pow((pow((rs_sorted1 + rs_average), 2)), 0.5)
            dist = Distance(rs_sorted1).get_distance()
            dist_total = dist_total + dist                # Calculate the total/distance
            dist_average = dist_total / (i + 1)           # Calculate average/distance
            print(dist)

        for i in range(0, len(rs_sorted)):
            rs_sorted1 = int(rs_sorted[i]) * -1
            rs_new = pow((pow(pow(10, rs_corr/10), 2.5)), 0.5)
            rs_new_tot = rs_new_tot + rs_new
            rs_new_avg = rs_new_tot/3
            rs_var = 1 / 2 * pow((rs_sorted1 - rs_new_avg), 2)
            rs_std = pow(rs_var, 0.5)

# Gaussian Filter
        for i in range(0, self.k):
            rs_sorted1 = int(rs_sorted[i]) * -1
            rs_gaussian = (1/(rs_std * pow(2 * math.pi, 0.5))) * \
                          (pow(math.e, - (pow((rs_sorted1-rs_new_avg), 2))))/(2 * rs_var)

            rs_gaussian_distance = Distance(rs_gaussian).get_distance()
            rs_gaussian_tot = rs_gaussian_tot + rs_gaussian_distance
            rs_gaussian_average = rs_gaussian_tot/(i+1)

        dist = Distance(rs_corr).get_distance()
        av_rs = rs_average1/dist

        rs_weighted = rs_gaussian_average/rs_gaussian_tot             # "3" because of the number of the nodes

        return rs_weighted




import matplotlib.pyplot as plt
from Distance import Distance
from knn import KnN
from dataset import DataSet

# The Tested Points
p1 = q1 = r1 = 1
p2 = q2 = r2 = 3
p3 = q3 = r3 = 5


# Data From The First Position
# Distance equal to one meter
data1 = DataSet().rssi_average("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D1.txt")
data1_ = DataSet().doc_opener("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D1.txt")
# Distance equal to three meters
data2 = DataSet().rssi_average("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D1.txt")
data2_ = DataSet().doc_opener("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D1.txt")
# Distance equal to five meters
data3 = DataSet().rssi_average("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D1.txt")
data3_ = DataSet().doc_opener("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D1.txt")
# Real position 1
(u1, v1) = (p1 / 2, 0)
(u2, v2) = (p2 / 2, 0)
(u3, v3) = (p3 / 2, 0)


# # Data From the Second Position
# # Distance equal to one meter
# data1 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D2.txt")
# data1_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D2.txt")
# # Distance equal to three meters
# data2 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D2.txt")
# data2_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D2.txt")
# # Distance equal to five meters
# data3 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D2.txt")
# data3_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D2.txt")
# # Real position 2
# (u1, v1) = (p1 / 2, p1/2)
# (u2, v2) = (p2 / 2, p2/2)
# (u3, v3) = (p3 / 2, p3/2)


# # Data the Third Position
# # Distance equal to one meter
# data1 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D3.txt")
# data1_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D3.txt")
# # Distance equal to three meters
# data2 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D3.txt")
# data2_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D3.txt")
# # Distance equal to five meters
# data3 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D3.txt")
# data3_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D3.txt")
# # Real position 3
# (u1, v1) = (2 * p1 / 3, p1/3)
# (u2, v2) = (2 * p2 / 3, p2/3)
# (u3, v3) = (2 * p3 / 3, p3/3)


# Literature Algorithm
e1 = Distance(data1[0]).get_distance()
f1 = Distance(data1[1]).get_distance()
g1 = Distance(data1[2]).get_distance()
x1 = (pow(e1, 2) - pow(f1, 2) + pow(p1, 2)) / (2 * p1)
y1 = (pow(e1, 2) - pow(g1, 2) + pow(q1, 2) + pow(r1, 2)) / (2 * r1) - (q1 / r1) * x1

e2 = Distance(data2[0]).get_distance()
f2 = Distance(data2[1]).get_distance()
g2 = Distance(data2[2]).get_distance()
x2 = (pow(e2, 2) - pow(f2, 2) + pow(p2, 2)) / (2 * p2)
y2 = (pow(e2, 2) - pow(g2, 2) + pow(q2, 2) + pow(r2, 2)) / (2 * r2) - (q2 / r2) * x2

e3 = Distance(data3[0]).get_distance()
f3 = Distance(data3[1]).get_distance()
g3 = Distance(data3[2]).get_distance()
x3 = (pow(e3, 2) - pow(f3, 2) + pow(p3, 2)) / (2 * p3)
y3 = (pow(e3, 2) - pow(g3, 2) + pow(q3, 2) + pow(r3, 2)) / (2 * r3) - (q3 / r3) * x3


# Our Algorithm
error1_ = []
error1 = []

error2_ = []
error2 = []

error3_ = []
error3 = []


n = 70

x1_, x2_, x3_ = 0, 0, 0
y1_, y2_, y3_ = 0, 0, 0

for i in range(1, n):

    knn = KnN()            # Set the k value

    x1_ = knn.knnAlgo(data1_[0]) * 0 + knn.knnAlgo(data1_[1]) * p1 + knn.knnAlgo(data1_[2]) * q1
    y1_ = knn.knnAlgo(data1_[0]) * 0 + knn.knnAlgo(data1_[1]) * 0 + knn.knnAlgo(data1_[2]) * r1
    error1_.append(pow((pow((x1_ - u1), 2) + pow((y1_ - v1), 2)), 0.5))
    error1.append(pow((pow((x1 - u1), 2) + pow((y1 - v1), 2)), 0.5))

    x2_ = knn.knnAlgo(data2_[0]) * 0 + knn.knnAlgo(data2_[1]) * p2 + knn.knnAlgo(data2_[2]) * q2
    y2_ = knn.knnAlgo(data2_[0]) * 0 + knn.knnAlgo(data2_[1]) * 0 + knn.knnAlgo(data2_[2]) * r2
    error2_.append(pow((pow((x2_ - u2), 2) + pow((y2_ - v2), 2)), 0.5))
    error2.append(pow((pow((x2 - u2), 2) + pow((y2 - v2), 2)), 0.5))

    x3_ = knn.knnAlgo(data3_[0]) * 0 + knn.knnAlgo(data3_[1]) * p3 + knn.knnAlgo(data3_[2]) * q3
    y3_ = knn.knnAlgo(data3_[0]) * 0 + knn.knnAlgo(data3_[1]) * 0 + knn.knnAlgo(data3_[2]) * r3
    error3_.append(pow((pow((x3_ - u3), 2) + pow((y3_ - v3), 2)), 0.5))
    error3.append(pow((pow((x3 - u3), 2) + pow((y3 - v3), 2)), 0.5))



# # Choosing the k value, by checking the error incremental
# error_ = []
# error = []
# knn = KnN(1)
#
# for i in range(1, 70):
#     knn = KnN(i)
#     # Calculate the error produced
#     x_ = knn.knnAlgo(a_)*0 + knn.knnAlgo(b_)*p + knn.knnAlgo(c_)*q
#     y_ = knn.knnAlgo(a_)*0 + knn.knnAlgo(b_)*0 + knn.knnAlgo(c_)*r
#     error_.append(pow((pow((x_-u), 2)+pow((y_-v), 2)), 0.5))
#     error.append(pow((pow((x - u), 2) + pow((y - v), 2)), 0.5))
#
#     # is the error greater than the previous
#     # if YES do not change the k value
#     # if NO then change the k value
#
# for i in range(2, len(error_)):
#     # if yes
#     if error_[i] >= error_[i-1]:
#         knn = KnN(i-1)                  # Keep the value of k
#     elif error_[i] < error_[i-1]:
#         knn = KnN(i)                    # Change the value of k
#
# for i in range(1, 70):
#     x_ = knn.knnAlgo(a_)*0 + knn.knnAlgo(b_)*p + knn.knnAlgo(c_)*q
#     y_ = knn.knnAlgo(a_)*0 + knn.knnAlgo(b_)*0 + knn.knnAlgo(c_)*r
#     error_.append(pow((pow((x_-u), 2)+pow((y_-v), 2)), 0.5))
#     error.append(pow((pow((x - u), 2) + pow((y - v), 2)), 0.5))
#
#
# # plt.plot(range(1, 70), error_, label="Tito's Algo")
# # plt.plot(range(1, 70), error, label="Literature's Algo")
# # plt.legend()
# # plt.xlabel("k Number")
# # plt.ylabel("Localization Error (cm)")
# # plt.show()
#
# print(x)
# print(y)
#

print(" "*50)
print(" "*50)


print("The Distance Equal to One Meter")
print("="*50)
print("Real position: 1                    {:04.4f},{:04.4f}".format(u1, v1))
print("Estimated position  Literature 1    {:04.4f},{:04.4f}".format(x1, y1))
print("Estimated position  Our Algorithm 1 {:04.4f},{:04.4f}".format(x1_, y1_))
print("Error1                              {:04.4f}".format(error1[0]))
print("Error1_                             {:04.4f}".format(error1_[0]))

print(" "*50)
print(" "*50)

print("The Distance Equal to Three Meters")
print("="*50)
print("Real position: 2                    {:04.4f},{:04.4f}".format(u2, v2))
print("Estimated position  Literature 2    {:04.4f},{:04.4f}".format(x2, y2))
print("Estimated position  Our Algorithm 2 {:04.4f},{:04.4f}".format(x2_, y2_))
print("Error2                              {:04.4f}".format(error2[0]))
print("Error2_                             {:04.4f}".format(error2_[0]))


print(" "*50)
print(" "*50)

print("The Distance Equal to Five Meters")
print("="*50)
print("Real position: 3                    {:04.4f},{:04.4f}".format(u3, v3))
print("Estimated position  Literature  3   {:04.4f},{:04.4f}".format(x3, y3))
print("Estimated position  Our Algorithm 3 {:04.4f},{:04.4f}".format(x3_, y3_))
print("Error3                              {:04.4f}".format(error3[0]))
print("Error3_                             {:04.4f}".format(error3_[0]))


plt.plot(range(1, n), error1_, label="Tito's Algo 1m")
plt.plot(range(1, n), error1, label="Literature's Algo 1m")
plt.plot(range(1, n), error2_, label="Tito's Algo 3m")
plt.plot(range(1, n), error2, label="Literature's Algo 3m")
plt.plot(range(1, n), error3_, label="Tito's Algo 5m")
plt.plot(range(1, n), error3, label="Literature's Algo 5m")
plt.legend()
plt.xlabel("k Number")
plt.ylabel("Localization Error (cm)")
plt.show()




import matplotlib.pyplot as plt1
from Distance import Distance
from knn import KnN
from dataset import DataSet
import numpy as np
from results import Results
from results import SignalComparison



one_meter = "/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D1.txt"
three_meter = "/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D1.txt"





# The Tested Points
p1 = q1 = r1 = 1
p2 = q2 = r2 = 3
p3 = q3 = r3 = 5


# Data From The First Position
# Distance equal to one meter
am = DataSet("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D1.txt")
data1 = DataSet("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D1.txt").rssi_average()
print(data1)
data1_ = DataSet("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D1.txt").doc_opener()
# Distance equal to three meters
data2 = DataSet("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D1.txt").rssi_average()
data2_ = DataSet("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D1.txt").doc_opener()
# Distance equal to five meters
data3 = DataSet("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D1.txt").rssi_average()
data3_ = DataSet("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D1.txt").doc_opener()
# Real position 1
(u1, v1) = (p1 / 2, 0)
(u2, v2) = (p2 / 2, 0)
(u3, v3) = (p3 / 2, 0)


# # Data From the Second Position
# # Distance equal to one meter
# data1 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D2.txt")
# data1_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D2.txt")
# # Distance equal to three meters
# data2 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D2.txt")
# data2_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D2.txt")
# # Distance equal to five meters
# data3 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D2.txt")
# data3_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D2.txt")
# # Real position 2
# (u1, v1) = (p1 / 2, p1/2)
# (u2, v2) = (p2 / 2, p2/2)
# (u3, v3) = (p3 / 2, p3/2)


# # Data the Third Position
# # Distance equal to one meter
# data1 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D3.txt")
# data1_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/1D3.txt")
# # Distance equal to three meters
# data2 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D3.txt")
# data2_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/3D3.txt")
# # Distance equal to five meters
# data3 = DataSet().openerLit("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D3.txt")
# data3_ = DataSet().openerAlgo("/Users/SimahoJr/tito/rssi-dataset/dataset/environment1/ble/5D3.txt")
# # Real position 3
# (u1, v1) = (2 * p1 / 3, p1/3)
# (u2, v2) = (2 * p2 / 3, p2/3)
# (u3, v3) = (2 * p3 / 3, p3/3)


# Literature Algorithm
e1 = Distance(data1[0]).get_distance()
f1 = Distance(data1[1]).get_distance()
g1 = Distance(data1[2]).get_distance()
x1 = (pow(e1, 2) - pow(f1, 2) + pow(p1, 2)) / (2 * p1)
y1 = (pow(e1, 2) - pow(g1, 2) + pow(q1, 2) + pow(r1, 2)) / (2 * r1) - (q1 / r1) * x1

e2 = Distance(data2[0]).get_distance()
f2 = Distance(data2[1]).get_distance()
g2 = Distance(data2[2]).get_distance()
x2 = (pow(e2, 2) - pow(f2, 2) + pow(p2, 2)) / (2 * p2)
y2 = (pow(e2, 2) - pow(g2, 2) + pow(q2, 2) + pow(r2, 2)) / (2 * r2) - (q2 / r2) * x2

e3 = Distance(data3[0]).get_distance()
f3 = Distance(data3[1]).get_distance()
g3 = Distance(data3[2]).get_distance()
x3 = (pow(e3, 2) - pow(f3, 2) + pow(p3, 2)) / (2 * p3)
y3 = (pow(e3, 2) - pow(g3, 2) + pow(q3, 2) + pow(r3, 2)) / (2 * r3) - (q3 / r3) * x3


# Check this
# Our Algorithms
i = 1          # Set the k value
knn10 = KnN(data1_[0], i)
knn11 = KnN(data1_[1], i)
knn12 = KnN(data1_[2], i)
e11 = knn10.distAlgo()
f11 = knn11.distAlgo()
g11 = knn12.distAlgo()
x11 = (pow(e11, 2) - pow(f11, 2) + pow(p1, 2)) / (2 * p1)
y11 = (pow(e11, 2) - pow(g11, 2) + pow(q1, 2) + pow(r1, 2)) / (2 * r1) - (q1 / r1) * x11

knn20 = KnN(data2_[0], i)
knn21 = KnN(data2_[1], i)
knn22 = KnN(data2_[2], i)
e12 = knn20.distAlgo()
f12 = knn21.distAlgo()
g12 = knn22.distAlgo()
x22 = (pow(e12, 2) - pow(f12, 2) + pow(p2, 2)) / (2 * p2)
y22 = (pow(e12, 2) - pow(g12, 2) + pow(q2, 2) + pow(r2, 2)) / (2 * r2) - (q2 / r2) * x22

knn30 = KnN(data3_[0], i)
knn31 = KnN(data3_[1], i)
knn32 = KnN(data3_[2], i)
e13 = knn30.distAlgo()
f13 = knn31.distAlgo()
g13 = knn32.distAlgo()
x33 = (pow(e13, 2) - pow(f13, 2) + pow(p3, 2)) / (2 * p3)
y33 = (pow(e13, 2) - pow(g13, 2) + pow(q3, 2) + pow(r3, 2)) / (2 * r3) - (q3 / r3) * x33

x1_ = (knn10.knnAlgo() * 0 + knn11.knnAlgo() * p1 + knn12.knnAlgo() * q1) / \
      (knn10.knnAlgo() + knn11.knnAlgo() + knn12.knnAlgo())
y1_ = (knn10.knnAlgo() * 0 + knn11.knnAlgo() * 0 + knn12.knnAlgo() * r1) / \
      (knn10.knnAlgo() + knn11.knnAlgo() + knn12.knnAlgo())

x2_ = (knn20.knnAlgo() * 0 + knn21.knnAlgo() * p2 + knn22.knnAlgo() * q2) / \
      (knn20.knnAlgo() + knn21.knnAlgo() + knn22.knnAlgo())
y2_ = (knn20.knnAlgo() * 0 + knn21.knnAlgo() * 0 + knn22.knnAlgo() * r2) / \
      (knn20.knnAlgo() + knn21.knnAlgo() + knn22.knnAlgo())

x3_ = (knn30.knnAlgo() * 0 + knn31.knnAlgo() * p3 + knn32.knnAlgo() * q3) / \
      (knn30.knnAlgo() + knn31.knnAlgo() + knn32.knnAlgo())
y3_ = (knn30.knnAlgo() * 0 + knn31.knnAlgo() * 0 + knn32.knnAlgo() * r3) / \
      (knn30.knnAlgo() + knn31.knnAlgo() + knn32.knnAlgo())


# RESULTS

knn20.results()
knn10.results()
knn10.results()

a = "3m"
b = "5m"
c = "1m"
pos1 = Results(u1, v1, x1, y1, x1_, y1_, x11, y11, c)
pos2 = Results(u2, v2, x2, y2, x2_, y2_, x22, y22, a)
pos3 = Results(u3, v3, x3, y3, x3_, y3_, x33, y33, b)

am.rssi_filtered_avg()

pos1.printed_results()
pos2.printed_results()
pos3.printed_results()

# Comparison("", "").rs_comparison(knn10.distAlgo(), Distance(data1[0]).get_distance_ble_env1())

# pos1.error_graph()
# pos2.error_graph()
# pos3.error_graph()





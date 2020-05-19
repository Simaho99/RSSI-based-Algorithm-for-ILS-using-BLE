import matplotlib.pyplot as plt1
from Distance import Distance
from knn import KnN
from dataset import DataSet
import numpy as np
from results import Results
from results import SignalComparison
from weight import WeightCal
from results import DistanceComparison
from results import Hist
from correction import Correction
from results import ErrorVsDistance
import matplotlib.pyplot as plt

"""The environment of the algorithm together with the tested locations on different distances"""

# The environment
env = "2"                      # The environment is a string value

# The Tested Points
p1 = q1 = r1 = 1               # The parameters at distance equal to 1m
p3 = q3 = r3 = 3               # The parameters at distance equal to 3m
p5 = q5 = r5 = 5               # The parameters at distance equal to 5m

"""The following is the list of tested positions with their respective position
The aim is to open the respective datasets from the computer with their corresponding
 positions"""

# # Position D1
# DX = "D1"                       # Opens files corresponding to D1 (Position 1)
# (u1, v1) = (p1 / 2, 0)          # Position D1 coordinates at distance equal to one meter
# (u3, v3) = (p3 / 2, 0)          # Position D1 coordinates at distance equal to three meters
# (u5, v5) = (p5 / 2, 0)          # Position D1 coordinates at distance equal to five meters

# Position D2
DX = "D1"
(u1, v1) = (p1/2, p1/2)
(u3, v3) = (p3 / 2, p3 / 2)
(u5, v5) = (p5 / 2, p5 / 2)

# # Position D3
# DX = "D3"
# (u1, v1) = (2 * p1 / 3, p1/3)
# (u3, v3) = (2 * p3 / 3, p3 / 3)
# (u5, v5) = (2 * p5 / 3, p5 / 3)

# Opens the required files and assigns to the variable depends on the position "DX"
one_meter = "/Users/SimahoJr/tito/rssi-dataset/dataset/environment"+env+"/ble/1"+DX+".txt"
thr_meters = "/Users/SimahoJr/tito/rssi-dataset/dataset/environment"+env+"/ble/3"+DX+".txt"
five_meters = "/Users/SimahoJr/tito/rssi-dataset/dataset/environment"+env+"/ble/5"+DX+".txt"

"""The variables below (rs_Xm) takes a list of three lists of RSSI values which signifies a list of RSSI values
from the three nodes. For A, B, C being a list of RSSI from a respective node at particular distance,
 the value returns [A, B, C]"""

rs_1m = DataSet(one_meter)
rs_3m = DataSet(thr_meters)
rs_5m = DataSet(five_meters)

# Calculated the distance according to the developed RSSI-Distance Model by the author
dist = Distance()

# Literature Algorithm
"""The Corrected RSSI values"""

"""The averaged (float) values of RSSI according to the literature
The value takes a list of three averaged RSSI values from each node for a 
particular distance"""
rs_1m_lit_sort = rs_1m.rssi_average()
rs_3m_lit_sort = rs_3m.rssi_average()
rs_5m_lit_sort = rs_5m.rssi_average()

"""The specific RSSI values are now taken from the list for tri-lateration approach"""
rs1_0 = rs_1m_lit_sort[0]
rs1_1 = rs_1m_lit_sort[1]
rs1_2 = rs_1m_lit_sort[2]
rs3_0 = rs_3m_lit_sort[0]
rs3_1 = rs_3m_lit_sort[1]
rs3_2 = rs_3m_lit_sort[2]
rs5_0 = rs_5m_lit_sort[0]
rs5_1 = rs_5m_lit_sort[1]
rs5_2 = rs_5m_lit_sort[2]


"Trilateration Algorithm"
# One meter
e1 = dist.get_distance_ble(rs1_0, env)
f1 = dist.get_distance_ble(rs1_1, env)
g1 = dist.get_distance_ble(rs1_2, env)
x1 = (pow(e1, 2) - pow(f1, 2) + pow(p1, 2)) / (2 * p1)
y1 = (pow(e1, 2) - pow(g1, 2) + pow(q1, 2) + pow(r1, 2)) / (2 * r1) - (q1 / r1) * x1
# Three meters
e2 = dist.get_distance_ble(rs3_0, env)
f2 = dist.get_distance_ble(rs3_1, env)
g2 = dist.get_distance_ble(rs3_2, env)
x2 = (pow(e2, 2) - pow(f2, 2) + pow(p3, 2)) / (2 * p3)
y2 = (pow(e2, 2) - pow(g2, 2) + pow(q3, 2) + pow(r3, 2)) / (2 * r3) - (q3 / r3) * x2
# Five meters
e3 = dist.get_distance_ble(rs5_0, env)
f3 = dist.get_distance_ble(rs5_1, env)
g3 = dist.get_distance_ble(rs5_2, env)
x3 = (pow(e3, 2) - pow(f3, 2) + pow(p5, 2)) / (2 * p5)
y3 = (pow(e3, 2) - pow(g3, 2) + pow(q5, 2) + pow(r5, 2)) / (2 * r5) - (q5 / r5) * x3


# The developed algorithm
"""The Corrected RSSI values"""
i = 1                           # Relates to the percentiles selection on the population
rs1_0_ = Correction(rs_1m.rssi_raw()[0], i).correction()
rs1_1_ = Correction(rs_1m.rssi_raw()[1], i).correction()
rs1_2_ = Correction(rs_1m.rssi_raw()[2], i).correction()
rs3_0_ = Correction(rs_3m.rssi_raw()[0], i).correction()
rs3_1_ = Correction(rs_3m.rssi_raw()[1], i).correction()
rs3_2_ = Correction(rs_3m.rssi_raw()[2], i).correction()
rs5_0_ = Correction(rs_5m.rssi_raw()[0], i).correction()
rs5_1_ = Correction(rs_5m.rssi_raw()[1], i).correction()
rs5_2_ = Correction(rs_5m.rssi_raw()[2], i).correction()

"Same Trilateration Algorithm"
# One meter
e11 = dist.get_distance_ble(rs1_0_, env)
f11 = dist.get_distance_ble(rs1_1_, env)
g11 = dist.get_distance_ble(rs1_2_, env)
x11 = (pow(e11, 2) - pow(f11, 2) + pow(p1, 2)) / (2 * p1)
y11 = (pow(e11, 2) - pow(g11, 2) + pow(q1, 2) + pow(r1, 2)) / (2 * r1) - (q1 / r1) * x1
# Three meters
e22 = dist.get_distance_ble(rs3_0_, env)
f22 = dist.get_distance_ble(rs3_1_, env)
g22 = dist.get_distance_ble(rs3_2_, env)
x22 = (pow(e22, 2) - pow(f22, 2) + pow(p3, 2)) / (2 * p3)
y22 = (pow(e22, 2) - pow(g22, 2) + pow(q3, 2) + pow(r3, 2)) / (2 * r3) - (q3 / r3) * x2
# Five meters
e33 = dist.get_distance_ble(rs5_0_, env)
f33 = dist.get_distance_ble(rs5_1_, env)
g33 = dist.get_distance_ble(rs5_2_, env)
x33 = (pow(e33, 2) - pow(f33, 2) + pow(p5, 2)) / (2 * p5)
y33 = (pow(e33, 2) - pow(g33, 2) + pow(q5, 2) + pow(r5, 2)) / (2 * r5) - (q5 / r5) * x3


"""This section displays different results for performance evaluations between the two algorithms"""
# Printing results on a file/screen
# Set parameters for each position
a = "3m"
b = "5m"
c = "1m"
# Objects at their respective distances
d1 = Results(u1, v1, x1, y1, x11, y11, c)
d3 = Results(u3, v3, x2, y2, x22, y22, a)
d5 = Results(u5, v5, x3, y3, x33, y33, b)

# Printing results on the Screen
# d1.printed_results()
# d3.printed_results()
# d5.printed_results()


# Printing to a file for further calculations
# For tables creation
# print(d1.error, d1.error1, d3.error, d3.error1, d5.error, d5.error1, sep="_", file=open("sum.txt", "a"))

# Plotting the error graphs
# d1.error_graph()
# d3.error_graph()
# d5.error_graph()


# Plot localization error vs distance on a single position for the two algorithms
# ErrorVsDistance().error_vs_distance(d1.error, d3.error, d5.error, d1.error1, d3.error1, d5.error1)


a = rs_5m.rssi_raw_[0]
b = rs_5m.rssi_filtered_[0]

print(a)
print(b)


plt.plot(range(0, len(a)), a, label="Raw")
plt.plot(range(0, len(b)), b, label="Corrected")
# plt.plot(range(0, len(self.dist_filtered)), b, "-ro", label="Actual Distance")
plt.legend()
plt.xlabel("Sequence Number")
plt.ylabel("RSSI")
plt.show()

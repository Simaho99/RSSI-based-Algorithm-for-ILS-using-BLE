import math
from Distance import Distance
import numpy as np


class DataSet(object):
    def __init__(self, halo):
        self.halo = halo
        self.rs_filtered_avg = []
        self.a_ = []
        self.b_ = []
        self.c_ = []
        self.rs_ = []
        self.rssi_read = []
        self.rssi_filtered_ = []
        self.rssi_raw_ = []
        self.rs_gaussian_all = []
        self.k = 1

    def doc_opener(self):
        self.a_.clear()
        self.b_.clear()
        self.c_.clear()
        self.rssi_read.clear()

        with open(self.halo) as rssiValues:
            for line in rssiValues:
                if line[5] == "A":
                    self.a_.append(int(line[9] + line[10]))

                if line[5] == "B":
                    self.b_.append(int(line[9] + line[10]))

                if line[5] == "C":
                    self.c_.append(int(line[9] + line[10]))

        return [self.a_, self.b_, self.c_]

    def rssi_filtered_avg(self):  # rs is the integer valued list of the RSSIs
        self.rssi_raw_.clear()
        self.rs_filtered_avg.clear()
        self.rssi_filtered_.clear()
        self.rs_gaussian_all.clear()

        for i in range(0, len(self.doc_opener())):
            rs = []
            rs_filtered = []
            rs_filtered1 = []
            rs_gaussian = []
            rs_var = 0

            for j in range(0, len(self.doc_opener()[i])):
                rs_change = -1 * self.doc_opener()[i][j]  # collected from a single node
                rs.append(rs_change)

            self.rssi_raw_.append(rs)

            # Calculate the mean and standard deviation of the rs
            rs_mean = sum(rs) / len(rs)  # mean value

            a_sorted = sorted(rs)

            for m in range(0, len(rs)):
                rs_var = rs_var + (1 / (len(rs) - 1)) * (pow((rs[m] - rs_mean), 2))

            rs_std = pow(rs_var, 0.5)  # standard deviation

            # Gaussian Filtered values
            for m in range(0, len(rs)):  # removing outliers
                rs_gaussian.append((1 / (rs_std * pow(2 * math.pi, 0.5))) *
                                    (pow(math.e, - (pow((a_sorted[m] - rs_mean), 2)))) / (2 * rs_var))
                a = -abs(rs_mean - self.k * rs_std)
                b = -abs(rs_mean + self.k * rs_std)

                if abs(rs[m]-rs_mean) > self.k*rs_std:
                    rs_filtered.append(rs[m])
                    rs_filtered1.append(rs[m])
                else:
                    rs_filtered.append(rs_mean)

            self.rssi_filtered_.append(rs_filtered)

            # print(len(self.rssi_raw_))

            amf = sum(rs_filtered)/len(rs_filtered)
            self.rs_filtered_avg.append(amf)
            self.rs_gaussian_all.append(rs_gaussian)

        # print(np.corrcoef(self.rssi_raw_[0], self.rssi_filtered_[0]))

        return self.rs_filtered_avg

    def rssi_average(self):
        self.doc_opener()
        A_rssi = sum(self.a_)/len(self.a_)
        B_rssi = sum(self.b_)/len(self.b_)
        C_rssi = sum(self.c_)/len(self.c_)

        return [A_rssi * -1, B_rssi * -1, C_rssi * -1]

    def rssi_filtered(self):
        self.rssi_filtered_avg()

        return self.rssi_filtered_

    def rssi_raw(self):
        self.rssi_filtered_avg()

        return self.rssi_raw_

    def gaussian_pdf(self):
        self.rssi_filtered_avg()

        return self.rs_gaussian_all

    def correlation(self):
        self.rssi_filtered_avg()
        print(np.correlate(self.rssi_raw_, self.rssi_filtered_))

        return np.correlate(self.rssi_raw_, self.rssi_filtered_)

    def rssi_mean(self):
        self.rssi_filtered_avg()

        return sum(self.rssi_raw_)/len(self.rssi_raw_)  #returns the mean value of the raw rssi

    def rssi_median(self):
        self.rssi_filtered_avg()
        medium_var = 0                      # the variable to store the medium value

        m = sorted(self.rssi_raw_)          # m contains the set of sorted rssi in decreasing order
        for i in range(0, len(m)):
                                            # Check for even and odd RSSI
            if len(m) % 2 is 1:  # If odd
                b = int((len(m) + 1) / 2)
                medium_var = m[b]
            else:                           # Else even
                b = int(len(m) / 2)
                medium_var = m[b]

        return medium_var                   # Return the medium value








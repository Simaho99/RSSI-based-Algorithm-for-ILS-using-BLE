from Distance import Distance
import math
import numpy as np
import matplotlib.pyplot as plt
from results import Results
from results import SignalComparison

class KnN(object):

    def __init__(self, rs, k):
        self.dist = 0
        self.rs = rs
        self.k = k
        self.dist1 = 0

        self.rs_filtered = []
        self.cf = []
        self.cf_ = []
        self.snr_ = []
        self.diff = []
        self.cf2 = []

        self.rs_var = 0  # variance value
        self.rs_fit = []

        self.rs_std = 0
        self.rs_mean = 0
        self.rs_mean_fil = 0
        self.rs_ = []
        self.a = []
        self.b = []
        self.rs_tot = []

    def knnAlgo(self):                                  # rs is the integer valued list of the RSSIs

        self.rs_.clear()
        # self.diff.clear()
        self.rs_filtered.clear()
        # self.snr_.clear()
        self.a.clear()
        self.b.clear()
        self.cf_.clear()
        self.rs_tot.clear()
        self.rs_.clear()


        for i in range(0, len(self.rs)):
            rs_change = -1 * self.rs[i]                           # collected from a single node
            self.rs_.append(rs_change)

    # Calculate the mean and standard deviation of the rs
        self.rs_mean = sum(self.rs_)/len(self.rs_)                         # mean value

        for i in range(0, len(self.rs_)):
            self.rs_var = self.rs_var + (1/(len(self.rs_)-1)) * (pow((self.rs_[i] - self.rs_mean), 2))
        self.rs_std = pow(self.rs_var, 0.5)                         # standard deviation

    # Gaussian Filtered values
        for i in range(0, len(self.rs_)):
            rs_new = (1 / (self.rs_std * pow(2 * math.pi, 0.5))) * \
                          pow(math.e, - (pow((self.rs_[i] - self.rs_mean), 2)) / (2 * self.rs_var))
            self.rs_fit.append(rs_new)

        for i in range(0, len(self.rs_)):                # removing outliers
            rs1 = self.rs_[i]
            a = self.rs_mean - self.k*self.rs_std
            b = self.rs_mean + self.k*self.rs_std
            if (rs1 > a) and (rs1 < b):
                self.rs_filtered.append(rs1)
            elif rs1 < a:
                self.rs_filtered.append(a)
            elif rs1 > b:
                self.rs_filtered.append(b)

        for i in range(0, len(self.rs_filtered)):
            rs_dist = Distance(self.rs_filtered[i]).get_distance()
            self.cf.append(-self.rs_filtered[i]/rs_dist)

        for i in range(0, len(self.rs_filtered)):
            rs_dist = Distance(self.rs_filtered[i]).get_distance()
            self.cf2.append(1/rs_dist)

        self.rs_mean_fil = sum(self.rs_filtered) / len(self.rs_filtered)

        for i in range(0, len(self.rs_)):
            self.snr_ = self.rs_[i] / self.rs_var                                      # Signal to noise ratio
            self.diff = self.rs_[i] - self.rs_filtered[i]
            self.cf_.append(np.convolve(self.snr_, self.diff, "valid"))


            # Differential relationship
            # between the filtered
        #
                                             # and the current read
        #                                                                          # Correction Factor CF
        # cf_avg = sum(cf_)/len(cf_)
        #
        # # print(rs_filtered)
        # print(diff)
        # print(snr)
        # print(self.cf_)

        for i in range(0, len(self.rs_filtered)):
            self.rs_tot.append(sum(self.rs_[i] + self.cf_[i])/len(self.rs_filtered[i]-self.cf_[i]))

        # self.dist1 = Distance(cf_avg).getDistance()

        a = sum(self.rs_tot)/len(self.rs_tot)

        self.dist = Distance().get_distance(self.rs_mean_fil)
        self.a.append(self.rs_mean_fil)
        self.b.append(a)

        return a

    def distAlgo(self):
        self.knnAlgo()

        return self.dist

    def snr(self):
        self.knnAlgo()

        return self.snr_

    def filtered_rs(self):
        self.knnAlgo()

        return self.rs_filtered

    def raw_rs(self):
        self.knnAlgo()

        return self.rs

    def results(self):
        # Comparison("RSSI Raw", "RSSI Filtered").rs_comparison(self.rs_, self.rs_filtered)
        # Comparison("RSSI Raw", "RSSI CF").rs_comparison(self.rs_, self.rs_tot)
        # Comparison("RSSI Filtered", "RSSI CF").rs_comparison(self.rs_filtered, self.rs_tot)
        print("hallo")




import math
from Distance import Distance
import numpy as np
from dataset import DataSet


class WeightCal(object):

    def __init__(self):
        self.rs = 0

    @staticmethod
    def weighted(rs_fil, rs_raw):

        diff = rs_raw - rs_fil

        if diff == 0:                                  # Sometimes the filtered is equal to the raw value
            diff = 1

        snr = rs_raw/(rs_raw)

        cf = np.convolve(diff, snr, "valid")           # Check dimensions

        d = Distance().get_distance(rs_fil)
        d1 = Distance().get_distance(diff)    # Dimensioning again

        return rs_fil/d                                # Need Rechecking

    def weight_median_based(self, halo, k):

        a = DataSet(halo, k).rssi_filtered_

    # Sort the RSSI values from each node, from node a to node c
        node_a = sorted(a[0])
        node_b = sorted(a[1])
        node_c = sorted(a[2])

    # Find the RSSI  medium set for each node
    # find the length 'n' of the set
    # "t" is the length of the new developed set
    # if the length of the set is equal to odd then use t =(n+1)/2
    # if the length of the set is even then use the formula t = n/2
    # So
    #     medium = []                             # This will contain three median values
    #     m = [node_a, node_b, node_c]
    #     for i in range(0, len(m)):
    #         # Check for even and odd RSSI
    #         a = [i]
    #         if len(a) % 2 is 1:                 # If odd
    #             b = int((len(a) + 1)/2)
    #             medium.append(a[b])
    #         else:                               # Else even
    #             b = int(len(a)/2)
    #             medium.append(a[b])






# Check for the distance
#     may be we should fix one rssi value vs distance and use it
#     for correcting other rssi values, and not convolution
#     let pick the rssi average value for one meter distance as our reference
#     buth this will be correnting the
#     if distance and not rssi in such:
#
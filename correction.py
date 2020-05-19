
"""correction of raw RSSI values to get more meaningful RSSI value
to help to increase the accuracy of the entire algorithm
The class takes the one value of the raw RSSI from particular node and estimates
the median and the mean value of the given RSSI values
the class estimates the relationship before applying the gaussian filter type
different types of gaussian filters used, depending on the nature of the distribution
and the prior knowledge of the RSSI experiments"""

import numpy as np
import statistics as st
from scipy import stats

class Correction(object):

    def __init__(self, raw, k):                 # The RSSI raw list is input for this instance
        self.raw = raw
        self.std = 0
        self.var = 0
        self.k = k                              # K signify the percentiles on the sample

    def mean(self):
        return sum(self.raw)/len(self.raw)      # Returns the mean value of the list

    def stats(self):
        self.var = 0  # The variance variable
        self.std = 0  # Standard deviation

        for m in range(0, len(self.raw)):
            self.var = self.var + (1 / (len(self.raw) - 1)) * (pow((self.raw[m] - self.mean()), 2))

        self.std = pow(self.var, 0.5)

    def median(self):
        medium_var = 0                          # The variable to store the medium value
        m = sorted(self.raw)                    # m contains the set of sorted rssi in decreasing order
        for i in range(0, len(m)):
                                                # Check for even and odd RSSI
            if len(m) % 2 is 1:  # If odd
                b = int((len(m) + 1) / 2)
                medium_var = m[b]
            else:                               # Else even
                b = int(len(m) / 2)
                medium_var = m[b]
        return medium_var                       # Return the medium value of the list

    def mode(self):
        a = []
        m = sorted(self.raw)
        for i in range(0, len(m)):
            a.append(int(m[i]))

        m = stats.mode(a)

        return m[0]                     # Return the medium value of the list

    def high_pass(self):
        self.stats()
        corrected = []
        for m in range(0, len(self.raw)):
            if self.raw[m] - self.mean() < -self.k * self.std:
                corrected.append(self.raw[m])
            else:
                corrected.append(self.mean())
        return corrected

    def low_pass(self):
        self.stats()
        corrected = []
        for m in range(0, len(self.raw)):
            if self.raw[m] - self.mean() < self.k * self.std:
                corrected.append(self.raw[m])
            else:
                corrected.append(self.mean())
        return corrected

    def band_pass(self):
        self.stats()
        corrected = []

        for m in range(0, len(self.raw)):
            if (self.k * self.std) < (self.raw[m] - self.mean()) < (self.k * self.std):                   # Band pass
                corrected.append(self.raw[m])
            else:
                corrected.append(self.mean())

        return corrected

    def correction(self):
        self.stats()

        """The relationship between the median value and the mean value gives us the type of gaussian
        filter to use there are three values to be tested, which are positive, negative and zero
        we put some uncertainty in comparison because we understand the values can not be the exactly the
        same"""

        diff = abs(self.median() - self.mean())
        c = 0                                     # Uncertainty factor, plus or minus like width
        corrected = []

        print(diff)
        print("median ", self.median())
        print("mean ", self.mean())
        print(self.std)
        print(self.mode())

        if self.mean() > self.median() > self.mode():            # Skewed to the right as the median is greater than the mean
            '''High Pass Filter'''
            # if self.median() - self.mean() >= c:
            corrected = self.high_pass()
            print("High Pass")

        elif self.mean() < self.median() < self.mode():         # Skewed to the left as the median is less than the mean value
                '''Low Pass Filter'''
                # if self.median() - self.mean() <= c:
                corrected = self.low_pass()
                print("Low Pass")

        else:                      # If they are perfectly symmetrical
            '''Band Pass Filter'''
            corrected = self.band_pass()
            print("Band Pass")

        return sum(corrected)/len(corrected)          # Returns averaged corrected value

import numpy as np
import matplotlib.pyplot as plt
from Distance import Distance
from scipy.stats import norm


class Results(object):

    def __init__(self, u, v, x1, y1, x11, y11, a):
        self.a = a
        self.u = u
        self.v = v
        self.error = 0
        self.error_ = 0
        self.error1 = 0
        self.x1 = x1
        self.y1 = y1
        self.x11 = x11
        self.y11 = y11

    def printed_results(self):

        self.error = pow((pow((self.x1 - self.u), 2) + pow((self.y1 - self.v), 2)), 0.5)
        self.error1 = pow((pow((self.x11 - self.u), 2) + pow((self.y11 - self.v), 2)), 0.5)

        p1 = ((self.error - self.error1) / self.error) * 100
        p = ((self.error - self.error_)/self.error)*100

        print("=" * 50)
        print("Real position with {} Distance                   {:04.4f} m, {:04.4f} m".format(self.a, self.u, self.v))
        print("Estimated Location Literature:                   {:04.4f} m, {:04.4f} m".format(self.x1, self.y1))
        print("Estimated Location  Developed: Corrected         {:04.4f} m, {:04.4f} m".format(self.x11, self.y11))
        print("Error: Literature                                {:04.4f} m".format(self.error))
        print("Error: Developed (Corrected)                     {:04.4f} m".format(self.error1))
        # print("Error: Developed (Weighted)                      {:04.4f} m".format(self.error_),file=open(m, "a"))
        print("Percentage: Filtered (w.r.t Literature)          {:04.4f}%".format(p1))
        # print("Percentage: Weighted (w.r.t Literature)          {:04.4f}%".format(p))

    def printed_results_file(self):

        self.error = pow((pow((self.x1 - self.u), 2) + pow((self.y1 - self.v), 2)), 0.5)
        self.error1 = pow((pow((self.x11 - self.u), 2) + pow((self.y11 - self.v), 2)), 0.5)

        p1 = ((self.error - self.error1) / self.error) * 100
        p = ((self.error - self.error_)/self.error)*100

        m = "tito.txt"

        print("=" * 50)
        print("Real position with {} Distance                   {:04.4f} m, {:04.4f} m".format(self.a, self.u, self.v),
              file=open(m, "a"))
        print("Estimated Location Literature:                   {:04.4f} m, {:04.4f} m".format(self.x1, self.y1)
              , file=open(m, "a"))
        print("Estimated Location  Developed: Corrected         {:04.4f} m, {:04.4f} m".format(self.x11, self.y11)
              , file=open(m, "a"))
        print("Error: Literature                                {:04.4f} m".format(self.error), file=open(m, "a"))
        print("Error: Developed (Corrected)                     {:04.4f} m".format(self.error1), file=open(m, "a"))
        # print("Error: Developed (Weighted)                      {:04.4f} m".format(self.error_),file=open(m, "a"))
        print("Percentage: Corrected (w.r.t Literature)         {:04.4f}%".format(p1), file=open(m, "a"))
        # print("Percentage: Weighted (w.r.t Literature)          {:04.4f}%".format(p), file=open(m, "a")))

    def error_graph(self):

        label = ["Literature", "Developed Corrected"]
        errors = [self.error, self.error1]
        index = np.arange(len(label))
        plt.bar(index, errors, label='', width=0.5, color=['blue', 'yellow'])
        # plt.bar(index, errors, label=self.a, color=['black', 'red', 'green'])
        plt.xticks(index, label)

        plt.xlabel("Algorithms")
        plt.ylabel("Localization Error (cm)")
        plt.title("Localization Errors at Distance Equal to " + self.a)
        plt.legend()

        plt.tight_layout()
        plt.show()


class SignalComparison(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rs_comparison(self, raw, filtered):
        plt.plot(range(0, len(raw)), raw, label=self.a)
        plt.plot(range(0, len(filtered)), filtered, label=self.b)
        plt.legend()
        plt.xlabel("Sequence Number")
        plt.ylabel("RSSI(dBm)")
        plt.title(self.c)
        plt.show()


class DistanceComparison(object):

    def __init__(self, rs_raw, rs_filtered, alli):
        self.rs_raw = rs_raw
        self.rs_filtered = rs_filtered
        self.dist_raw = []
        self.dist_filtered = []
        self.alli = alli

    def distances_graph(self):
        b = []
        self.dist_raw.clear()
        self.dist_filtered.clear()

        for i in range(0, len(self.rs_raw)):
            dist = Distance.get_distance(self.rs_raw[i])
            self.dist_raw.append(dist)

        for i in range(0, len(self.rs_filtered)):
            dist = Distance.get_distance(self.rs_filtered[i])
            self.dist_filtered.append(dist)

        for i in range(0, len(self.rs_filtered)):
            b.append(self.alli)

        plt.plot(range(0, len(self.dist_raw)), self.dist_raw, label="Raw")
        plt.plot(range(0, len(self.dist_filtered)), self.dist_filtered, label="Filtered")
        # plt.plot(range(0, len(self.dist_filtered)), b, "-ro", label="Actual Distance")
        plt.legend()
        plt.xlabel("Sequence Number")
        plt.ylabel("Distance")
        plt.title(self.alli)
        plt.show()

    def distances(self):
        self.distances_graph()

        avg_raw = sum(self.dist_raw)/len(self.dist_raw)
        avg_filtered = sum(self.dist_filtered)/len(self.dist_filtered)

        return [avg_raw, avg_filtered]




class Hist(object):

    def __init__(self, a):
        self.a = a

    def plot(self):
        sigma = 0
        mean = sum(self.a)/len(self.a)                                  # Mean Value
        for i in range(0, len(self.a)):
            sigma = sigma + ((1/(1-len(self.a)))*pow(mean-self.a[i], 2))    # Standard Deviation
        m = []
        z = []
        m.clear()

        m.append(mean)
        for i in range(1, 10):
            m.append(mean + i*sigma)
            m.insert(0, mean - i*sigma)

        m.sort()

        for i in range(0, len(self.a)):
            z.append((self.a[i]-mean)/pow(abs(sigma), 0.5))

        print(mean)

        plt.hist(z, bins=np.linspace(-5, 5, 19), density=True, rwidth=0.96)
        a = np.arange(-4, 4, 0.001)
        plt.plot(a, norm.pdf(a))
        plt.ylabel("PDF")
        plt.xlabel("RSSI Distribution")

        plt.show()


class ErrorVsDistance(object):

    def __init__(self):
        self.a = 0

    @staticmethod
    def error_vs_distance(a, b, c, d, e, f):
        err_lst = [a, b, c]
        err_lst1 = [d, e, f]
        dist_lst = [1, 3, 5]

        plt.plot(dist_lst, err_lst, "-ro", label="Literature")
        plt.plot(dist_lst, err_lst1, "-bo", label="Proposed")
        # plt.plot(range(0, len(self.dist_filtered)), b, "-ro", label="Actual Distance")
        plt.legend()
        plt.xlabel("Distance (m)")
        plt.ylabel("Localization Error (m)")
        plt.show()





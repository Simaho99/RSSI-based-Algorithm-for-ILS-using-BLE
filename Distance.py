import math


class Distance(object):

    def __init__(self):
        self.m = 0

    @staticmethod
    def get_distance_ble(m, env):
        distance_modeled = 0
        if env == "1":
            distance_modeled = math.pow(10, ((-75.54 - m) / 25.11))      # Environment 1
        if env == "2":
            distance_modeled = math.pow(10, ((-75.48 - m) / 22.71))      # Environment 2

        return distance_modeled





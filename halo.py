from scipy.stats import zscore
import numpy as np

# print(zscore([5, 1, 3]))
#
# print(np.linspace(1, 10, 4))
#
#
# p = 23.33
#
# print(int(p))

import numpy as np
from scipy import stats

a = [1, 3, 4, 2, 2, 7]

m = stats.mode(a)

print(max(m))
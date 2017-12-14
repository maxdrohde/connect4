import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2)
wins = [int(b1_wins),int(b2_wins)]



fig, ax = plt.subplots()
plt.bar(x, wins)
plt.xticks(x, (bot1.name,bot2.name))
plt.show()

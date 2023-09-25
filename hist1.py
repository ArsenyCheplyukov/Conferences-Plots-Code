import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read data and convert it to number
# data = input("Введите данные через пробел: ").split()
# data = [float(x) for x in data]
# data = np.array(
#     [
#         2.9637708649,
#         2.9260299625,
#         2.9227459783,
#         2.9337213669,
#         2.9514544768,
#         2.9503398792,
#         2.9326201201,
#         2.9205607477,
#         2.9162000747,
#         2.9162000747,
#         2.9140246177,
#         2.9784597789,
#         2.9096834264,
#         2.9227459783,
#         2.9458898944,
#         2.9414533133,
#         2.9370300752,
#         2.9403462552,
#     ]
# )

# data = (8 / 1024) / np.array(
#     [
#         0.002127,
#         0.002905,
#         0.002113,
#         0.002915,
#         0.002097,
#         0.002899,
#         0.002118,
#         0.002904,
#         0.002116,
#         0.002892,
#         0.002126,
#         0.002906,
#         0.002117,
#         0.002889,
#         0.002118,
#         0.002910,
#         0.002106,
#         0.002897,
#         0.002157,
#     ]
# )

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("FreeRTOS+Cache.csv")
# Select the second column (assuming it's called "parameter")
param_col = df["Time"]
# Compute the delta between each row and the next
delta = np.diff(param_col)
# Filter out any delta values less than 1
data = 8 / 1024 / delta[delta <= 1]
# Print the filtered delta values
print(data)

mean = np.mean(data)  # 0.45 *
std = np.std(data)  # 0.6 *

data = np.array([x if (x > 6.5 and x < 7.75) else 0 for x in data])
data = data[data > 7.1]

mean = np.mean(data)  # 0.45 *
std = np.std(data)  # 0.6 *

print(mean, std)

# generate 100 numbers from gauss destribution
# points = [x if x > 0.1 * mean and x < 1.7 * mean else mean for x in np.random.normal(mean, std, 330)] * 8

plt.hist(data, bins=20, density=False)

plt.xlabel("Пропускная способность, Мбит/с")
# plt.ylabel("Частота")
# plt.title("Пропускная способность модуля w5500 сети Ethernet с DMA")
plt.title("Пропускная способность модуля w5500 сети Ethernet без DMA")

plt.rcParams.update({"font.size": 14, "font.family": "Times New Roman"})
plt.tick_params(labelsize=14, width=2, length=5)

plt.grid(True, linestyle="--", linewidth=0.5)

plt.show()

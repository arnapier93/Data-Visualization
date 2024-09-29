import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

# the -1 accounts for the index 0 location
data_len = len(data) - 1
# initialize counters
num_stat = 0
num_pix = 0
num_vids = 0
num_linx = 0

# loops over the data taking 1 column as a new array for easier use
for i in range(1, data_len):
    status_type = data[i][1]
    match status_type:
        case "video":
            num_vids += 1
        case "photo":
            num_pix += 1
        case "link":
            num_linx += 1
        case "status":
            num_stat += 1

print("videos ", num_vids)
print("photos ", num_pix)
print("links ", num_linx)
print("statuses ", num_stat)

plt.style.use('_mpl-gallery-nogrid')

# assign values for a pie chart
x = [num_vids, num_pix, num_linx, num_stat]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot pie chart
fig, ax = plt.subplots(figsize=(6, 4))
ax.pie(x, labels=["Videos", "Photos", "Links", "Statuses"], colors=colors, radius=1, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False)


# show pie chart
plt.show()

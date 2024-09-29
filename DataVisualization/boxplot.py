import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

# the -1 accounts for the index 0 location
data_len = len(data) - 1
# initialize counters
num_vids = 0
num_pix = 0
num_linx = 0
num_stat = 0

for i in range(1, data_len):
    status_type = data[i][1]        # first column after index is type of post
    match status_type:
        case "video":
            num_vids += 1
        case "photo":
            num_pix += 1
        case "link":
            num_linx += 1
        case "status":
            num_stat += 1

num_oth = num_stat + num_linx

# generates blank matrices
videos = np.array([[0, 0, 0] for x in range(num_vids)])
photos = np.array([[0, 0, 0] for x in range(num_pix)])
other = np.array([[0, 0, 0] for x in range(num_oth)])

# indexes
v = p = o = 0

for i in range(1, data_len):
    status_type = data[i][1]        # first column after index is type of post
    match status_type:
        case "video":
            videos[v][0] = data[i][3]
            videos[v][1] = data[i][4]
            videos[v][2] = data[i][5]
            v += 1
        case "photo":
            photos[p][0] = data[i][3]
            photos[p][1] = data[i][4]
            photos[p][2] = data[i][5]
            p += 1
        case "link":
            other[o][0] = data[i][3]
            other[o][1] = data[i][4]
            other[o][2] = data[i][5]
            o += 1
        case "status":
            other[o][0] = data[i][3]
            other[o][1] = data[i][4]
            other[o][2] = data[i][5]
            o += 1

labels = ['Reactions', 'Comments', 'Shares']

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

bplot1 = ax1.boxplot(videos,
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
ax1.set_title('Videos')

bplot2 = ax2.boxplot(photos,
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
ax2.set_title('Photos')

bplot3 = ax3.boxplot(other,
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
ax3.set_title('Other')


# fill with colors
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, 3))
for bplot in (bplot1, bplot2, bplot3):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

# adding horizontal grid lines
for ax in [ax1, ax2, ax3]:
    ax.yaxis.grid(True)

plt.show()

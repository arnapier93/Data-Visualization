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

reactions = comments = shares = 0

for i in range(num_vids):
    comments += videos[i][0]
    reactions += videos[i][1]
    shares += videos[i][2]

cpv = comments / num_vids
rpv = reactions / num_vids
spv = shares / num_vids

reactions = 0
comments = 0
shares = 0

for i in range(num_pix):
    comments += photos[i][0]
    reactions += photos[i][1]
    shares += photos[i][2]

cpp = comments / num_pix
rpp = reactions / num_pix
spp = shares / num_pix

reactions = 0
comments = 0
shares = 0

for i in range(num_oth):
    comments += other[i][0]
    reactions += other[i][1]
    shares += other[i][2]

cpo = comments / num_oth
rpo = reactions / num_oth
spo = shares / num_oth

print(rpv, spv, cpv)
print(rpp, spp, cpp)
print(rpo, spo, cpo)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

bars = ['Reactions', 'Comments', 'Shares']
bar_colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, 3))

v_counts = [rpv, cpv, spv]
p_counts = [rpp, cpp, spp]
o_counts = [rpo, cpo, spo]

ax1.bar(bars, v_counts, color=bar_colors)
ax1.set_ylabel('Average per post')
ax1.set_title('Interactions with Videos')

ax2.bar(bars, p_counts, color=bar_colors)
ax2.set_title('Interactions with Photos')

ax3.bar(bars, o_counts, color=bar_colors)
ax3.set_title('Interactions with Other Posts')

plt.show()

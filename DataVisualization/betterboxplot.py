import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

# initialize counters
num_vids = num_pix = num_linx = num_stat = 0

# loops through data and counts types of posts
for i in range(1, len(data)):
    post_type = data[i][1]        # first column after index is type of post
    match post_type:
        case "video":
            num_vids += 1
        case "photo":
            num_pix += 1
        case "link":
            num_linx += 1
        case "status":
            num_stat += 1

# status and links to small to judge on their own
num_oth = num_stat + num_linx

# generates blank matrices
videos = np.array([[0, 0, 0] for x in range(num_vids)])
photos = np.array([[0, 0, 0] for x in range(num_pix)])
other = np.array([[0, 0, 0] for x in range(num_oth)])

# indexes
v = p = o = 0

for i in range(1, len(data)):
    post_type = data[i][1]        # first column after index is type of post
    match post_type:
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

print(len(data))
print(num_vids, "+", num_pix, "+", num_oth)
print(num_vids + num_pix + num_oth)

print('videos', len(videos), 'photos', len(photos), 'other', len(other))

viral_v = videos
dud_v = videos

viral_p = photos
dud_p = photos

viral_o = other
dud_o = other

print('viral', len(viral_v), 'vs duds', len(dud_v))

viral_score = 0

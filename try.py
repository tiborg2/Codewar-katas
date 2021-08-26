data = [1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]
peak = []
pos = []
i = 1
while i < (len(data)-1):
    if (data[i] > data [i-1]) and (data[i] >= data[i+1]):
        x = 1
        while data[i] == data[i+x] and data [i+x] != (len(data) - 1):
            x += 1
        if data[i] > data[i+x]:
            peak.append(data[i])
            pos.append(i)
        #peak.append(data[i])
        #pos.append(i)
    i += 1
out = dict()
out["pos"] = pos
out["peaks"] = peak
print(out, "\n", pos, "\n",  peak)


# ([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
# [2, 7, 11, 14, 20, 21] [5, 6, 3, 5, 5, 5]

# [5, 6, 3, 5, 5, 5] [2, 7, 11, 14, 20, 21]
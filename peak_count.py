def pick_peaks(arr):
    peak = []
    pos = []
    i = 1
    while i < (len(arr)-3):
        if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]):
            peak.append(arr[i])
            pos.append(i)
        x = 1    
        if arr[i] == arr[i+x]:
            while (arr[i] == arr[i+x]):
                if (i+x) < (len(arr) - 1):
                    x += 1
                else:
                    break
            if arr[i] > arr[i+x]:
                peak.append(arr[i])
                pos.append(i)
        i += 1
    out = dict()
    out["pos"] = pos
    out["peaks"] = peak
    return out

print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))
print(pick_peaks([2,1,3,1,2,2,2,2]))

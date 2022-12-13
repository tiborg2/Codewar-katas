with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC04/input.txt', 'r') as input:
	data = input.read().splitlines()
	
def to_pairs(data):
	arr = []
	for item in data:
		element = item.split(',')
		arr.append(element)
	return arr

def converter(arr):
	temp1 = []
	temp2 = []
		
	element = arr[0].split('-')
	temp1.append(int(element[0]))
	temp1.append(int(element[1]))

	element = arr[1].split('-')
	temp2.append(int(element[0]))
	temp2.append(int(element[1]))
	return temp1, temp2

arr = to_pairs(data)
final = []
for item in arr:
	element = converter(item)
	final.append(element)

#print (final[9:12])

def sorter (arr):
	sorted = []
	for i in range (0, len(arr)):
		element = []
		x = arr[i][0][0]
		y = arr[i][1][0]
		if x > y:
			element.append(arr[i][1])
			element.append(arr[i][0])
		else:
			element.append(arr[i][0])
			element.append(arr[i][1])
		sorted.append(element)	
	return sorted

srt_final = sorter(final)
#print (srt_final[51])
count = 0
test = []
for item in srt_final:
	x1 = item[0][0]
	y1 = item[0][1]
	x2 = item[1][0]
	y2 = item[1][1]
	print (item,x1,y1,x2,y2)
	
	if (x1 == x2) or (y1 == y2):
		count+=1
		test.append(item)
	if y1 > y2:
		count+=1
		test.append(item)
	
	print(len(test), count)
	
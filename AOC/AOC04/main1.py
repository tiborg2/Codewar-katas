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
#print (final[1:3])

def check_intersection (arr):
	x = False
	x1 = arr[0][0]
	y1 = arr[0][1]
	x2 = arr[1][0]
	y2 = arr[1][1]
	setA = set()
	setB = set()
	#print (x1,y1, x2, y2)
	
	if x1 == y1:
		setA.add(x1)
	else: 
		for i in range (x1, y1+1):
			setA.add(i)
	if x2 == y2 :
		setB.add(x2)
	else:
		for i in range(x2, y2+1):
			setB.add(i)
			#print (setB)
	out = len(setA.intersection(setB))
	#print (setA,'\n', setB)
	#print (out)
	if out > 0:
		x = True
	return x

answer = []
counter = 0
counterT = 0
counterF = 0 
for item in final:
	x = check_intersection(item)
	
	if x == True:
		answer.append(True)
		counterT+=1
	else:
		answer.append(False)
		counterF+=1
	counter+=1

print (f'\nTrue: {counterT}\nFalse: {counterF}\n------------------\nSum: {counter}\n')

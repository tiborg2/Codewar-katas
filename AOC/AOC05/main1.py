with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC05/input.txt', 'r') as input:
	data = input.read().splitlines()
stack_arr =[]

#*******section forming start position from file******************

for i in range(0, 8):
	stack_arr.append(data[i])

temp =[]
for i in range (1,34, 4):
	el = []
	for item in stack_arr:
		el.append(item[i])

	temp.append(el)

start_position =[]
for item in temp:
	element = []
	for i in range(0, len(item)):
		if item[i] != " ":
			element.append(item[i])
	start_position.append(element)


#print(start_position)

#****************forming data of position changes******************

text_arr =[]
for i in range (10, 511):
	text_arr.append(data[i])

movement_arr = []
for item in text_arr:
	tmp = item.split(" ")
	temp = []
	element1 = int(tmp[1])
	element2 = int(tmp[3])
	element3 = int(tmp[5]) 
	temp.append(element1)
	temp.append(element2)
	temp.append(element3)
	movement_arr.append(temp)
#print (movement_arr)
			
#*****************counting changes*****************************

def move (arr, mov):
	crates = mov[0]
	home = mov[1]-1
	dest = mov[2]-1
	temp = []
	#print (f'Home before: {arr[home]} {len(arr[home])}\nDestinationbefore: {arr[dest]} {len(arr[dest])}\n----------------------------- ')
	for i in range (0, crates):
		temp.insert(0,arr[home][0])
		arr[home].pop(0)
	for i in range (0, crates):
		arr[dest].insert(0,temp[i])
	#print (f'Crates: {temp} {len(temp)}\nHome after: {arr[home]} {len(arr[home])}\nDestination after: {arr[dest]} {len(arr[dest])}')
count = 1
for item in movement_arr:
	
	#print (f'\n-{count}-\n')
	move(start_position, item)
	#print (f'**********************************\n------------------------\n**********************************')
	count+=1
#print(len(movement_arr), movement_arr)
answer =[]
for item in start_position:
	answer.append(item[0])
	print (item)

print (''.join(answer))




with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC06/input.txt', 'r') as input:
	data = input.read().splitlines()

	#print(data[0])

def check_difference(string, step):
	x = 0
	y = step
	rezult = 0
	while y < len(string):
		temp = []
		answer = False
		for i in range(x, y):
			temp.append(string[i])
		compare = set(temp)
		if len(temp) == len(compare):
			#print (i, temp, True)
			answer  = True
			rezult = i+1
		#print (temp)
		if answer == True:
			break
		x+=1
		y+=1
	return rezult	

answer = check_difference(data[0], 14)
print (answer) 
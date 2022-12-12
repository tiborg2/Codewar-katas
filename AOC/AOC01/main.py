with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC01/input.txt', 'r') as input:
	data = (input.readlines())


#converting string to int
number_list = []
for element in data: 
	if element != '\n':
		digit = int(element[:-1])
		number_list.append(digit)
	else:
		element = 0
		number_list.append(element)

sum_list = []
sum = 0
for i in number_list:
	if i != 0:
		sum = sum+i
	else:
		sum_list.append(sum)
		sum = 0 

#seeking for largest
largest = 0
for i in sum_list:
	if i > largest:
		largest = i

#seeking for calories sum of top 3 elements
sum_list.sort(reverse = True)
sum = sum_list[0] + sum_list[1] + sum_list[2]


print (f'largest sum: {largest}\nthree largest: {sum_list[0:3]}\nsum of 3 largest:{sum}\n')

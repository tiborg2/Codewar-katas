with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC03/input.txt', 'r') as input:
	data = input.read().splitlines()
	#print (data)

group_data = []
for i in range (0, len(data), 3):
	element = []
	element.append(data[i])
	element.append(data[i+1])
	element.append(data[i+2])
	group_data.append(element)
#print(len(group_data))

def letter_generator():
	#Generator of small and capital latin letters 
	chr_arr = []
	for x in range (97, 123):
		a = chr(x)
		chr_arr.append(a)
	for x in range (65, 91):
		a = chr(x)
		chr_arr.append(a)
	return chr_arr
letters = letter_generator()	
#print (len(letters))

#Rating dictionary for letters
values = {}
i = 1
for item in letters:
	values[item] = i
	i+=1

#Comparing first 2 elements
same_letters = []
for item in group_data:
	s1=item[0]
	s2=item[1]
	char=list(set(s1)&set(s2))
	#print(f'The common letters are:')
	element = []
	element.append(char)
	same_letters.append(char)

def listToString(s):
	#list to string
	str1 = ""
	return str1.join(s)

#Forming string to 2nd comparison 
commons_array =[]
for i in same_letters:
	element = listToString(i)
	commons_array.append(element)
#print (len(commons_array))

#preparing arr for 2nd comparison
arr = []
for i in range (0, len(commons_array)):
	element = []
	el1 = commons_array[i]
	el2 = group_data[i][2]
	element.append(el1)
	element.append(el2)
	arr.append(element)
#print (arr[51], commons_array[51], group_data[51])


#2nd comparison
final_letters = []
for item in arr:
	s1=item[0]
	s2=item[1]
	char=list(set(s1)&set(s2))
	#print(f'The common letters are:')
	final_letters.append(char)
print (len(final_letters))

#counting rezilt
sum = 0
for i in final_letters:
	l = i[0]
	value = values[l]
	sum+=value

print (l, value, sum)


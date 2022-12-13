with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC03/input.txt', 'r') as input:
	data = input.read().splitlines()
	#print (data)
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

#splitting data strings
splited_arr =[] 
for string in data:
	half = int(len(string)/2)
	part1 = string[0:half]
	part2 = string[half:]
	element = []
	element.append(part1)
	element.append(part2)
	splited_arr.append(element)
#print (splited_arr[0][0], splited_arr[0][1])

#finding similar letters and formig array
letters = []
for item in splited_arr:
	s1=item[0]
	s2=item[1]
	char=list(set(s1)&set(s2))
	#print(f'The common letters are:')
	letters.append(char)
#print (letters[2][0], values[letters[2][0]])

sum = 0
for i in letters:
	l = i[0]
	value = values[l]
	sum+=value
	print (l, value, sum)
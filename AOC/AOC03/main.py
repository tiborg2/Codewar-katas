with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC03/input.txt', 'r') as input:
	data = (input.readlines())
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

#Dictionary of letters' rating
values = {}
i = 1
for item in letters:
	values[item] = i
	i+=1

def array_splitter (arr):
	half = (len(arr)-1)/2
	
	pass

x = values['a'] + values['A']


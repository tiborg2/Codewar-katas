'''
Op	Me 	Selection	Pnt
A 	X 	Rock 		1,
B 	Y 	Paper		2,
C 	Z 	Scissors	3.
'''


with open ('/home/tiborg/projects/Codewar-katas/AOC/AOC02/input.txt', 'r') as input:
	data = (input.readlines())
	
def make_touple(element):
	#function makes one touple from one line of file
	first = element[0]
	second = element[2]
	return first, second
rezult_list = []

#generating rezult pairs
for element in data:
	pair = make_touple(element)
	rezult_list.append(pair)

#counting points for selection only.
selection_sum = 0
x_count, y_count, z_count  = 0, 0, 0
print(selection_sum)
for i in rezult_list:
	if i[1] == 'X':
		selection_sum+=1
		x_count+=1
	if i[1] == 'Y':
		selection_sum+=2
		y_count+=1
	if i[1] == 'Z':
		selection_sum+=3
		z_count+=1	

#countinng win=6, draw=3, loss=0)		
wdl_sum = 0
draws, wins = 0, 0
for i in rezult_list:
	fst = i[0]
	snd =i[1]
	if (fst == 'A' and snd == "X") | (fst == 'B' and snd == "Y") | (fst == 'C' and snd == "Z"):
		wdl_sum+=3
		draws+=1
	if (fst == 'A' and snd == "Y") | (fst == 'B' and snd == "Z") | (fst == 'C' and snd == "X"):
		wdl_sum+=6
		wins+=1

score = selection_sum + wdl_sum

print (f'{selection_sum}\n{wdl_sum}\n{score}')

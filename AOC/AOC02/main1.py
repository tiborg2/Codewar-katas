'''
Op	Me 	Selection	Pnt
A 	X 	Rock 		1,
B 	Y 	Paper		2,
C 	Z 	Scissors	3.

X	loose	0
Y 	draw	3
Z	win 	6

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

#counting points for win=6 and draw=3 only.
win_draw_sum = 0
x_count, y_count, z_count  = 0, 0, 0
for i in rezult_list:
	if i[1] == 'X':
		x_count+=1
	if i[1] == 'Y':
		win_draw_sum+=3
		y_count+=1
	if i[1] == 'Z':
		win_draw_sum+=6
		z_count+=1	

#counting point for selection		
selection_sum = 0
rock, paper, scissor = 0, 0, 0
for i in rezult_list:
	fst = i[0]
	snd =i[1]
	if (fst == 'A' and snd == "Y") | (fst == 'B' and snd == "X") | (fst == 'C' and snd == "Z"):
		selection_sum+=1
		rock+=1
	if (fst == 'A' and snd == "Z") | (fst == 'B' and snd == "Y") | (fst == 'C' and snd == "X"):
		selection_sum+=2
		paper+=1
	if (fst == 'A' and snd == "X") | (fst == 'B' and snd == "Z") | (fst == 'C' and snd == "Y"):
		selection_sum+=3
		scissor+=1
#print(selection_sum, rock, paper, scissor)

#final score
score = win_draw_sum + selection_sum


print (f'{win_draw_sum}\n{selection_sum}\n{score}')

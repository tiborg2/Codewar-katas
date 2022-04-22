'''
Class User calculates the amount, that User progresses throught ranking system.
'''
class User ():
    def __init__(self):
        self.rank_index = 0
        self.rank = ranks [self.rank_index]
        self.progress = 0

    def inc_progress (self, level):
        if level not in rank_list:
            raise ValueError 
        act_level = rank_list.index(level)
        if self.rank_index == act_level + 1:#Progress calculation.
            self.progress += 1
        if self.rank_index == act_level:
            self.progress += 3
        if self.rank_index < act_level:
            d = act_level - self.rank_index 
            self.progress += 10*d*d
        if self.rank_index == 15:
                self.progress = 0   
        
        if self.progress >= 100:#Rank up calculation.
            jump = self.progress // 100
            print(jump)            
            residue = self.progress % 100
        if self.rank_index + jump >= 15:
                self.rank_index  = 15
                self.rank = ranks[self.rank_index]
                self.progress = 0
        else:
            print(residue)
            self.rank_index = self.rank_index + jump
            self.rank = ranks[self.rank_index]
            self.progress = residue

ranks = {0:-8, 1:-7, 2:-6, 3:-5, 4:-4, 5:-3, 6:-2, 7: -1, 
        8:1, 9:2, 10:3, 11:4, 12:5, 13:6, 14:7, 15:8}
rank_list = list(ranks.values())
print(rank_list)
user = User()
#print(user.rank, user.progress)
user.inc_progress(8)

print(user.rank, user.progress)
print()
#user.inc_progress(-5)
#print(user.rank, user.progress)
#test.assert_equals(user.progress, 0)
#test.assert_equals(user.rank, -7)


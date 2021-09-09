'''
Function calculates how many years ago the father was twice as old as his son
(or in how many years he will be twice as old).
'''
def twice_as_old(dad_years_old, son_years_old):
    if dad_years_old <= son_years_old:
        return f'ERROR: Father cannot be younger or the same age as son.'
    if son_years_old == 0:        
        return dad_years_old # Example: F=18, S=0. After 18 years F=36, S=18.
    if dad_years_old / son_years_old == 2:
        return 0
    if dad_years_old / son_years_old > 2:
        count = 0
        while dad_years_old / son_years_old > 2:
            count += 1
            dad_years_old += 1
            son_years_old += 1
        return count
    if dad_years_old / son_years_old < 2:
        count = 0
        while dad_years_old / son_years_old < 2:
            count += 1
            dad_years_old -= 1
            son_years_old -= 1
        return count       







print (twice_as_old(50, 8))
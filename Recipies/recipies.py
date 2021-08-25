
def cakes(recipe, available):
    """Function counts how many items can be produced from available resources(ingredients)."""   
    def value_check(ingredients):
        """Nested function checks if we have enough ingredients. Returns True/False."""
        values = ingredients.values()
        count = 0
        for x in values:
            if x >= 0:
                count += 1 
            else:
                return False    
        if count == len(values):
            return True
        else:
            return False
    def key_evaluation(cake, ingredients):
        """Function checks if required type (key) of resources exists in resources(ingredients)."""
        item = set(cake.keys())
        resources = set(ingredients.keys())
        tmp = item - resources
        result = len(tmp)
        if result == 0:
            return True
        return False
    cake = dict(recipe)
    ingredients = dict(available)
    if key_evaluation(cake, ingredients) == False:
        return 0
    check = value_check(ingredients)
    count = int(0)
    while check == True:
        for key in cake:
            ingredients[key] -= cake[key]
        if value_check(ingredients) == True:
            count += 1
        check = value_check(ingredients)
    return count

print (cakes({'flour': 500, 'sugar': 200, 'eggs': 1, "banana": 1},
            {'flour': 2000, 'sugar': 400, 'eggs': 5, 'milk': 200}))
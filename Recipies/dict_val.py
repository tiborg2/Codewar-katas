def value_check(cake, ingredients):
    item = set(cake.keys())
    resources = set(ingredients.keys())
    tmp = item - resources
    result = len(tmp)
    if result == 0:
        return True
    return False


print(value_check({'flour': 500, 'sugar': 200, 'eggs': 1},
            {'flour': 2000, 'sugar': 400, 'eggs': 5, 'milk': 200}))


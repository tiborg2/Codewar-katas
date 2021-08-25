def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0

def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)


def cakes(recipe, available):
    return min(available.get(k, 0) // v for k,v in recipe.iteritems())
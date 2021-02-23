if __name__ == "__main__" :   
    # Input Parsing
    l = open("input.txt").readlines()
    count = {}
    food = []
    d = {}  
    for line in l:
        ingredients, a = line.split(" (")
        ingredients = set(ingredients.split())
        for ing in ingredients:
            if ing in count:
                count[ing] += 1
            else:
                count[ing] = 1
        a = a.replace(")","").replace("contains","").strip().split(", ")
        allergens = set()
        for x in a:    
            allergens.add(x)
        food.append([allergens, ingredients])
    
    # Find the ingredients that can contain each allergen
    for allergens,ingr in food:
        for allergen in allergens:
            if allergen not in d:
                d[allergen] = ingr
            else:
                d[allergen] = d[allergen] & ingr
   
    # Remove those ingredients from the dictionary count
    for key in d:
        for item in d[key]:
            if item in count:
                count.pop(item)

    result = 0
    for item in count:
        result += count[item]    
    print(result)
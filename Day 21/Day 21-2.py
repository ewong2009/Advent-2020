if __name__ == "__main__" :   
    # Input Parsing
    l = open("input.txt").readlines()
    count = {}
    food = []
    d = {} 
    for item in l:
        ingredients , a = item.split(" (")
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
    for i in d:
        for item in d[i]:
            if item in count:
                count.pop(item)
                    
    # Part 2, find which allergens correspond with each ingredient
    allergens = []
    answer = ''    
    while len(d) > 0:
        for key in d:
            if len(d[key]) == 1:
                a = d[key].pop()
                del d[key]
                allergens.append((key,a))
                for key2 in d:
                    d[key2].discard(a)
                break
    allergens.sort()
    for _ , ingredient in allergens:
        answer += ingredient + ','
    
    print(answer[:-1])                                               
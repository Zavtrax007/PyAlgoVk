def feedAnimals(animals, food):
    if type(animals) is not list or type(food) is not list:
        raise TypeError('Arrays must be list')
    if len(animals) == 0 or len(food) == 0:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break
    return count





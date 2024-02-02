while True:
    name, age, weight = input().split()
    age, weight = map(int, [age, weight])

    if(name == '#' and age == weight and age == 0):
        break

    if(age > 17 or weight >= 80):
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')
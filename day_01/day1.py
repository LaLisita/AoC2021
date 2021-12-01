filename = "day_01/input.txt"

with open(filename) as file:
    lines = file.readlines()
    prev = int(lines[0])
    incCount = 0

for l in lines[1::]:
    number = int(l)
    if number > prev:
        incCount+=1
    prev = number

print(incCount)




    





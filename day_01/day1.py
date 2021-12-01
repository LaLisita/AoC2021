filename = "day_01/input.txt"

with open(filename) as file:
    lines = file.readlines()
prev = int(lines[0]) + int(lines[1]) + int(lines[2])
incCount = 0

for i in range(len(lines)-2):
    number = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if number > prev:
        incCount+=1
    prev = number

print(incCount)




    





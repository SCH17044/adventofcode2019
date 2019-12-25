from collections import defaultdict

# string -> wire
# wire example: [ ("U", 5), ("D", 40), ... ]
with open("day03_input.txt") as file:
    move_input = [line.strip() for line in file]

# creates a default collection
dict1 = defaultdict(lambda: defaultdict(int))
dict2 = defaultdict(lambda: defaultdict(int))

distance = []
times = []

# enumerate() adds a counter to an iterable and returns it in a form of enumerate object
for symbol, move in enumerate(move_input):
    x, y = 0, 0
    counter = 1

    # converts the rest of the point into an integer int(point[1:])
    for direction, number in [(point[0], int(point[1:])) for point in move.split(",")]:
        for _ in range(number):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1

            dict2[x][y] += counter

            if dict1[x][y] != 0 and dict1[x][y] != symbol+1:
                distance.append(abs(x)+abs(y))
                times.append(dict2[x][y])

            dict1[x][y] = symbol+1
            counter += 1

print(min(distance))
print(min(times))

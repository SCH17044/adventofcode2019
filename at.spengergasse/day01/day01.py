# part 1
modules_part1 = open("day01_input.txt", "r")
print(sum([(int(float(module) / 3) - 2) for module in modules_part1]))

# part 2
modules_part2 = open("day01_input.txt", "r")
total_fuel = 0

for module in modules_part2:
    needed_fuel = int(float(module) / 3) - 2

    while needed_fuel > 0:
        total_fuel += needed_fuel
        needed_fuel = int(float(needed_fuel) / 3) - 2

print(total_fuel)

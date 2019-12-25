# part 1
input_values = []
text_file = open("day02_input.txt", "r")
for value in text_file.read().split(','):
    input_values.append(int(value))

input_values[1] = 12
input_values[2] = 2


def do_program(input_values):
    copy = input_values[:] # copy of the input values
    for index in range(0, len(copy), 4): # goes through every 4th value of the array, which is the opcode in our case

        opcode = copy[index]
        i_a = copy[copy[index+1]]
        i_b = copy[copy[index+2]]

        if opcode == 99:
            return copy[0]
        elif opcode == 1:
            copy[copy[index+3]] = i_a + i_b
        elif opcode == 2:
            copy[copy[index+3]] = i_a * i_b

    return copy[0]

print(do_program(input_values))

# part 2
for noun in range(100):
    for verb in range(100):
        input_values[1] = noun
        input_values[2] = verb

        output = do_program(input_values)

        if output == 19690720:
            print(100 * noun + verb)
            break

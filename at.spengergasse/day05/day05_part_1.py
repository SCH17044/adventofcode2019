#1

with open('day05_input.txt') as f:
    line = f.readline()
    data = [int(x.strip()) for x in line.split(',')]
    position = 0
    input = 1

    def get_position(mode, i):
        if mode == 0:
            return data[i]
        else:
            return i

    while position < len(data):
        num = data[position] % 100
        mode_1 = data[position] // 100 % 10
        mode_2 = data[position] // 1000 % 10
        mode_3 = data[position] // 10000 % 10
        if num == 1:
            data[get_position(mode_3, position+3)] = data[get_position(mode_1, position+1)] + data[get_position(mode_2, position+2)]
            position += 4
        elif num == 2:
            data[get_position(mode_3, position+3)] = data[get_position(mode_1, position+1)] * data[get_position(mode_2, position+2)]
            position += 4
        elif num == 3:
            data[get_position(mode_1, position+1)] = input
            position += 2
        elif num == 4:
            print(data[get_position(mode_1, position+1)])
            position += 2

f.close()

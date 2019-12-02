from functools import reduce


def runProgram(program):
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break
        elif opcode == 1:
            program[program[i+3]] = program[program[i+1]] + \
                program[program[i+2]]
        elif opcode == 2:
            program[program[i+3]] = program[program[i+1]] * \
                program[program[i+2]]
        else:
            raise Exception("Invalid opcode")
    return program


testPrograms = [[1, 0, 0, 0, 99],
                [2, 3, 0, 3, 99],
                [2, 4, 4, 5, 99, 0],
                [1, 1, 1, 4, 99, 5, 6, 0, 99]]
testOutputs = [[2, 0, 0, 0, 99],
               [2, 3, 0, 6, 99],
               [2, 4, 4, 5, 99, 9801],
               [30, 1, 1, 4, 2, 5, 6, 0, 99]]

if all(map(lambda x: runProgram(x[0]) == x[1],
           zip(testPrograms, testOutputs))):
    print("Tests passed")

file = open("input.txt")
program = file.read().split(',')
file.close()

program = [int(i) for i in program]
program[1] = 12
program[2] = 2
runProgram(program)
print(program[0])

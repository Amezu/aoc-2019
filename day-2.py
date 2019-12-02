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
    return program[0]


testPrograms = [[1, 0, 0, 0, 99],
                [2, 3, 0, 3, 99],
                [2, 4, 4, 5, 99, 0],
                [1, 1, 1, 4, 99, 5, 6, 0, 99]]
testOutputs = [[2, 0, 0, 0, 99],
               [2, 3, 0, 6, 99],
               [2, 4, 4, 5, 99, 9801],
               [30, 1, 1, 4, 2, 5, 6, 0, 99]]

for program in testPrograms:
    runProgram(program)

if all(map(lambda x: x[0] == x[1],
           zip(testPrograms, testOutputs))):
    print("Tests passed")
else:
    print("Tests not passed")


file = open("input.txt")
program = file.read().split(',')
file.close()

program = [int(i) for i in program]
program_copy = program.copy()
program_copy[1] = 12
program_copy[2] = 2
print("Part 1:", runProgram(program_copy))

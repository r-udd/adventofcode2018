import ast
import functions

before = []
after = []
regs = []
funclist = [getattr(functions, func) for func in dir(functions) if callable(getattr(functions, func)) and not func.startswith('__')]
opcodefuncs = [funclist for x in range(16)]
with open('day16/input.1') as f:
    for line in f:
        if line.startswith('Before'):
            before = (ast.literal_eval(line[-13:-1]))

        elif line.startswith('After'):
            after = (ast.literal_eval(line[-13:-1]))
            couldwork = 0
            stillworking = []
            for func in opcodefuncs[int(opcode)]:
                regs = before.copy()
                func(regs, int(a), int(b), int(c))
                if regs == after:
                    stillworking.append(func)
            opcodefuncs[int(opcode)] = stillworking
            if len(stillworking) == 0:
                print('ERROR len should not be 0')

        elif line.startswith('\n'):
            continue

        else:
            opcode, a, b, c = line.split()

#Some opcodes still has multiple possible functions
unique = False
operations = [print] * 16
while not unique:
    unique = True
    for index, funclist in enumerate(opcodefuncs):
        if len(funclist) == 1:
            operations[index] = funclist[0]
        else:
            unique = False
            opcodefuncs[index] = [f for f in funclist if f not in operations]



regs = [0,0,0,0]

with open('day16/input.2') as f:
    for line in f:
        opcode, a, b, c = line.split()
        operations[int(opcode)](regs, int(a), int(b), int(c))
print('answer', regs[0])
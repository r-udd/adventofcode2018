import ast
import functions

before = []
after = []
regs = []
morethan3 = 0
funclist = [getattr(functions, func) for func in dir(functions) if callable(getattr(functions, func)) and not func.startswith('__')]
with open('day16/input.1') as f:
    for line in f:
        if line.startswith('Before'):
            before = (ast.literal_eval(line[-13:-1]))

        elif line.startswith('After'):
            after = (ast.literal_eval(line[-13:-1]))
            couldwork = 0

            for func in funclist:
                regs = before.copy()
                func(regs, int(a), int(b), int(c))
                if regs == after:
                    couldwork += 1
            if couldwork >= 3:
                morethan3 += 1

        elif line.startswith('\n'):
            continue

        else:
            opcode, a, b, c = line.split()
            
print('answer', morethan3)
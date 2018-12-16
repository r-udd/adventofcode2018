import ast
import functions

before = []
after = []
regs = []
morethan3 = 0
total = 0
debugnext = 'Before'
funclist = [getattr(functions, func) for func in dir(functions) if callable(getattr(functions, func)) and not func.startswith('__')]
with open('day16/input.1') as f:
    for line in f:
        if line.startswith('Before'):
            before = (ast.literal_eval(line[-13:-1]))
            if debugnext != 'Before':
                print('ERROR 1')
            debugnext = 'Opcode'
        elif line.startswith('After'):
            after = (ast.literal_eval(line[-13:-1]))
            couldwork = 0
            if debugnext != 'After':
                print('ERROR 2')
            debugnext = 'Endline'
            for func in funclist:
                regs = before.copy()
                func(regs, int(a), int(b), int(c))
                if regs == after:
                    couldwork += 1
            if couldwork >= 3:
                morethan3 += 1
            total += 1
        elif line.startswith('\n'):
            if debugnext != 'Endline':
                print('ERROR 3')
            debugnext = 'Before'
            continue
        else:
            opcode, a, b, c = line.split()
            if debugnext != 'Opcode':
                print('ERROR 4')
            debugnext = 'After'

print('total instructions', total)
print('answer', morethan3)
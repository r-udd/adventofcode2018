import ast
import functions

regs = [11840402, 0, 0, 0, 0, 0]
program = []
funclist = {func: getattr(functions, func) for func in dir(functions) if callable(getattr(functions, func)) and not func.startswith('__')}
with open('day21/input') as f:
    for line in f:
        if line.startswith('#ip'):
            ipindex = int(line.split()[1])
        elif line.startswith('#'):
            continue
        elif line.startswith('\n'):
            continue
        else:
            splitted = line.split()
            funcname = splitted[0]
            a = int(splitted[1])
            b = int(splitted[2])
            c = int(splitted[3])
            program.append((funcname, a, b, c))
ip = regs[ipindex]
counter = 0
while True:
    counter+=1
    regsbefore = regs.copy()
    try:
        operation = program[ip]
    except IndexError:
        print('answer', regs[0])   
        break
    regs[ipindex] = ip
    funclist[operation[0]](regs, operation[1],operation[2],operation[3])
    print(ip, regsbefore, operation, regs)
    #if counter % 1000 == 0:
    #    print(ip, regsbefore, operation, regs)
    ip = regs[ipindex] + 1
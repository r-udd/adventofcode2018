import ast
import functions

regs = [0, 0, 0, 0, 0, 0]
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
seen = set()
while True:
    counter+=1
    regsbefore = regs.copy()
    try:
        operation = program[ip]
    except IndexError:
        print('answer', regs)   
        break
    
    if ip == 18:
        regs[1] = int(regs[2] / 256)
    regs[ipindex] = ip
    funclist[operation[0]](regs, operation[1],operation[2],operation[3])
    if ip == 28:
        if regs[4] not in seen:
            #print('new lowest', regs[4])
            prev = regs[4]
            seen.add(regs[4])
        else:
            #print('seen already', regs[4])
            print('answer', prev)
            break
    ip = regs[ipindex] + 1
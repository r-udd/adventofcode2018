def addr (regs, a, b, c):
    addi(regs, a, regs[b], c)

def addi (regs, a, b, c):
    regs[c] = regs[a] + b
#
def mulr (regs, a, b, c):
    muli(regs, a, regs[b], c)

def muli (regs, a, b, c):
    regs[c] = regs[a] * b
#
def banr (regs, a, b, c):
    bani(regs, a, regs[b], c)

def bani (regs, a, b, c):
    regs[c] = regs[a] & b
#    
def borr (regs, a, b, c):
    bori(regs, a, regs[b], c)

def bori (regs, a, b, c):
    regs[c] = regs[a] | b
#    
def setr (regs, a, b, c):
    seti(regs, regs[a], b, c)

def seti (regs, a, b, c):
    regs[c] = a
#
def gtir (regs, a, b, c):
    regs[c] = a > regs[b]
    
def gtri (regs, a, b, c):
    regs[c] = regs[a] > b

def gtrr (regs, a, b, c):
    regs[c] = regs[a] > regs[b]
#
def eqir (regs, a, b, c):
    regs[c] = a == regs[b]
    
def eqri (regs, a, b, c):
    regs[c] = regs[a] == b

def eqrr (regs, a, b, c):
    regs[c] = regs[a] == regs[b]
    


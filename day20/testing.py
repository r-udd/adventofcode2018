

def findbackwardmatchingparenthesis(text, index):
    count = 0
    for i in range(index, -1, -1):
        char = text[i]
        if char == ')':
            count += 1
        elif char == '(':
            count -= 1
            if count == 0:
                return i

def removeparenthesis(text):
    right = text.rfind('|)')
    while right != -1:
        match = findbackwardmatchingparenthesis(text, right + 1)
        text = text[:match] + text[right+2:]

        right = text.rfind('|)')
    return text
'''
line = '123456(456|)abc(34|)789'
text = removeparenthesis(line)
print(text)
'''
with open('day20/test6') as f:
    line = f.readline()
    print(len(line))
    text = removeparenthesis(line)
    print(len(text))

with open('day20/test6.1') as f:
    line = f.readline()
    print(len(line))

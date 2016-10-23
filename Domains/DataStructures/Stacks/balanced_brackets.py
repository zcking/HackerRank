
import sys

def checker(s):
    stack = []
    balanced = True
    index = 0


    while index < len(s) and balanced:

        symbol = s[index]

        if symbol in "{[(":
            stack.append(symbol)

        else:

            if len(stack) == 0:
                balanced = False 

            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False 

        index += 1


    if balanced and len(stack) == 0:
        return 'YES'

    else:
        return 'NO'
    
def matches(open_Symbol, close_symbol):

    opens = "([{"
    closers = ")]}"

    return opens.index(open_Symbol) == closers.index(close_symbol)


t = int(raw_input().strip())
for a0 in range(t):
    s = raw_input().strip()
    
    print(checker(s))

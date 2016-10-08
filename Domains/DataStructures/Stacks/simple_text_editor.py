
Q = int(input())


string = ''
history = []  

for i in range(Q):  
    #print('After ' + str(i+1) + ': ' + string)
    t = input()
    if ' ' in t:
        t, s = t.split(' ')
    
    if t == '1':
        history.append(string)
        string += s
    elif t == '2':
        history.append(string)
        string = string[:-1*int(s)]
    elif t == '3':
        try:
            print(string[int(s)-1])
        except:
            continue
    elif t == '4':
        string = history.pop()
        
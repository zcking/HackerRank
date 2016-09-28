def ransom_note(magazine, ransom):
    if len(ransom) > len(magazine):
        return False
    
    for word in ransom:
        try:
            index = magazine.index(word)
            magazine[index] = ''
            continue
        except ValueError:
            return False
        
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

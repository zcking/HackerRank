"""
Cre­ate another another Stack(track_max) which will keep track of max­i­mum in the given Stack(Arr).
When you insert an ele­ment in the Arr stack for the first time ( means it is empty), insert it in the track-max Stack as well.
Now onwards when you insert a new element(say it is x) in the Arr Stack, peek() the ele­ment from the track Stack ( say it is ‘a’). 
Com­pare x and a and which ever is greater, insert it into track_max Stack.
When you pop the ele­ment from the Arr stack, pop from the track_stack Stack as well
So to get to know the max­i­mum ele­ment in the Arr Stack, peek the ele­ment in the track_max Stack.
"""

N = int(input())
Arr = []
track_max = []


for i in range(N):
    
    args = raw_input().strip().split(" ")
    
    if args[0] == '1':
        num = int(args[1])
        if len(Arr) == 0:
            Arr.append(num)
            track_max.append(num)
            
        else:
            Arr.append(num)
            top_max = track_max[-1]
            track_max.append(max(top_max, num))
        
    if args[0] == '2':
        if len(Arr) != 0 and len(track_max) != 0 :
            Arr.pop()
            track_max.pop()
        

    if args[0] == '3':
        print (track_max[-1])
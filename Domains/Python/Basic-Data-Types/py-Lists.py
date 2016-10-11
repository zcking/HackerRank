T = int(input().strip())
Arr = []

for i in range(T):
    # save each command as a list 
    args = input().strip().split(" ")
    
    # check for print command
    if args[0] == "print":
        print(Arr)
        
    # Check for insert command and insert item to the list
    elif len(args) == 3:
        
        # use getattr (http://devdocs.io/python~3.5/library/functions#getattr)
        getattr(Arr, args[0])(int(args[1]), int(args[2]))
        
        
    # Check for append
    elif len(args) == 2:
        getattr(Arr,args[0])(int(args[1]))
        
    
    # Check for the remaining commands such as sort and pop, etc
    else:
        getattr(Arr, args[0])()
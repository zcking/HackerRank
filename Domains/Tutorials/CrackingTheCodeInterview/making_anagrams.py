from itertools import repeat

def number_needed(a, b):
    # Map the count of each character for a and b
    a_lets = set(a)
    b_lets = set(b)
    a_dict = dict(zip(a_lets, repeat(0, len(a_lets)))) # Set each letter's (key) value to 0
    b_dict = dict(zip(b_lets, repeat(0, len(b_lets))))
    
    for letter in a_lets:
        a_dict[letter] = a.count(letter)
            
    for letter in b_lets:
        b_dict[letter] = b.count(letter)
            
    # Check for anagram
    counter = 0
    
    unique_a_lets = a_lets.difference(b_lets) # letters in a but not in b
    unique_b_lets = b_lets.difference(a_lets) # letters in b but not in a
    same_lets = a_lets.intersection(b_lets)   # letters in both a and b
    
    # Count all the missing letters
    for let in unique_a_lets:
        counter += a_dict[let]
    for let in unique_b_lets:
        counter += b_dict[let]
        
    # Count the shared letters
    for let in same_lets:
        counter += abs(a_dict[let] - b_dict[let])
            
            
    return counter
        

a = input().strip()
b = input().strip()

print(number_needed(a, b))

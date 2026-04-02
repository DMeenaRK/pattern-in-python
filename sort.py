def custom_sort(c):
    if c.islower():
        return (0, c)      
    elif c.isupper():
        return (1, c)      
    elif c.isdigit():
        val = int(c)
        if val % 2 != 0:
            return (2, c)  
        else:
            return (3, c)  

s = input()
print("".join(sorted(s, key=custom_sort)))

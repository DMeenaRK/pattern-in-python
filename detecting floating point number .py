import re
for _ in range(int(input())):
    s = input().strip()
    pattern = r'^[+-]?\d*\.\d+$'
    
    try:
        if re.match(pattern, s) and float(s):
            print("True")
        elif re.match(pattern, s):
            print("True")
        else:
            print("False")
    except ValueError:
        print("False")

import re
for _ in range(int(input())):
    pattern = r"^[789]\d{9}$"
    
    if re.match(pattern, input()):
        print("YES")
    else:
        print("NO")

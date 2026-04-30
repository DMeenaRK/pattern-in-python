import re

S = input()
k = input()

pattern = re.compile(f'(?=({k}))')
matches = list(pattern.finditer(S))

if not matches:
    print((-1, -1))
else:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))

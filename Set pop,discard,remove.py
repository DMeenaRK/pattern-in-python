n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())
for _ in range(num_commands):
    command = input().split()
    
    cmd_name = command[0]
    
    if cmd_name == 'pop':
        s.pop()
    elif cmd_name == 'remove':
        s.remove(int(command[1]))
    elif cmd_name == 'discard':
        s.discard(int(command[1]))
print(sum(s))

if __name__ == '__main__':
    N = int(input())
    res = []
    
    for _ in range(N):
        command, *args = input().split()
        
        if command == "insert":
            res.insert(int(args[0]), int(args[1]))
        elif command == "print":
            print(res)
        elif command == "remove":
            res.remove(int(args[0]))
        elif command == "append":
            res.append(int(args[0]))
        elif command == "sort":
            res.sort()
        elif command == "pop":
            res.pop()
        elif command == "reverse":
            res.reverse()
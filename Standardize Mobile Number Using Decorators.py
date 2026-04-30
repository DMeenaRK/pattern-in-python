def wrapper(f):
    def fun(l):
        format_f = [x[-10:] for x in l]
        decode_f = [f"+91 {x[0:5]} {x[5:10]}" for x in format_f]
        f(decode_f)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
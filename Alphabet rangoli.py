
def print_rangoli(size):
    import string
    chars = string.ascii_lowercase 
    lines = []
    for i in range(size):
        s = "-".join(chars[i:size][::-1] + chars[i+1:size])
        lines.append(s.center(4 * size - 3, "-"))
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
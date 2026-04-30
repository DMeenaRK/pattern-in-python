import re

if __name__ == "__main__":
    t = int(raw_input())
    
    for _ in range(t):
        try:
            pattern = re.compile(raw_input())
            print(True)
        except re.error:
            print(False)
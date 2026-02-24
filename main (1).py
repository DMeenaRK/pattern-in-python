import sys

def iweird(n):
    if(n%2!=0):
        print("weird")
    else:
            if(n%2==0 and 2<=n<=5):
                print("not weird")
            elif(n%2==0 and 6<=n<=20):    
                print("weird")
            else:
                print("not weird")


if __name__ == '__main__':
    n = int(input().strip())
    iweird(n)

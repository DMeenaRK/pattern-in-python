
    
from datetime import datetime

def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    return str(int(abs((dt1 - dt2).total_seconds())))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        t1 = input().strip()
        t2 = input().strip()

        delta = time_delta(t1, t2)
        print(delta)


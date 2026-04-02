

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()

    chars = sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))

    for char, count in chars[:3]:
        print(f"{char} {count}")

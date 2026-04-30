import re
import email.utils


pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

n = int(input())

for _ in range(n):
    line = input()
    parsed_email = email.utils.parseaddr(line)
    if re.match(pattern, parsed_email[1]):
        print(email.utils.formataddr(parsed_email))

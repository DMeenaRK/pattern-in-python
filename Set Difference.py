n = int(input())
english_subs = set(map(int, input().split()))
m = int(input())
french_subs = set(map(int, input().split()))

result = english_subs.symmetric_difference(french_subs)

print(len(result))


n = int(input())
english_set = set(map(int, input().split()))

b = int(input())
french_set = set(map(int, input().split()))
only_english = english_set.difference(french_set)

print(len(only_english))


n = int(input())
distinct_countries = set()
for _ in range(n):
    country = input().strip()
    distinct_countries.add(country)
print(len(distinct_countries))
n = int(input())

result = set()

for _ in range(1, n + 1):
    current_set = set(input().split())
    result = result.union(current_set)

for r in result:
    print(r)
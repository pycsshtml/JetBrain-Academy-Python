lst = []
while True:
    n = input()
    if n == '.':
        break
    else:
        lst.append(int(n))
print(sum(lst) / len(lst))
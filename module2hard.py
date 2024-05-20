result = str()
n = 7
for i in range(1, int(n/2) + 1):
    for j in range(1, 21):
        if n % (i + j) == 0:
            result += str(i) + str(j)
print(result)
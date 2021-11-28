# Collatza recursion


# def collatza(n):
#     if n == 1:
#         return 0
#     elif n%2 == 0:
#         return int(n/2)
#     else:
#         return int(3*n + 1)

x = 0 # temp value to calculate a number of steps
y = 0 # temp value to store the number of steps

def collatza(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatza(int(n/2))
    else:
        return 1 + collatza(int(3*n + 1))


for i in range(1, 100001):
    x = collatza(i)
    if x > y:
        y = x
        z = i # the number with max of steps


print(f"max steps - {y} and it is a {z}")

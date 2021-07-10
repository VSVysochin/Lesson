list_cubes = []
all_sum = 0

for ind in range(1, 1001, 2):
    list_cubes.append(ind ** 3)

for i, v in enumerate(list_cubes):
    sum_digits = 0
    while v > 0:
        sum_digits += v % 10
        v //= 10
    if sum_digits % 7 == 0:
        all_sum += list_cubes[i]
    list_cubes[i] += 17

print(all_sum)

all_sum = 0

for i, v in enumerate(list_cubes):
    sum_digits = 0
    while v > 0:
        sum_digits += v % 10
        v //= 10
    if sum_digits % 7 == 0:
        all_sum += list_cubes[i]

print(all_sum)
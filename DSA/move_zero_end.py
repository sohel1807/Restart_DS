def move_zero_end(lst):
    i = 0

    for j in range(len(lst)):
        if lst[j] != 0:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1

    return lst

print(move_zero_end([0, 0, 1, 0, 3, 0]))
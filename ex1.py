def eratosthenes(n):
    my_list = [i for i in range(3, n + 1)]
    error_znach = [my_list[i] for i in range(len(my_list)) if my_list[i] % 2 == 0]
    my_list = [my_list[i] for i in range(len(my_list)) if my_list[i] % 2 != 0]
    a = min(my_list)
    tech_znach = []
    while a < n:
        a = min(my_list)
        del my_list[my_list.index(min(my_list))]
        for i in range(len(my_list)):
            if my_list[i] % a == 0:
                tech_znach.append(my_list[i])
        for i in range(len(tech_znach)):
            del my_list[my_list.index(tech_znach[i])]
    error_znach.extend(tech_znach)
    error_znach = [str(error_znach[i]) for i in range(len(error_znach))]
    if len(error_znach) == 0:
        print()
    else:
        print(' '.join(error_znach))


eratosthenes(15)

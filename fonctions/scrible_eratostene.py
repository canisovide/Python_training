def est_premier(n):
    m = 0
    for i in range(1, n + 1):
        if n % i == 0:
            m += 1

    if m == 2:
        return True

    return False


# print("Le scrible d'erathostene :")
# for i in range(1, 101) :
#     if est_premier(i):
#         print("{}".format(i))

for i in range(1,101):

    if i%10 != 0  and est_premier(i):
        print("{:4d}".format(i), end=" ")
    elif i%10 != 0 and not est_premier(i):
        print("{:4d}".format(i), end=" ")
    else:
        print("{:4d}".format(i))



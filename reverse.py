def my_reverse(l):

    a = len(l) - 1
    newList = []

    while (a >= 0):
        newList.append(l[a])
        a -= 1

    print(newList)
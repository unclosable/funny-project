def mergeThree(l1, l2, l3):
    l1l2 = mergeTwo(l1, l2)
    return mergeTwo(l1l2, l3)


def mergeTwo(l1, l2):
    dic = {}
    re = []
    for i in l1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in l2:
        if i in dic and dic[i] > 0:
            dic[i] -= 1
            re.append(i)

    return re


if __name__ == '__main__':
    print(mergeThree([1, 2, 3, 4, 4, 5, 5, 6], [5, 5, 4, 4, 6, 7, 8], [5, 5, 5, 6, 7, 8]))

if__name__ == '__main__':
    s = input()
    dct = {}
    for c in s:
        dct[c] = dct.get(c, 0) + 1
    lst = sorted(list(dct.items()), key=lambda x: (-x[1], x[0]))
    print("\n".join(map(lambda x: x[0] + " " + str(x[1]), lst[:3])))

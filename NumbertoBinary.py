def Numtobinary():
    num = int(input("Enter the number: "))
    st = ''
    if num % 2 == 0:
        while num != 1:
            div = num // 2
            x = num - (div * 2)
            st = st + str(x)
            num = div
            if num == 1:
                st = st + '1'
    else:
        while num != 0:
            div = num // 2
            x = num - (div * 2)
            st = st + str(x)
            num = div
    y = len(st) + 1
    print(f"The Binary is: {st[y: : -1]}")


Numtobinary()
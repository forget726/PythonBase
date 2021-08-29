'''
def mul(*num):

    if len(num)==0:

        raise TypeError

    else:

        result = 1

    for nums in num:

        result = result * nums

    return result

print(mul (5,6,7))
'''


def mul(*y):
    if len(y) == 0:
        print('systans error!')
    else:
        sum = 1
        for n in y:
            sum = sum * n
    return (sum)


cal1 = mul(2, 3, 5)

cal2 = mul(23, 45, 67, 54)

print(cal1, cal2, sep="\n")

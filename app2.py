def p(x, coeff):
    # e.g. p (1, (3, 5)) = 3*1^1 + 5*1^2
    return sum([b * x ** a for a, b in enumerate(coeff)])


m = p(1, (2, 4))


# print (m)


# Write a function that takes a string as an argument and returns the number of capital letters in the string


def upp(foo):
    return sum([x == x.upper() and x.isalpha() for x in foo])


# print(upp('AasBasFaLKDSF*&(*89K'))


def issubset(seq_a, seq_b):
    answer = True
    for x in seq_a:
        if x not in seq_b:
            answer = False
            break
    return answer


print(issubset([1, 2], [1, 2, 3]))

print(issubset([1, 2, 3], [1, 2]))

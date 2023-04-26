# Wypisywanie n razy wyrazu rekurencyjnie

def wypisywanie(n):
    if n == 1:
        print(n)
    else:
        print(n)
        wypisywanie(n-1)



# Proszę napisać program, który rekurencyjnie zlicza silnie

# def silnia(n, iloczyn=1):
#     if n == 1:
#         return iloczyn
#     else:
#         return silnia(n-1, iloczyn = iloczyn *  n)
#
#
# print( silnia(20) )


def silnia(n):
    if n<2:
        return 1
    else:
        return silnia(n-1)*n

# Napisz program ,który rekurencyjnei znajduje 10 pierwszych liczb trojkatnych 




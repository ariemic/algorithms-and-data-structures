from math import sqrt
from random import randint


def prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    i = 5
    while i <= sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end while
    return True

#end prime function

def new_numbers( n ):
    def rek(n, x, i):
        if n == 0:
            if n != x and prime( x ) and len( str(x) ) >= 2: print(x)
    
        else:
            rek( n//10, x + ( n % 10 ) * ( 10 ** i ), i + 1)
            rek( n//10, x, i)
    #end def rek
    return rek(n, 0, 0)
#end def new_numbers

# new_numbers(8314)

def waga(n):
    cnt = 0
    i = 2
    k = n 
    while i <= sqrt(k) + 1:
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n = n // i
        #end if 
        i += 1 
    #end while
    return cnt 

def zad2(T):
    
    def rek(x,y,z,i):
        if i == len(T):
            if x == y == z: return True 
            return False 
        else:
            return rek(x+waga( T[i] ), y, z, i + 1) or rek(x, y+waga( T[i] ), z, i + 1) or rek(x, y, z+waga( T[i] ), i + 1)
    #end def
    return rek(0,0,0,0)
#end zad2

# T = [1,2,64,42,8,9,15]
# print( zad2(T) )


def zad3(T,k):
    best = float('inf')
    def rek(y, x, koszt):
        nonlocal best
        if y == 7: 
            best = min(best, koszt)
        else:
            if x > 0:
                rek(y + 1, x - 1, koszt + T[y][x] )

            rek(y + 1, x, koszt + T[y][x] )
            
            if x < 7: rek(y + 1, x + 1, koszt + T[y][x] ) 

    #end def rek
    rek(0, k, T[0][k] )
    return best
#end zad3


T = [ [15, 17, 11, 15, 15, 19, 6, 9],
[20, 5, 18, 8, 15, 4, 4, 4],
[1, 14, 20, 16, 17, 17, 15, 17],
[14, 2, 2, 10, 20, 16, 15, 13],
[12, 18, 18, 12, 7, 4, 18, 1],
[19, 20, 18, 13, 16, 9, 2, 8],
[4, 9, 5, 6, 5, 5, 10, 4],
[2, 9, 10, 19, 19, 7, 8, 15] ]

# print(zad3(T,4) ) 


###

def if_jump_possible(T,y,x):
    n = len(T)
    if 0 <= y <= 7:
        if 0 <= x <= 7:
            return True
    #end if
    return False 



###

def bin_to_dec(T,k,i):
    x = 0
    pom = 0
    for y in range(i,k-1,-1):
        x += T[y] * ( 2 ** pom )
        pom += 1
    #end for
    return x 



def zad6(T):
    def rek(sum_elements, sum_indexes, i):
        if i == len(T):
            if sum_elements == sum_indexes and sum_elements != 0:
                print(sum_elements)
               
        else:
            rek(sum_elements + T[i], sum_indexes + i, i + 1)
            rek(sum_elements, sum_indexes, i + 1)
        #end if
    return rek(0,0,0)
#end def

# T = [1,7,3,5,11,2]
# zad6(T)


def waga_2(T,n,i=0):
    if n == 0: 
        return True
    if i == len(T) or n < 0:
        return False 
    
    return waga_2(T, n-T[i], i+1) or waga_2(T, n, i + 1) or waga(T,n+T[i], i + 1)

    

# T = [2,7,14,4,3]
# print( waga_2(T,10) )




def liczba_samoglosek(n):
    set_1 = {'a', 'e', 'i','o','u','y'}
    cnt = 0
    n = n.lower()
    for i in range(len(n)):
        if n[i] in set_1: cnt += 1 
    #end for
    return cnt 

def sum_codes(n):
    suma = 0
    for i in range( len(n ) ):
        suma += ord( n[i] )
    #end for
    return suma



### 

def rek(x,y,n,i):

    if x == y == 0:
        if prime(n): print(n)

    elif x == 0: 
        y = y * ( 10 ** i )
        n = n + y 
        if prime(n): print(n)
    
    elif y == 0:
        x = x * ( 10 ** i )
        n = n + x
        if prime(n): print(n)

    else:
        rek(x//10, y, n + (x % 10) * ( 10 ** i ), i + 1)
        rek(x, y//10, n + (y % 10) * ( 10 ** i ), i + 1)
    


# rek(13,31,0,0)



###




# n = len(T) 

# def king(T, w, k):
    
#     if w == 7 and k == 7:
#         return True

#     else:

#         if is_possible(w+1,k+1):
#             if last_digit( T[w][k] ) < first_digit( T[w+1][k+1] ):
#                 if king(T,w+1,k+1):
#                     return True
            
#         #end if
#         if is_possible(w, k+1):
#             if last_digit( T[w][k] ) < first_digit( T[w][k+1] ): 
#                 if king(T, w, k + 1):
#                     return True
             
#         #end if
#         if last_digit( T[w][k] ) < first_digit( T[w+1][k] ):
#             if king(T, w+1, k):
#                 return True

    # return False 
#end def king 

# for i in range(10000):
#     tab = [ [randint(1,30) for _ in range(8)] for _ in range(8) ]
#     if king(tab,0,0): print("1")

def last_digit(n):
    return n % 10 


def first_digit(n):
    while n // 10 != 0:
        n = n // 10 
    #end while
    return n % 10


def can_move(y,x,to_y,to_x):
    if to_y >= y:
        if to_x >= x:
            return True
    #end if
    return False

def if_possible(y,x):
    if 0 <= y <= 7:
        if 0 <= x <= 7:
            return True
    #
    return False


def king(T, y, x):

    if y == 7 and x == 7:
        return True 
    
    
    moves = [ (0,1), (1,0), (1,1) ]

    for ele in moves:
        if if_possible( y + ele[0], x + ele[1] ):
            if can_move( y, x, y + ele[0], x + ele[1] ):
                if last_digit( T[y][x] ) < first_digit( T[ y + ele[0] ][ x + ele[1] ] ):
                    return king(T, y + ele[0], x + ele[1])
                        
    #end for
    return False 

# ----------------------------------

def zad21(T, s):
    def rek(T, s, value, W, K): # Tablice W i K to tablice (jednowymiarowe) True/False. True jesli moge wziac element z danego wiesza, False jesli nie moge. Analogicznie dla kolumn

        if value > s: return False 
        if value == s and value != 0: 
            print( value )
            return True
        

        for y in range( 8 ):
            if W[y]:
                for x in range( 8 ):
                    if K[x]:

                        W[y] = False
                        K[x] = False

                        if rek(T, s, value + T[y][x], W, K):
                            return True 
                        else:
                            W[y] = True
                            K[x] = True 
                            return False 
                #end for 2
        #end for 1
        
    #end def rek 
    return rek(T, s, 0, [True] * 8, [True] * 8)
#end def zad 21 ------------------


def prime_factor(n,k):
    return n % k == 0 and prime(k)


def zad22(T):

    def rek(T, i, cnt):

        if i == len(T) - 1:
            print( cnt )
            return True

        k = 2 
        while i + k < len(T):
            if prime_factor( T[i], k):
                if rek(T, i + k, cnt + 1):
                    return True
            else:
                k + 1 

        #end while
        return False
    #end def rek
    return rek(T, 0, 0)
                    



def zad26(a,b):
    def rek(a, b, liczba, i = 0):

        if a == 1:
            liczba += 2 ** ( i + b )
            if not prime( liczba ): print( liczba )
            return
        
        if b == 0: 

            for k in range(a):
                liczba += 2 ** ( i + a - 1 )
                a -= 1
            
            if not prime( liczba ): print( liczba )
            return 
        
        else:
            rek(a, b - 1, liczba, i + 1)
            rek(a - 1, b, liczba + ( 2 ** i ), i + 1)
    #end def rek
    return rek(a,b,0)

#end def zad26


def zad32(T, k):
    def rek(T, k, i, a, b, suma):

        if i == len(T):
            return False 

        if suma == 0 and a != 0:
            if a + b == k:
                return True 
        
        else:
            return rek(T, k, i + 1, a + 1, b, suma + T[i] ) or rek(T, k, i + 1, a, b + 1, suma - T[i] )
    #end def rek
    return rek(T, k, 0, 0, 0, 0)
#end def zad32     


# T = [1,17,4,2,7,1,9]
# print(zad32(T, 8))
        




# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry



# def zad(n):
#     def rek(n, x, i):
#         if n == 0:
#             if i >= 2:
#                 if prime( x ):
#                     print( x )
        
#         rek( n // 10, x + ( n % 10 ) * ( 10 ** i ), i + 1 )
#         rek( n // 10, x, i )
#     #end def
#     return rek(n, 0, 0)
# #end def zad

# zad(134)

        
            



        










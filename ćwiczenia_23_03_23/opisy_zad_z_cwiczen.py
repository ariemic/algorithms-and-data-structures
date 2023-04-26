'''
1. Dana jest tablica n liczb ze zbioru {0, ,,, n^2 -1}. Chcemy ją posortować.
Korzystamy z radix sorta, gdyż counting sort powodowałby że mielibyśmy złożoność kwadratową. 
1)%n
2) //n


2.Sortowanie tablicy n liczb, w której występuje O(logn) różnych wartości.
3. Dana jest tablica n liczb. Szukamy takcih dwóch, które po posortowaniu byłyby koło sibie, których różnica jest maksymalna.

Wkładamy liczby do n kubełków, dla każdego kubełka znjdujemy min i max, porównujemy odlegości pomiędzy kubełkami i wybieramy wieksza.
Kilka liczb może być w tym samym kubełku wtedy napewno, będą istniały puste kubełki. Jeżeli mielibyśmy np. jeden kubełek w którym byłyby prawie 
wszystkie wartości i jeden kubełek z większą wartością to w kubełku z mniejszymi wartościamy musiamy znaleźć max, odległość od niego a wiekszego 
będzie największa.


4. Dane są dwa napisy. Proszę zaimplementować funkcję sprawdzającą czy są anagramami.
'''
#4
def is_anagram(a, b):
    if a != b: return False
    A = [0]*(ord('z') - ord('a')+1)
    for i in a:
        A[ord('i')-ord('a')] += 1
    for j in b:
        A[ord('j')-ord('a')] -= 1
        if A[ord('j')-ord('a')] != 0: return False
    '''
    for i in a:
        A[ord('i')-ord('a')] = 0
    for j in b:
        A[ord('i')-ord('a')] = 0
    '''
    return True
#mozna zaimplementować tą funkcje bez zerowania tablicy dla dużego alfabetu i małych słów


'''
5. Mamy tablicę T rozmiaru n T[i] należy do przedziału {0, .... k-1}
Chcemy najmniejszy podprzedział T, który zawiera wszystkie kolory. 


6.
mamy ogromna tablice liczników, każde pole zawera dwie wartości : licznik i wskażnik na stos, stos musimy zaokplementowac na talibcy żeby wskazniki działałay. Poczatkowo
stos jest zupsy. Kidey patrzymy na indeks 7 jesli wskazuje na sots to wiemy liznik nie był wgl wczesniej uzywany
Pole wsakzuje na sots, stos z powrotem wskazuje na niego. Jeżli znowu zobaczymy 7 to odsyła na stos do 1, zwiekszamy licznik.

'''














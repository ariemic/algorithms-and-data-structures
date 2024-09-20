from zad3testy import runtests

""" Złożoność czasowa: O(N + nlogn)
Algorytm porównuje każde słowo z zadanej tablicy ze swoją odwrotnością, następnie wybiera mniejszy leksykograficznie odpowiednik (dzięki temu w tablicy napisy, które są równoważne będą wyglądać tak samo).
Następnie sortuje zmienioną tablce, według kolejności leksykograficznej napisów, używając quicksorta. Po tym zabiegu te same napisy będą obok siebie, zliczam ile jest takich samych napisów w tablicy,
jeżeli jakiś ma moc >= połowy pozostałych napisów to kończe szukanie i zwracam zmienną maxi, bo nie znajdę już nic większego.  """


def partition(A, l, r):
  x = A[r]
  i = l - 1
  for j in range(l, r):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1

def quicksort(A, l, r):
  if l < r:
    pivot = partition(A, l, r)
    quicksort(A, l, pivot - 1)
    quicksort(A, pivot+1, r)


# partintion for new_T = [('eips', 433), ('msyz', 467), ('kot', 334), ('gkotu', 554), ('kot', 334), ('eips', 433), ('kot', 334)] where idx is the number of element we sort by
def partition_idx(A, l, r, idx):
  x = A[r][idx]
  i = l - 1
  for j in range(l, r):
    if A[j][idx] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1

def quicksort_idx(A, l, r, idx):
  if l < r:
    pivot = partition_idx(A, l, r, idx)
    quicksort_idx(A, l, pivot - 1, idx)
    quicksort_idx(A, pivot+1, r, idx)


def sort_word(word):
  word_list = list(word)
  suma = sum(ord(x) for x in word_list)
  quicksort(word_list, 0, len(word_list)-1)
  return ("".join(word_list), suma)

def strong_string(T):
    n = len(T)
    for i in range(n):
      T[i] = sort_word(T[i])
    quicksort_idx(T, 0, n-1, 1) #Sort the list based on the sum (second element)
    sorted_T = [x[0] for x in T] #extract only the sorted words

    power = 1
    i = 0
    while i < n:
      j = i+1
      loc_power = 1
      while j < n and sorted_T[i] == sorted_T[j]:
        loc_power += 1  
        j += 1
      i = j
      power = max(loc_power, power)
      if power > n//2 + 1 : return power
    
    return power


    

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# new_T = [('eips', 433), ('msyz', 467), ('kot', 334), ('gkotu', 554), ('kot', 334), ('eips', 433), ('kot', 334)]
# sorted_T=['kot', 'kot', 'kot', 'eips', 'eips', 'msyz', 'gkotu']
# strong_string(T)

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=False )

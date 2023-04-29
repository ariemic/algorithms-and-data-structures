'''
Najkrótsze ścieżki między każdą parą wirzchołków
- |V| wywołań Dijkstry O(VElogV)
- |V| wywołań Bellmana-Forda O(V^2E)

Istnieje specjalizowany algorytm Floyda-Warshalla który znajduje rozwiązanie w czasie O(V^3) - radzi sobie z kraw ujemnymi

Dla grafów rzadkich z ujemnymi krawedziami -> algorytm Floyda-Warshalla
Dla grafów rzadkich bez ujemnych kraw -> Dijkstra, dla gęstych nie traci się dużo
Dla grafów gęstych -> Floyd-Warshall

Aby sprawdzić czy graf jest rzadki czy gęsty należy policzyć krawędzie

'''
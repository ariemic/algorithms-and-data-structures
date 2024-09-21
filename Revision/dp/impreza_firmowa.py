class Employee:
  def __init__(self, fun):
    self.emp = []
    self.fun = fun
    self.f = -1
    self.g = -1



# wartość najlepszej imprezy dla poddrzewa ukorzenionego w v
def f(v):
  if v.f >= 0: return v.f
  x = g(v)
  y = v.fun
  for u in v.emp:
    y += g(u)
  v.f = max(y, x)
  return v.f

#j.w, gdy v nie jest zaproszony
def g(v):
  if v.g >= 0: return v.g
  v.g = 0
  for u in v.emp:
    v.g += f(u)
  return v.g


# Coś w tym stylu nie mam przykładu żeby sprawdzić poprawność i jest to bardziej poglądowe
def problem_imprezy_firmowej(G, boss):
  n = len(G)
  employees = [Employee(u) for u in range(n)]
  return max(f(employees(boss)), g(employees(boss)))



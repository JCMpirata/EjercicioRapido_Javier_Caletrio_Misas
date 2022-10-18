# Ejercicio 2: Utilice las funciones anteriores para elminar elementos sobrantes
def ejercici0():
  lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  del lista[5]
  lista.remove(3)
  lista.pop()
  assert lista == list(range(1,6))
  
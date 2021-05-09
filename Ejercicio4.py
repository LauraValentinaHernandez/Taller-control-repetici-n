"""
Calcular el término doceavo y la suma de los doce primeros términos de la sucesión: 6, 11, 16, 21. Respuesta: a12=61, suma=402.
"""
lista=[]
for i in range(1,13):
  t=5*i+1
  lista.append(t)
print(lista)
suma=sum(lista)
print(suma)

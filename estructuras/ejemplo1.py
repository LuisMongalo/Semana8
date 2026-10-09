listas = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "Hola"]
print(listas)

conjuntos = {1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "Hola"}
print(conjuntos)

tuplas = (1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "Hola")
print(tuplas)

diccionarios = {"estudiante": "Juanito", "Sexo": "Masculino", "Nota": 85}
print(diccionarios)

diccionarios["Nota"]= 80
print(diccionarios)

NuevaLista = []
NuevaLista.extend(listas)
NuevaLista.extend(conjuntos)
NuevaLista.extend(tuplas)
NuevaLista.extend(diccionarios)
print(NuevaLista)

for item in NuevaLista:
    print(item)
    
for item in NuevaLista:
    print(type(item))
    
with open("texto.txt", "+w", encoding="utf-8") as archivo:
    for item in NuevaLista:
        archivo.write(str(item) + "\n")

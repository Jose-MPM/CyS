from collections import Counter

# Abre el archivo de texto y lee todo el contenido del archivo
with open('archivo1.txt', 'r') as file:
    original = file.read()

with open('archivo2.txt', 'r') as file:
    cifrado = file.read()

def cleantxt(lst):
    # Divide el contenido en parejas de caracteres
    parejas = [(lst[i], lst[i+1]) for i in range(0, len(lst)-1, 2)]
    # Convierte todas las parejas a mayúsculas
    parejas_mayusculas = [(c1.upper(), c2.upper()) for c1, c2 in parejas]
    # Guarda las parejas en una lista
    lstC = list(parejas_mayusculas)
    return lstC
def joinlsts(lst1,lst2):
    """
    Toma dos listas y devuelve una lista de duplas donde cada elemento es un par formado por un elemento de cada lista.
    """
    if len(lst1) != len(lst2):
        raise ValueError('Las listas deben tener la misma longitud')
    return list(zip(lst1, lst2))


def ordenar_por_frecuencia(lista):
    """
    Toma una lista de elementos y devuelve una lista ordenada de mayor a menor según su frecuencia de aparición.
    """
    conteo = Counter(lista)  # Obtenemos un objeto Counter con el conteo de cada elemento
    return [elem for elem, _ in conteo.most_common()]  # Devolvemos una lista ordenada de mayor a menor frecuencia








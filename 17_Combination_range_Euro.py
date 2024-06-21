import itertools
import random

def generar_combinaciones_loteria():
    numeros = list(range(1, 51))  # Números de la lotería primitiva
    

    combinaciones_validas = []
    
    # Generar todas las combinaciones posibles de 5 números
    todas_combinaciones = itertools.combinations(numeros, 5)
    
    for combinacion in todas_combinaciones:
        suma_combinacion = sum(combinacion)
        if 130 < suma_combinacion < 140:
            estrellas = random.sample(range(1, 13), 2)
            combinaciones_validas.append((combinacion, estrellas))

    # Seleccionar aleatoriamente 5 combinaciones de las válidas
    if len(combinaciones_validas) >= 8:
        combinaciones_seleccionadas = random.sample(combinaciones_validas, 8)
    else:
        combinaciones_seleccionadas = combinaciones_validas
    
    return combinaciones_seleccionadas

# Ejemplo de uso
resultados = generar_combinaciones_loteria()
for combinacion in resultados:
    print(f"Combinación: {combinacion}")

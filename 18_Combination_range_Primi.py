import itertools
import random

def generar_combinaciones_loteria():
    numeros = list(range(1, 50))  # Números de la lotería primitiva
    combinaciones_validas = []
    
    # Generar todas las combinaciones posibles de 6 números
    todas_combinaciones = itertools.combinations(numeros, 6)
    
    for combinacion in todas_combinaciones:
        suma_combinacion = sum(combinacion)
        if 130 < suma_combinacion < 140:
            combinaciones_validas.append(combinacion)
    
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

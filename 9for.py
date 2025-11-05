# suma = 0
# for x in range(10):
#     num = int(input("ingrese un numero"))
#     if x >= 5:
#         suma = suma + num
# print(suma)


positivo = 0
negativo = 0
for x in range(10):
    num = int(input(f"Ingrese el valor : "))
    
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1


# Mostramos resultados
print("resultados positivos:", positivo)
print("resultados negativos:", negativo)

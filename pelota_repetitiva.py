# Ejercicio de la pelota rebotante :Hacer el diagrama de flujo y el programa en python, que lea "h" y que calcule e imprima en cual rebote la pelota no alcanza a subir la quinta parte de la altura inicial.

print("________________________________________")
print("|Altura de la pelota de su quinta parte |")
print("|_______________________________________|")
print("")

# input
h = int(input("Dijite la altura de la pelota en cm: "))
h1 = h
i = 0

#process
while h1 >= h/5: 
    h1 = h1 - h1 * 0.10
    i = i + 1 
else:
    print("los",h,"cm de la altura de la pelota,en el rebote",i, ",fue de ",h1,"cm de altura")
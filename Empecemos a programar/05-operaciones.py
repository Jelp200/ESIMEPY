# Para poder realizar el ingreso de datos en PY lo que necesitamos es la palabra reservada *input()*

n1 = int(input("De el primer número: "))
n2 = int(input("De el segundo número: "))

S = n1 + n2
R = n1 - n2
P = n1 * n2
D = n1 / n2
Dint = n1 // n2
M = n1 % n2
# P = pow(n1, 2)                                                # Se eleva al cuadrado la variable

print(f"Los resultados son los siguientes...\nLa suma de {n1} y {n2} es: {S}\nLa resta de {n1} y {n2} es: {R}\nEl producto de {n1} y {n2} es: {P}\nEl cociente de {n1} y {n2} es: {D}\nEl cociente entero de {n1} y {n2} es: {Dint}\nEl modulo de {n1} y {n2} es: {M}")

print(f"\n\nLa suma es de tipo: {type(S)}"), print(f"La resta es de tipo: {type(R)}"), print(f"El producto es de tipo: {type(P)}"), print(f"El cociente es de tipo: {type(D)}"), print(f"El cociente entero es de tipo: {type(Dint)}"), print(f"El modulo es de tipo: {type(M)}")
def biseccion(func, a:float, b:float, tol:float =1e-6, max_iter:int =100):


    # Verificar  que el intervalo inicial tenga una raiz
    if func(a) * func(b) >= 0:
        print("El intervalo no es valido. Debe tener f(a) * f(b) < 0.")

        return None

    #Variables iniciales
    iteracion = 0

    c = a

    while a + (b-a)/2 > tol and iteracion < max_iter:
        # Calcular el punto medio
        c = a + (b-a)/2
        # Evaluar la funvion en el punto medio
        fc = func(c)
        

        # Criterio de parada si se encuentra la raiz exacta
        if fc==0 or a + (b-a)/2 < tol:
            break

        # Decidir el nuevo intervalo

        if func(a) * fc < 0:
            b = c

        else:
            a = c

        iteracion += 1 
        print (f"Iteracion {iteracion}: a = {a}, b = {b}, c = {c}, f(c) = {fc}")

    print(f"La raiz aproximada es: {c}")

    return c 

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la función
    def funcion(x):
        return x**3 - 6*x**2 + 11*x - 6.1   # Ejemplo: queremos la raíz de x^2 - 4

    # Llamar al método de bisección
    raiz = biseccion(funcion, 2, 4)
    print("Raíz encontrada:", raiz)


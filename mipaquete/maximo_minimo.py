def encontrar(lista):
    maximo = lista[0]
    
    for numero in lista:
        if numero > maximo:
            maximo = numero
    print(f"El numero maximo de la lista es: {maximo}")
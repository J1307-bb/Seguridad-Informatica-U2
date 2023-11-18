def promediar():
    materias = int(input("Ingresa el numero de materias a promediar:"))
    calificacion_total = 0
    
    for i in range(materias):
        calificacion=int(input(f"Ingresa la calificacion #{i+1}"))
        calificacion_total = calificacion_total + calificacion
        
    resultado = calificacion_total/materias
    if resultado == 10:
        emoji = "🧑‍🎓"
    elif resultado >= 8 :
        emoji = "😎"
    elif resultado > 6:
        emoji = "😒"
    else:
        emoji = "😰"
        
    print(f"Tu promedio es de: {round(resultado, 2)} {emoji}")
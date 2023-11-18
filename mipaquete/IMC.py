def calculadora(miPersona):
    nombre = miPersona["nombre"]
    peso = miPersona["peso"]
    altura = miPersona["altura"]**2
    IMC = peso / altura
    InMaCo = round(IMC, 2)
    
    if IMC >= 30:
        nivelPeso = "Obesidad"
    elif IMC >= 25:
        nivelPeso = "Sobrepeso"
    elif IMC > 18.5:
        nivelPeso = "Normal"
    else:
        nivelPeso = "Bajo peso"
        
    print(f"Hola {nombre}, tu IMC es de {InMaCo} y tu peso se considera como: {nivelPeso}")
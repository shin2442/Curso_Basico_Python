def promedio(n_1, n_2, n_3, n_4, n_5):
    return (n_1 + n_2 + n_3 + n_4 + n_5) / 5  

def obtener_5_notas():
    print("Hola, vamos a calcular tu promedio\nPara calcular tu promedio ingresa las 5 notas\n(Solo números)\t (Del 1 al 100)")
    
    n_1 = int(input("¿Cuál es tu primera nota? "))
    n_2 = int(input("¿Cuál es tu segunda nota? "))
    n_3 = int(input("¿Cuál es tu tercera nota? "))
    n_4 = int(input("¿Cuál es tu cuarta nota? "))
    n_5 = int(input("¿Cuál es tu quinta nota? "))

    total = promedio(n_1, n_2, n_3, n_4, n_5)
    
    print(f"Tu promedio es: {total}")  
    
    if total >= 80:
        print("¡Pasaste!")
    else:
        print("¡Perdiste!")

obtener_5_notas()

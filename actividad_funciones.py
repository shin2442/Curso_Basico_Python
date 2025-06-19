print("Bienvenido al converson de monedas \n")
"""
Este programa es un conversor de monedas que permite convertir valores entre dólares, euros y otras monedas como pesos colombianos, yuanes y libras esterlinas.
Preguntas y respuestas:
1. ¿Cuánto equivale 50 dólares en pesos colombianos?
    50 dólares * 3750 = 187,500 pesos colombianos.
2. ¿Cuánto equivale 30 euros en yuanes?
    30 euros * 6.93 = 207.9 yuanes.
3. ¿Cuánto equivale 15 euros en libras esterlinas?
    15 euros * 0.83 = 12.45 libras esterlinas.
"""
def conversor(moneda_actual,valor,moneda_a_convertir):
    if moneda_actual ==1:
        def dolarTo():
            if moneda_a_convertir=="1":
                print(f'{valor} dolares equivale a ${valor * 3750} pesos colombianos')
            elif moneda_a_convertir =="2":
                print(f'${valor} dolares equivale a ${valor*6.37} yuanes')
            elif moneda_a_convertir=="3":
                print(f'${valor} dolares equivale a ${valor*0.76} libras esterlinas')
            else:
                print("No se reconoce la moneda a convertir")
        dolarTo()
    elif moneda_actual ==2:
        def euroTo():
            if moneda_a_convertir=="1":
                print(f'${valor} euros equivale a ${valor*4000} pesos colombianos')
            elif moneda_a_convertir=="2":
                print(f'${valor} euros equivale a ${valor*6.93} yuanes')
            elif moneda_a_convertir=="3":
                print(f'${valor} euros equivale a ${valor*0.83} libras esterlinas')
            else:
                print("No se reconoce la moneda a convertir")
        euroTo()
    else:
        print("No se reconoce la moneda a convertir")
    moneda_actual=int(input("Ingrese su moneda actual: \n 1. Dolar \n 2. Euro"))
    valor=float(input("Ingrese el valor a convertir: \n"))
    moneda_a_convertir=input(
        "¿A qué moneda quiere convertirlo? \n 1. Pesos Colombianos "
        "\n 2. Yuanes \n 3. Libras Esterlinas \n")
    

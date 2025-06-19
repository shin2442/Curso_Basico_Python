def ejemplo_listas():
    #Ejemplo de uso de listas
    mi_lista = ['Juan','Pedro','Laura','Carmen','Susana']
    print(mi_lista[0])
    print(mi_lista[-1])
    print(mi_lista[1])
    print(mi_lista[2])
    print(mi_lista[-2])
    print("")
def recoriendo_arreglos_ejemplo():
    #Recorriendo arreglos ejemplo (usando funcion len)
    edades=[20,41,6,18,23]
    for edad in edades:
    print(edad)
    for i in range(len(edades)):
        print(edades[i])
    indice=0
    while indice<len(edades):
        print(edades[indice])
        indice +=1
    print("")
def agregar_elementos():
    #agregado elementos a undo append()
    numeros =[]
    numeros.append(10)
    numeros.append(5)
    numeros.append(3)
    print(numeros)
    #mostrara [10, 5, 3]
    print("")
def removiendo_elementos():
    #removiendo un elemento usando pop()
    palabras=['hola','hello','hello','ola']
    palabras.pop(1)
    print(palabras)
    #mostrara ['hola','hello','ola']
    print("")
#Resumen, append() agrega elementos al final de la lista, pop() quita elementos en el indice que se le indica, remove quita la concidencia
def remove_funcion_elementos():
    #Remove
    palabras=['hola','hello','hello','ola',]
    palabras.remove('hello')
    print(palabras)
    #mostrara ['hola','hello','hola']
#Reto: Queremos crear un programa con el cual podamos guardar los nombres y las identificacines de multiples personas( no sabemos cuantas)sin perder ninguna de ellas. El usuario es el en cargado de suministrar la informacion de cada persona.
def ejemplo_tablas():
    #tablas
    nombre_de_la_tabla = []
    #poner una tabla en una tabla
    nombre_de_la_tabla_ = [[],[]]

    mi_tabla =[['juan','laura'],[21,32]]
    print(mi_tabla[0][0])
    print(mi_tabla[-1][1])
    print(mi_tabla[1][2])
    print(mi_tabla[2][-2])
def ejemplo_2_tablas():
    #otro ejemplo
    usuarios = [[],[]]
    tamaño=3
    for i in range(tamaño):
        print("ingrese los datos de la persona",i+1)
        nombre = input("nombre: ")
        indentificacion =input("identificacion: ")
        usuarios[0].append(nombre)
        usuarios[1].append(indentificacion)
    #mostrar los valores
    for i in range(tamaño):
        print("mostrando los datos de la persona",i+1)
        print("nombre: ", usuarios [0][i])
        print("identificacion: ",usuarios[1][i])
def diccionarios():
    mi_diccionario ={
        "nombre":"juan",
        "edad":"23",
        "usuario":"jn23"
        }
    #recorriendo los elementos:
    for llave in mi_diccionario:
        print(llave,":", mi_diccionario[llave],sep='')
def ejemplo_2_diccionario():
    usuarios = {
        "nombres": []
        "identificaciones":[]
        }
    tamaño =3
    for i in range(tamaño):
        print("ingrese los datos de la persona",i +1)
        nombre=input("nombre: ")
        identificacion=input("identificacion: ")
        usuarios["nombres"].append(nombre)
        usuarios["identificaciones"].append(identificacion)
    for i in range(tamaño):
        print("mostrando los datos de la persona",i+1)
        print("nombre:",usuarios["nombres"][i])
        print("identificacion:",usuarios["identificaciones"][i])
def diccionarios_3():
    diccionario={'nombre':'alberto','edad':30}
    print(diccionario)
    resultado=diccionario['edad']
    print(resultado)
def ejemplo_4_diccionarios():
    dic={'ci':55,'c2':[3,4],
         'c3':{'nombre':'roro'}}    
    print(dic["c2"][1])
    #para poner un diccionario dentro de un diccionario.
def agregar_elementos_diccionario():
    mi_dic={'1':'a','2':'b'}
    print(mi_dic)
    mi_dic['3']='c'
    print(len(mi_dic))  
    print(mi_dic)
    #3 metodos mas utilizados en diccionarios
    print(mi_dic.keys())
    print(mi_dic.values())
    print(mi_dic.items())
def tuples_en_diccionarios():
    mi_tuple=(1,2,3,4)
    print(type(mi_tuple))
    print(mi_tuple[2])
    #print = 3
    #ejemplo tuple
    t=(1,2,3)
    x,y,z=t
    print(x)
    print(y)
    print(z)
    #otro ejemplo
    m=(1,2,3,4)
    print(m.)
    #otra forma de usarlo
    j=(1,2,3,1)
    print(t.count(1))
#reto lunes: buscar una palabra en un texto.
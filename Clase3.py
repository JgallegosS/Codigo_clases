class For:
    def __init__(self):
        pass
        # ciclo repetitivo de incrementos o decrementos se ejecura por verdadero

    def usoFor(self):
        datos = ["Josue", 20, True]
        numeros = (2,5,6,4,1)
        docente = {"nombre":"Josue", "edad":20, "fac":"faci"}
        listaNotas = [(30,40),(20,40),(50,40)]
        # range ([inicio=0],limite, [inc/dec=1]). Genera un rango
        # se ejecuta desde inicio hasta el limite
        # for i in range(5): rango(0,1,2,3,4)
        #     print("i={}".format(i))
        # for i in range(2,10): # range(2,3,4,5,6,7,8,9)
        #     print("i={}".format(i))
        # for i in range(4,10,2): #range(4,6,8)
        #     print("i={}".format(i), end=" ")
        # for i in range(12,3,-3): # range(12,9,6)
        #     print("i={}".format(i))
        longitud = len(datos)
        # print(datos[0])
        # print(datos[1])
        # print(datos[2])
        # j = 0
        # while j < longitud:
        #     print("While", datos[j])
        #     j += 1
        # for i in range(longitud-1,-1,-1):
        # #     print(datos[i])
        # for i, dato in enumerate(datos):
        #     print("for", i, dato)
        # Dato toma caracter por caracter de la coleccion de numeros(cadena.lista.tupla)

        # for dato in numeros:
        #     print(dato)

        # for dato in ["H","o","l","a","que","tal"]:
        #     print(dato)

        print("\nDiccionario de notas")
        # for clave,valor in docente.items():
        #     print(clave, ":", valor, end="  ")

        # for alumnos in listaAlumnos:
        #     for clave,valor in alumnos.items():
        #         print(clave,":",valor, end=" ")

        # listaNotas = [(30,40),(20,40,20),(50,40,20,10)]
        # acum = 0
        # long = 0
        # for notas in listaNotas:
        #     parcial = 0
        #     print(notas)
        #     print(notas,end="")
        #     for nota in notas:
        #         print(nota)
        #         acum += nota
        #         long += 1
        #         parcial += nota
        #     promParcial = parcial/len(notas)
        #     print("Notas parciales = {}, Promedio Parcial = {}".format(parcial,promParcial))
        # prom = acum/long
        # print("Total de notas {}, #notas {} y su promedio es {}".format(acum,long,prom))
        # listaAlumnos = [{"nombre": "Erick", "Final": 70}, {"nombre": "Yady", "Final": 60},{"nombre": "Danny", "Final": 90}]
        # acum = 0
        # cont = 0
        # for alumnos in listaAlumnos:
        #     print(alumnos)
        #     for clave,valor in alumnos.items():
        #         print(clave,":",valor,end="")
        #         if clave =="Final": acum = acum+valor
        #     cont += 1
        # print(acum/cont)
        frase = "Hola mundo"
        for cara in frase:
            if cara in ('a','e','i','o','u'):
                print(cara)

bucle1 = For()
bucle1.usoFor()

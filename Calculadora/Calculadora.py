#Calculadora por Joel Franco
Intro = """
          CALCULADORA

Para utilizar la calculadora es necesario introducir dos numeros
a los cuales vamos a operar, despues seleccionar la operacion que 
se quiere realizar
"""
Selec_Operacion ="""
Seleccione la operacion de su eleccion
1.- Suma
2.- Resta
3.- Multiplicacion
4.- Division
"""
print(Intro)
print("Intruduce el primer numero")
def lee_numero():
    while True:
        entrada = input("Escribe un numero : ")
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            print ("La entrada es incorrecta: solo se permite la entrada de datos numericos, por favor escribe un numero ")

n1 = lee_numero()
#print("n1 ={t} y es del tipo {y}".format(y= type (n1), t=n1))
print("Intruduce el segundo numero")
def lee_numero():
    while True:
        entrada = input("Escribe un numero: ")
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            print ("La entrada es incorrecta: solo se permite la entrada de datos numericos, por favor escribe un numero")
n2 = lee_numero()
#print("n2 ={t} y es del tipo {y}".format(y= type (n2), t=n2))


while True:    
    print(Selec_Operacion)
    Op = input()
    
    if Op == "Suma":
            print("la suma de {} + {} tiene como resultado {} ".format(n1,n2,n1+n2))
            break
    if Op == "Resta":
        print("la resta de {} - {} tiene como resultado {} ".format(n1,n2,n1-n2))
        break   
    if Op == "Multiplicacion":
        print("la multiplicacion de {} * {} tiene como resultado {} ".format(n1,n2,n1*n2))
        break
    if Op == "Division":
        if n1 == 0 or n2 == 0:
            print("Dividir entre cero o dividir cero no esta permitido intente nuevamente")
        else:
            print("las division de {} / {} tiene como resultado {} ".format(n1,n2,n1/n2))
    if Op != "Suma" or "Resta" or "Multiplicacion" or "Division":
        print("Introduza una opcion valida, ejemplo: Suma")
            
    

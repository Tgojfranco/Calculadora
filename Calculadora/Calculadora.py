
Intro = """
          CALCULADORA

Para utilizar la calculadora es necesario introducir dos numeros
a los cuales vamos a operar, despues seleccionar la operacion que 
se quiere realizar
"""
Selec_Operacion ="""
Selecciona la operacion de su eleccion
1.- Suma
2.- Resta
3.- Multiplicacion
4.- Division
"""
print(Intro)
print("Intruduce el primer numero")
n1 =int (input())
print("Intruduce el segundo numero")
n2 =int (input())
print(type (n1))
print(Selec_Operacion)
Op = input()

if Op == "Suma":
    print("la suma de {} + {} tiene como resultado {} ".format(n1,n2,n1+n2))
if Op == "Resta":
    print("la resta de {} - {} tiene como resultado {} ".format(n1,n2,n1-n2))
if Op == "Multiplicacion":
    print("la multiplicacion de {} * {} tiene como resultado {} ".format(n1,n2,n1*n2))
if Op == "Division":
    if n1 == 0 or n2 == 0:
        print("Dividir entre cero o dividir cero no esta permitido intente nuevamente")
    else:
        print("las division de {} / {} tiene como resultado {} ".format(n1,n2,n1/n2))
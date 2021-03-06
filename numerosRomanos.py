#encoding: UTF-8
#Autor: Marina Itzel Haro Hernández, A01373471
#El programa lee un número entre 1 y 10 e imprime el número romano correspondiente  


#Convierte el número Arábigo que nos da el usuario a número Romano
def convertirArabigoARomano(numeroArabigo):
    if numeroArabigo>0 and numeroArabigo<4:
        return (numeroArabigo*"I")
    elif numeroArabigo == 4:
        return ("IV")
    elif numeroArabigo>4 and numeroArabigo<9:
        return ("V"+"I"*(numeroArabigo-5))
    elif numeroArabigo>8 and numeroArabigo<11:
        return ("I"*(abs(numeroArabigo-10))+"X") #usamos abs para que nos diera el valor absoluto de la operación
    else:
        return ("Error (No es un número en el rango pedido)")
 
       
#Llamamos la función anterior para poder imprimir el número romano que corresponda       
def main():
    numeroArabigo = int(input("Pon un número del 1 al 10"))
    arabigoARomano = convertirArabigoARomano(numeroArabigo)
    print("El número en romano es:", arabigoARomano)
    
main()        
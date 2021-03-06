#encoding: UTF-8
#Autor: Marina Itzel Haro Hernndez, A01373471 
#Este programa dependiendo de cuantos paquetes de $1500 compres te indica el precio final con el descuento correspondiente

#Función para calcular el pago total con el decuento aplicado
def calcularDescuento(costoDePaquete, paquetes):
    if paquetes < 10 and paquetes > 0:
        return (costoDePaquete*paquetes)
    elif paquetes >= 10 and paquetes <= 19:
        return (costoDePaquete*paquetes) * 0.8
    elif paquetes >= 20 and paquetes<=49:
        return (costoDePaquete*paquetes) * 0.7
    elif paquetes >= 50 and paquetes<=99:
        return (costoDePaquete*paquetes) * 0.6
    elif paquetes >= 100:
        return (costoDePaquete*paquetes) * 0.5
    elif paquetes < 0:
        return -1
    
    
#Definimos el costo del paquete, la cantidad que es dada por el usuario y llamamos la función para calcular el descuentp
def main():
    costoDePaquete = 1500
    paquetes = float(input("Cuántos paquetes de $1500 compraste"))
    descuento = calcularDescuento(costoDePaquete, paquetes)
    if descuento == -1:
        print ("Error: numeros negativos no validos")
    else:
        print ("El precio total a pagar con el descuento aplicado es de: $%i" % (descuento))
      
    
   
     
main()
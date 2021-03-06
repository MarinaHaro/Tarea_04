#encoding: UTF-8
#Autor: Marina Itzel Haro Hernández, A01373471
#Este programa lee las dimensiones de dos rectángulos y calcula el perímetro y área de ambos   


from Graphics import*

#Recibe las dimensiones y calcula el área
def calcularArea(base, altura):
    area = base*altura
    return area
    
#Recibe las dimensiones y calcula el perímetro
def calcularPerimetro(base, altura):
    perimetro = base*2 + altura*2
    return perimetro

#Compara las áreas de los dos rectangulos 
def compararAreas(area1, area2):
    if area1>area2:
        return ("El primer rectángulo tiene mayor área")
    elif area1<area2:
        return ("El segundo rectángulo tiene mayor área")
    elif area1 == area2:
        return ("Sus áreas son iguales")
        
#Dibuja los dos rectangulos con diferente color
def dibujarRectangulos(base1, altura1, base2, altura2):
    v = Window("Rectángulos", 800, 800)
    t = Arrow ((100, 400), 0)
    t.draw(v)
    t.penDown()
    t.pen.color = Color("Green")
    #primer rectangulo
    t.forward(base1)
    t.rotate(90)
    t.forward(altura1)
    t.rotate(90)
    t.forward(base1)
    t.rotate(90)
    t.forward(altura1)
    t.rotate(90)
    
    t.penUp()
    t.forward(base1+200)
    t.penDown()
    
    #segundo rectangulo
    t.pen.color = Color("Blue")
    t.forward(base2)
    t.rotate(90)
    t.forward(altura2)
    t.rotate(90)
    t.forward(base2)
    t.rotate(90)
    t.forward(altura2)
    t.rotate(90)
        
        
        
def main():
    base1 = int(input("Coloca la medida en metros de la base del primer rectángulo"))
    altura1 = int(input("Coloca la medida en metros de la altura del primer rectángulo"))
    base2 = int(input("Coloca la medida en metros de la base del segundo rectángulo"))
    altura2 = int(input("Coloca la medida en metros de la altura del segundo rectángulo"))
    area1 = calcularArea(base1, altura1)
    perimetro1 = calcularPerimetro(base1, altura1)
    area2 = calcularArea(base2, altura2)
    perimetro2 = calcularPerimetro(base2, altura2)
    print("Del primer rectángulo su área es:", area1, "m  y su perímetro es:", perimetro1, "m")
    print("Del segundo rectángulo su área es:", area2, "m  y su perímetro es:", perimetro2, "m")
    areas = compararAreas(area1, area2)
    print (areas)
    dibujarRectangulos(base1, altura1, base2, altura2)
    
main()
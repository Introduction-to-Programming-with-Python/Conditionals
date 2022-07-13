import condicionales as ifs

def ejecutar_bisiesto()->None:
    print("Vamos a determinar si un anio es bisiesto o no.")
    anio=int(input("Ingrese un año: "))
    resultado=ifs.bisiesto(anio)
    print(resultado)
    

def ejecutar_clasificar()->None:
    print("Vamos a determinar de qué tipo es un triángulo dados sus ángulos.")
    a1=int(input("Ingrese la medida del angulo 1: "))
    a2=int(input("Ingrese la medida del angulo 2: "))
    a3=int(input("Ingrese la medida del angulo 3: "))
    resultado=ifs.clasificar(a1, a2, a3)
    print(resultado)

def ejecutar_solucionar()->None:
    print("Vamos a tratar de hallar las soluciones de una ecuación cuadrática.")
    a=int(input("Ingrese el valor de a: "))
    b=int(input("Ingrese el valor de b: "))
    c=int(input("Ingrese el valor de c: "))
    resultado=ifs.solucionar(a, b, c)
    print(resultado)

def mostrar_menu()->None:
    print ("Menu principal")
    print ("(1) Año bisiesto")
    print ("(2) Tipo de triángulo")
    print ("(3) Solución ecuación cuadrática")
    
    x = int(input("Seleccione su opción: "))
    
    if x==1:
        d=ejecutar_bisiesto()
    
    elif x==2:
        d=ejecutar_clasificar()
    
    elif x==3:
        d=ejecutar_solucionar()
    
    return d


def iniciar_aplicacion()->None:
    print("Bienvenido al laboratorio de condicionales")
    mostrar_menu()
    

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

    
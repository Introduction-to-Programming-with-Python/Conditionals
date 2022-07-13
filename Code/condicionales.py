import math

#Calcular si un año es bisiesto

def bisiesto(anio:int)->bool:
  
    """
    Retorna True si es anio bisiesto o False de lo
    contrario

    Parameters
    ----------
    anio : int
        Año.

    Returns
    -------
    bool
        Valor de True o False.

    """
    
    if anio%4>0:
        respuesta=False    
        
    elif anio%100>0:
        respuesta=True

    elif anio%400>0:
        respuesta=False
        
    else:
        respuesta=True
        
    if respuesta==True:
        
        return "El anio es bisiesto"
    
    else:
        
        return "El anio no es bisiesto"

print(bisiesto(2040))


def clasificar(a1:float, a2:float, a3:float)->str:
   
    """
    
    La funcion retorna que tipo dse triangulo
    es, segun las medidas de sus angulos.

    Parameters
    ----------
    a1 : float
        Medida del angulo 1.
        
    a2 : float
        Medida del angulo 2.
        
    a3 : float
        Medida del angulo 3.

    Returns
    -------
    str
        DESCRIPTION.

    """
    
    a=a1
    b=a2
    c=a3
    
    if a+b+c>180:
        respuesta="Las medidas son incorrectas, la suma de los angulos de un triangulo debe ser 180."
    
    elif a==b and b==c:
        respuesta="El triangulo es equilatero."
    
    elif a!=b and b!=c:
        respuesta="El triangulo es escaleno."
        
    elif a==c and c!=b:
         respuesta="El triangulo es isosceles"
        
    elif a==b and a!=c:
         respuesta="El triangulo es isosceles"
        
    return respuesta

print(clasificar(150, 30, 1))


#Calcular ecuacion cuadratica


def solucionar(a:float, b:float, c:float)->str:
    """
    
    La funcion soluciona ecuaciones cuadraticas.

    Parameters
    ----------
    
    a : float
        Valor de a en la ecuacion.
        
    b : float
        Valor de b en la ecuacion.
        
    c : float
        Valor de c en la ecuacion.
        

    Returns
    -------
    str
        Soluciones de la ecuacion.

    """
    
    if a==0:
        respuesta1="La ecuacion no tiene solucion en a=0."
        return respuesta1
        
    if a>0:
        
        x1=((-(b)+math.sqrt((b**2)-(4*a*c)))/(2*a))
        respuesta1="La primera solucion de la ecuacion es "+str(x1)
        
        x2=((-(b)-math.sqrt((b**2)-(4*a*c)))/(2*a))
        respuesta2=" y la segunda solucion de la ecuacion es "+str(x2)+"."
        
    return str(respuesta1)+str(respuesta2)

print(solucionar(2, 9, 10))
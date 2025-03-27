import QR
import Solucion as Sol

n = 0
m = 0

# Función para comprobar que los valores ingresados son números reales
def intComprobacion(digit):
    try:
        int(digit)
        return digit
    except ValueError:
        print("\033[31mEl valor ingresado no es un número válido\n\033[0m")
        return None

# Función para la creación de la matriz A
def makeMatrix(n, m):
    print("A continuación deberá ingresar los dígitos correspondientes a la Matriz A \n ")
    Matrix = []
    for fila in range(n):
        row = []
        print("Fila "+str(fila+1))
        for digit in range(m):
            d = None
            while d == None:
                d = input("Ingrese el dígito a"+str(fila+1)+str(digit+1)+": ").strip()
                d = intComprobacion(d)
                if d != None:
                    d=float(d)
                    row.append(d)
                else:
                    d = None
        Matrix.append(row)
    print("Se ha estalecido la matriz A \n ")
    return Matrix

# Función para la creación de la matriz b
def makeMatrixB(n):
    print("A continuación deberá ingresar los digitos correspondientes a la Matriz b \n ")
    Vector = []
    for digit in range(n):
        d = None
        while d == None:
            d = input("Ingreseel dígito a1"+str(digit+1)+": ").strip()
            d = intComprobacion(d)
            if d != None:
                d=float(d)
                Vector.append(d)
            else:
                d = None
    print("Se ha estalecido la matriz b \n ")
    return Vector

#Función para comprobar que la matriz no sea nula
def matrixComprobacion(Matrix, Vector, a):
    null = 1
    for i in Matrix:
        for j in i:
            if j != 0:
                null = 0
    if null == 1:
        return False
    else:
        return True
    

#PROGRAMA EN EJECUCIÓN
n = None
m = None
while n == None or m == None:
    n = input("Por favor ingrese el número de filas de la matriz: ")
    m = input("Por favor ingrese el número de columnas de la matriz: ")
    if intComprobacion(n) != None:
        n = int(n)
    if intComprobacion(m) != None:
        m = int(m)
Matrix = makeMatrix(n, m)
Vector = makeMatrixB(n)
print("Se procese a ejecutar factorización QR...")
Q, R, msg = QR.factorizacion_qr(Matrix)
print("\nMensaje:", msg) 
if Q != None:
    Sol.SolucionQR(Q, R, Vector)

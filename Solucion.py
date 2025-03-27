import GaussJordan as GJ

def printMatrix(Matrix):
    for i in range(4):
        for j in range(4):
            print(str(Matrix[i][j]), end="  ")

def SolucionQR(Q, R, b):
    n = len(Q)
    m = len(R)
    QR = [[0 for _ in range(m)] for _ in range(n)]

    #Se multiplican las matrices Q y R para formar QR
    for i in range(n):
        for j in range(m):
            suma_producto = 0
            for k in range(m): 
                Ta = Q[i][k]
                Tb = R[k][j]
                suma_producto += Ta * Tb
            QR[i][j] = suma_producto

    GJ.SolGaussJordan(QR, b)
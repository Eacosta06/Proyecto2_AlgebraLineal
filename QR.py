import math

def factorizacion_qr(A):
    """
    Factoriza una matriz A en QR usando el proceso de Gram-Schmidt.
    
    Args:
        A (matriz): Matriz de tamaño m x n (puede ser no cuadrada).
    
    Returns:
        Q (matriz): Matriz ortonormal de tamaño m x n.
        R (matriz): Matriz triangular superior de tamaño n x n.
        mensaje (str): "Las columnas de A son LI" o "Las columnas de A son LD".
    """
    m = len(A)       # Número de filas
    n = len(A[0]) if m > 0 else 0  # Número de columnas
    
    if m == 0 or n == 0:
        return None, None, "Matriz vacía"
    
    #  Calcular Q y verificar si las columnas son LI
    Q = gram_schmidt(A)
    if Q is None:
        return None, None, "Las columnas de A son LD (no se puede factorizar QR completamente)"
    
    #  Calcular R = Q^T * A
    R = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            R[i][j] = sum(Q[k][i] * A[k][j] for k in range(m))  # Producto punto entre Q[:,i] y A[:,j]
    
    # Mostrar A = QR al final
    mostrar_factorizacion(A, Q, R)
    
    return Q, R, "Las columnas de A son LI"

def gram_schmidt(A):
    """
    Aplica el proceso de Gram-Schmidt a las columnas de A para obtener Q.
    Si las columnas son LD, retorna None.
    Imprime cada vector ortonormal obtenido en cada paso.
    """
    m = len(A)
    n = len(A[0])
    
    Q = [[0.0 for _ in range(n)] for _ in range(m)]
    for j in range(n):
        # Tomar la columna j-ésima de A
        v = [A[i][j] for i in range(m)]
        
        # Restar las proyecciones sobre los vectores anteriores
        for k in range(j):
            q_prev = [Q[i][k] for i in range(m)]
            proj_coeff = sum(v[i] * q_prev[i] for i in range(m))  # Producto punto v · q_k
            for i in range(m):
                v[i] -= proj_coeff * q_prev[i]
        
        # Normalizar el vector resultante
        norm = math.sqrt(sum(vi ** 2 for vi in v))
        if norm < 1e-10:  # Si la norma es casi cero, las columnas son LD
            return None
        
        for i in range(m):
            Q[i][j] = v[i] / norm
        
        # Imprimir el vector ortonormal obtenido
        print(f"Vector ortonormal q_{j+1}: {[round(Q[i][j], 4) for i in range(m)]}")
    
    return Q

def mostrar_factorizacion(A, Q, R):
    """
    Muestra las matrices A, Q, R y la ecuación A = QR.
    Los valores muy cercanos a cero se muestran como 0.
    """
    # Función para reescribir valores cercanos a cero como cero
    def limpiar_valor(x, tolerancia=1e-10):
        return 0.0 if abs(x) < tolerancia else x
    
    print("\nMatriz A:")
    for fila in A:
        print([limpiar_valor(x) for x in fila])
    
    print("\nMatriz Q:")
    for fila in Q:
        print([limpiar_valor(x) for x in fila])
    
    print("\nMatriz R:")
    for fila in R:
        print([limpiar_valor(x) for x in fila])
    
    print("\nPor lo tanto, A = QR.")

 # Matriz de ejemplo (2x2)
A = [
        [1, 2],
        [3, 4],
        [9, 8],
    ]

 # msg es para mostrar si A es LI o no
Q, R, msg = factorizacion_qr(A)

print("\nMensaje:", msg)  
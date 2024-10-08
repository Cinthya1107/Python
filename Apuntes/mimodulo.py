#Ejemplo de modulo
def fibonacci(n):
    """Calcula el n-esimo elemento de la serie de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def genera_multiplicador(n):
    return lambda x: x* n

doblar = genera_multiplicador(2)
triplicar = genera_multiplicador(3)
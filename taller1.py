
# 1. Defina una funcion lambda que calcule el  ́area de un triangulo dado el lado y altura,
# reciba los valores por teclado, luego imprima por consola el resultado, adem ́as debe
# verificar que los valores son positivos.
import math
# triangleArea = lambda b,h:(b*h)/2
triangleArea = lambda b,h:(b*h)/2
print("triangleArea(3,5)")
print(triangleArea(3,5))


# 2. Defina una funcion que pueda hallar el numero mas grande de una lista y lo retorne y ası
# mismo el numero mınimo.
def maximum(list):
    maxValue = None
    for num in list:
        if (maxValue == None or num > maxValue):
            maxValue = num
    return maxValue
print("maximum([52,9,7,3,63,8,10,105])")
print(maximum([52,9,7,3,63,8,10,105]))

def minimum(list):
    minValue = None
    for num in list:
        if (minValue == None or num < minValue):
            minValue = num
    return minValue
print("minimum([52,9,7,3,63,8,10,105])")
print(minimum([52,9,7,3,63,8,10,105]))


# 3. Defina unas funciones que calculen e de Euler segun la definicion sumatoria, realice una
# iterativa y otra recursiva.
def factIt(n):
    if n < 0:
        return None

    elif n == 0:
        return 1

    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

def factRec(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factRec(n - 1)

def euler():
    lim = 100
    e = 0

    for n in range(lim):
        # e += 1/factIt(n)
        e += 1/factRec(n)
    return e
print("euler()")
print(euler())


# 4. Desarrolle una funcion que pueda resolver un sistema de n ecuaciones con n incognitas,
# por reduccion de Gauss.
def gauss(matrix):
    piv = 0
    rows = len(matrix)
    for k in range(rows):
        temp = matrix[piv][piv]
        for y in range(rows + 1):
            matrix[piv][y] = matrix[piv][y] / temp
        for i in range(rows):
            if (i != piv):
                c = matrix[i][piv]
                for j in range(rows + 1):
                    matrix[i][j] = ((-c) * matrix[piv][j]) + matrix[i][j]
        piv += 1
    return matrix

print("gauss([[2, -1, 1, 2], [3, 1, -2, 9], [-1, 2, 5, -5]])")
print(gauss([[2, -1, 1, 2], [3, 1, -2, 9], [-1, 2, 5, -5]]))


# 5. Defina una funcion que pueda realizar una suma de Riemman para obtener el area bajo
# la curva dada una funcion f(x), dados los limites a y b. y la ∆x (no importa si se pasa al
# hacer los ciclos).
def riemman(func, a, b, n):
    dx = (b-a)/n
    k = 0
    total = 0
    while k <= n:
        xi = a + k*dx
        fx = func(xi)
        total += fx*dx
        k += 1
    return total
print("riemman(math.sin,0,3,20)")
print(riemman(math.sin,0,3,20))

# FUNCIONES BASICAS 1 
# He comentado todos los ejercicios para probar uno por uno de manera más sencilla e ir descomentandolos cuando sea necesario
#1
"""
def number_of_food_groups():
    return 5
print(number_of_food_groups())
"""
# Esta función imprimirá 5



#2
"""
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
"""
# Esta función imprimirá NameError, ya que la variable "number_of_days_in_a_week_silicon_or_triangle_sides" no está definida
# Entonces para solucionar, habría que definirla



#3
"""
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
"""
# Esta función imprimirá 5 y no 5 y 10, ya que la función termina en la primera declaración de retorno y la segunda no se ejecuta




#4
"""
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
"""
# Ocurre lo mismo que en la anterior, solo se imprime 5, porque la función acaba después del return.
# Si queremos que imprima 5 y luego 10, podríamos invertir el orden y poner print (5) y luego return 10




#5
"""
def number_of_great_lakes():
    return 5
x = number_of_great_lakes()
print(x)
"""
# Esta función imprime 5 y luego None, ya que la función no devuelve nada, por lo que x es None



#6
"""
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
"""
# Esta función imprime 3 luego 5 y luego un TypeError
# Si queremos solucionarlo tendríamos que poner return b+c así la función imprimiría 8, porque 1+2 son 3 y 2+3 son 5, en total 8




#7
"""
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
"""
# Esta función imprimirá 25




#8
"""
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
"""
# Esta función imprimirá 100 luego verificará si 100 es menor que 10 y como no lo es, retornará 10




#9
"""
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""
# Esta función imprime 7 porque 2 es menor que 3, luego avanza al siguiente print donde como 5 no es menor que 3, imprime 14
# Luego avanza al siguiente print en donde se suma el primer print con el segundo, lo que resulta en 14




#10
"""
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
"""
# Esta función solo imprime la suma de 3 + 5 que es 8. La función acaba en el primer return




#11
"""
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
"""
# Esta función va a imprimir 500, 500, 300 y 500 esto porque se define globalmente a b con valor de 500 y localmente con valor de 300
# En el primer print, b vale 500, en el segundo también, porque aun no pasamos por foobar, la tercera vez llamamos a foobar y dentro se imprime 300
# Por último, en el print final, b vuelve a tomar el valor de 500



#12
"""
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
"""
# En este caso ocurre lo mismo que en el ejemplo anterior. Aun cuando hay un return b dentro de foobar, esto no afecta el valor de b fuera de foobar
# Los valores impresos nuevamente serán 500, 500, 300 y 500


#13
"""
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
"""
# En este caso se imprime 500, 500, 300 y 300. Sigue la misma lógica que los ejemplos anteriores, solo que ahora fuera de foobar
# Se le otorga el valor de 300 a b, al igual como ocurre dentro de foobar. 


#14
"""
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
"""
# Esta función imprimirá 1, 3 y 2, ya que foo imprime 1, luego llama a bar que imprime 3 y luego foo imprime 2


#15
"""
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
"""
# Esta función imprimirá 1, 3, 5, 10. Foo imprime 1, luego llama a bar que imprime 3 y devuelve 5
# Luego foo asigna el valor de retorno a x y devuelve 10, el cual es asignado a y, imprimiendo y que ahora es 10
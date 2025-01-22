# Crear con list comprehension un lista con los 1000 primeros
# números naturales al cuadrado
# {1: 1.0, 2: 4, 3: 9, ...}
import math

def lists_comprehension():
    list = [i for i in range(1, 100001) if not i % math.lcm(4, 6, 9)]
    print(list,"\n")
    print(len(list))
    
    # Verfica que se cumpla la condición
    for i in list:
        if (i%4 + i%6 + i%9) != 0:
            print("No se cumple para", i)

# Crear con dictionary comprehension un diccionario
# cuyas llaves sean los 1000 primeros números naturales
# con sus raíces cuadradas como valores
# {1: 1.0, 2: 1.4142135623730951, 3: 1.7320508075688772, ...}

def dict_comprehension():
    dict = {i: i ** (1/2) for i in range(1, 1001)}

    print(dict,"\n")
    
if __name__ == '__main__':
    #lists_comprehension()
    dict_comprehension()
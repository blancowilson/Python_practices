
import math



if __name__ == '__main__':
    numbers_orden= list(range(29))
    print (numbers_orden[1::2])
    array_large = int(input("ingrese la cantidad de numeros a guardar: "))
    nubers_array = []
    for i in range(array_large):
        nubers_array.append(int(input(f'ingrese el valor {i+1}:' )))

    print(nubers_array)
    
"""Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de informes.
De cada línea se sabe numero, titular, tipo de plan (valor de 0 a 19), cantidad de minutos consumidos, provincia donde se
activo la línea (valor de 1 a 23)

Usted debe realizar dicho programa, controlado por un menú de opciones para que lleve a cabo los siguientes ítems:

1 - Cargar un vector de n Líneas, validando que el tamaño a cargar sea mayor a cero y que el tipo de producto y tipo de
plan sean válidos. El Arreglo debe generarse en forma ordenada por numero.

2 - Listar todas las líneas a razón de un registro por vez

3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos consumidos superen un valor X ingresado
por teclado. Muestre dicho archivo a razón de una registro a la vez y al final indique que porcentaje representan las
líneas del plan Y ingresado por parámetro sobre el total de líneas del archivo

4 - Determinar e informar la cantidad de minutos consumidos por cada tipo de plan y en cada provincia a la que pertenece
esa línea. Son 460 contadores

5 - Mostrar la línea con menor cantidad de minutos consumidos para las provincias x o y (donde ambos valores son ingresados
por parámetro), en caso que haya mas de una mostrarlas a todas

6 - Buscar una línea X ingresada por teclado. Si existe incrementar sus minutos consumidos en un 20% y mostrar los datos
de la línea. Caso contrario indicar con un mensaje que no existe"""

from funciones import *


def principal():
    v = []
    FD = "archivo.ds"
    opcion = None

    while opcion != 5:
        print("=" * 30)
        print("\tMenú de opciones")
        print("=" * 30)
        print()
        print("1-Cargar vector")
        print("2-Listar registros")
        print("3-Generar archivo")
        print("4-Consumo por provincia")
        print("5-Mostrar menor consumo")
        print("6-Buscar linea")
        print("7 Finalizar Programa-")
        print()

        opcion = int(input("Ingrese la opcion: "))

        if opcion == 1:
            n = validar_mayor(0)
            generar_arreglo(v, n)
        elif opcion == 2:
            if not v:
                print("No se encontraron datos cargados.")
            else:
                mostrar_string(v)
        elif opcion == 3:
            if not v:
                print("No se encontraron datos cargados. ")
            else:
                minutos = int(input("Ingrese la cantidad de minutos: "))
                crear_archivo(v, FD, minutos)
                plan = validar_intervalo(0 , 19)
                mostrar_archivo(FD, plan)
        elif opcion == 4:
            if not v:
                print("No se encontraron ")
            else:
                mat = generate_mat_cont(v)
                mostrar_matriz(mat)
        elif opcion == 5:
            print("Programa Finalizado.")
        else:
            print("Opión no valida")


if __name__ == "__main__":
    principal()

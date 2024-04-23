import sumar
import restar as r
import potencia
import divi
import raizc as z
from multi import multi
from input import tomar_datos
from tomar_u_n import tomar_u_n
import time
import os
import sys
# detecta el OS
clear = 'cls' if sys.platform == 'win32' else 'clear'
if __name__ == '__main__':
    while True:
        opcion = input("""Esto es una calculadora:
               1. Sumar
               2. Restar
               3. División
               4. Potencia
               5. Raíz cuadrada
               6. Multiplicación
               0. Salir
               >""")
        if opcion == '1':
            x, y = tomar_datos()
            sumar.sumar(x, y)
            time.sleep(3)
        elif opcion == '2':
            x, y = tomar_datos()
            r.restar(x, y)
            time.sleep(3)
        elif opcion == '3':
            x, y = tomar_datos()
            divi.divi(x, y)
            time.sleep(3)
        elif opcion == '4':
            x = tomar_u_n()
            potencia.potencia(x)
            time.sleep(3)
        elif opcion == '5':
            x = tomar_u_n()
            z.raizc(x)
            time.sleep(3)
        elif opcion == '6':
            x, y = tomar_datos()  # Corregir a tomar_datos para multiplicación
            multi(x, y)
            time.sleep(3)
        elif opcion == '0':
            print('Nos vemos a la próxima')
            time.sleep(1)
            os.system(clear)
            exit() 
        else:
            print('No existe esta Operación')
            time.sleep(1)
            os.system(clear)

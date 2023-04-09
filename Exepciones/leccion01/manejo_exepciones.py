from NumerosIgualesExeption import NumerosIgualesExecption

resultado = None

try:
    a = int (input("Digite el primer numero: "))
    b = int (input("Digite el segundo numero:  "))
    if a == b :
        raise NumerosIgualesExecption ("numeros son iguales")
    resultado = a/b # modificamos

except TypeError as e:
    print(f"TypeError - ocurrio un error: {type(e)}")
except ZeroDivisionError as e:
    print(f"Ocurrio un error: {type(e)}")
except Exception as e:
    print(f"Ocurrio un error: {type(e)}")
else:
    print("No se arrojo ninguna exepcion")
finally: #siempre se va a ejecutar
    print("Ejecucion de este bloque finally")
print(f"Elresultado es: {resultado}")
print("seguimos...")
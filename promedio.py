def leer_archivo_datos(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = [float(linea.strip()) for linea in archivo]
        return datos
    except FileNotFoundError:
        print(f"Archivo '{ruta_archivo}' no encontrado.")
        return None
    except ValueError:
        print(f"Datos inválidos en '{ruta_archivo}'. Asegúrate de que el archivo contenga valores numéricos.")
        return None

def calcular_promedio(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        # Si hay un número par de elementos, toma el promedio de los dos valores medios
        medio1 = datos_ordenados[n // 2 - 1]
        medio2 = datos_ordenados[n // 2]
        return (medio1 + medio2) / 2
    else:
        # Si hay un número impar de elementos, devuelve el valor medio
        return datos_ordenados[n // 2]

def calcular_moda(datos):
    frecuencia = {}
    for num in datos:
        frecuencia[num] = frecuencia.get(num, 0) + 1

    max_frecuencia = max(frecuencia.values())
    valores_moda = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    return valores_moda

def main():
    ruta_archivo = "datos.txt"
    datos = leer_archivo_datos(ruta_archivo)
    if datos:
        promedio = calcular_promedio(datos)
        mediana = calcular_mediana(datos)
        moda = calcular_moda(datos)

        print(f"Promedio: {promedio:.2f}")
        print(f"Mediana: {mediana:.2f}")
        print(f"Moda: {', '.join(map(str, moda))}")

if __name__ == "__main__":
    main()

# Matriz: [Título, Año de Lanzamiento, Calificación, Género]

videoteca = [
    ["Inception", 2010, 9, "Ciencia Ficción"],
    ["Avatar", 2009, 8, "Acción"],
    ["Dune", 2021, 9, "Ciencia Ficción"],
    ["Encanto", 2021, 8, "Animación"],
    ["The Batman", 2022, 8, "Acción"],
    ["Interstellar", 2014, 10, "Ciencia Ficción"],
    ["Joker", 2019, 9, "Drama"]
]

# Módulo (función) para contar títulos que cumplen criterios
def contar_titulos_populares(matriz, calificacion_minima, anio_limite):
    contador = 0
    
    for titulo in matriz:
        calificacion = titulo[2]
        anio = titulo[1]
        
        # Verificar ambos criterios
        if calificacion >= calificacion_minima and anio >= anio_limite:
            contador += 1
    
    return contador

# Parámetros de búsqueda
umbral_calificacion = 8
anio_limite = 2020

# Llamado de la función
resultado = contar_titulos_populares(
    videoteca,
    umbral_calificacion,
    anio_limite
)

# Salida
print("Cantidad de títulos que cumplen los criterios:", resultado)
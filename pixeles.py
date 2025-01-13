import os
import numpy as np
from PIL import Image

# Función para procesar una sola imagen
def process_image(image_path, output_path):
    """
    Cambia los píxeles del objeto (valor 1) a 255 en una imagen de segmentación semántica.
    
    :param image_path: Ruta de la imagen de entrada.
    :param output_path: Ruta para guardar la imagen procesada.
    """
    # Cargar la imagen como un arreglo de numpy
    image = Image.open(image_path).convert('L')  # Convertir a escala de grises si no lo está
    image_array = np.array(image)
    
    # Cambiar los valores 1 a 255
    image_array[image_array == 1] = 255
    
    # Crear una nueva imagen con los valores modificados
    result_image = Image.fromarray(image_array.astype(np.uint8))
    
    # Guardar la imagen procesada
    result_image.save(output_path)

# Función para procesar todas las imágenes PNG en un directorio
def process_directory(input_dir, output_dir):
    """
    Procesa todas las imágenes PNG en un directorio, aplicando el cambio deseado.
    
    :param input_dir: Directorio con las imágenes de entrada.
    :param output_dir: Directorio para guardar las imágenes procesadas.
    """
    # Crear el directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterar sobre todos los archivos en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):  # Filtrar solo archivos PNG
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            process_image(input_path, output_path)
            print(f"Procesada: {filename}")
    
    print("Todas las imágenes han sido procesadas.")

# Directorios de entrada y salida
input_directory = "C:/Users/MARIOALBERTOROMANGAR/Desktop/Pruebas/im"
output_directory = "C:/Users/MARIOALBERTOROMANGAR/Desktop/Pruebas/gt"

# Procesar las imágenes
process_directory(input_directory, output_directory)

import os
import subprocess
from PIL import Image

# Directorios de entrada y salida
# Input and output directories
input_dir = "Input"
output_dir = "Output"

# Crear el directorio de salida si no existe
# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Obtener la lista de archivos en el directorio de entrada
# Get the list of files in the input directory
files = os.listdir(input_dir)

# Iterar por cada archivo en el directorio de entrada
# Iterate through each file in the input directory
for file in files:
    # Comprobar si el archivo es un archivo VTF
    # Check if the file is a VTF file
    if file.endswith(".vtf"):
        # Construir la ruta completa de entrada y salida
        # Build the full input and output path
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".png")
        
        # Ejecutar el comando vtf2img para convertir el archivo
        # Execute the vtf2img command to convert the file
        subprocess.run(["vtf2img", input_path, output_path])
        
        # Dividir el tamaño del archivo PNG por la mitad
        # Split PNG image size in half
        with Image.open(output_path) as img:
            width, height = img.size
            new_width = width // 2 # Coge el ancho y lo divide entre 2 / Take the width and divide it by 2
            new_height = height // 2 # Coge la altura y la divide entre 2 / Take the height and divide it by 2
            img = img.resize((new_width, new_height))
            img.save(output_path)
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
import time
import argparse
import re

# Lista de palabras reservadas
reserved_words = ["for", "print", "if", "while", "main", "import", "from", "in", "with", "open", "def", "as", "else", "elif"]

def add_text_to_image(draw, text, position, font, color=(255, 255, 255)):
    x, y = position
    words = re.split(r'(\W+)', text)  # Dividir el texto en palabras y separadores no alfanuméricos
    for word in words:
        if word in reserved_words:
            draw.text((x, y), word, font=font, fill=(0, 255, 0))  # Palabras reservadas en verde
        else:
            draw.text((x, y), word, font=font, fill=color)
        x += draw.textbbox((0, 0), word, font=font)[2]
    return x, y

def generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path):
    # Leer la imagen de fondo
    bg_image = Image.open(bg_image_path).convert("RGBA")
    bg_image = bg_image.resize(output_resolution, Image.LANCZOS)
    
    # Configuración de la fuente
    font = ImageFont.truetype(font_path, 16)
    
    # Parámetros para la animación
    frames = []
    x, y = margins, margins
    max_width, max_height = output_resolution[0] - 2 * margins, output_resolution[1] - 2 * margins
    text_speed = 1.0 / char_per_sec
    line_height = font.getbbox("A")[3] - font.getbbox("A")[1] + 15
    
    # Convertir texto en una lista de caracteres
    chars = list(text)
    current_text = ""
    all_lines = []

    for char in chars:
        current_text += char
        text_bbox = ImageDraw.Draw(bg_image).textbbox((0, 0), current_text, font=font)
        if char == "\n" or text_bbox[2] > max_width:
            all_lines.append(current_text)
            current_text = ""
            y += line_height

        # Crear una nueva imagen con las líneas actuales
        frame = bg_image.copy()
        draw = ImageDraw.Draw(frame)
        y_temp = margins

        for line in all_lines[-(max_height // line_height):]:  # Mostrar solo las últimas líneas que caben en la pantalla
            x_temp, y_temp = margins, y_temp
            x_temp, y_temp = add_text_to_image(draw, line, (x_temp, y_temp), font)
            y_temp += line_height
        
        if current_text:
            x_temp, y_temp = add_text_to_image(draw, current_text, (margins, y_temp), font)

        frames.append(frame)
        time.sleep(text_speed)
    
    # Convertir frames a imágenes opencv
    video_frames = [cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR) for frame in frames]
    
    # Crear el video
    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, output_resolution)
    for frame in video_frames:
        video.write(frame)
    video.release()

def main():
    parser = argparse.ArgumentParser(description="Generar un video de un texto escribiéndose automáticamente.")
    parser.add_argument("text_file", type=str, help="Ruta del archivo de texto.")
    
    args = parser.parse_args()

    # Parámetros fijos del script
    bg_image_path = "image.png"
    font_path = "console.ttf"
    output_resolution = (640, 480)
    fps = 25
    char_per_sec = 10
    margins = 40
    output_path = "output_video.avi"

    # Leer el archivo de texto
    with open(args.text_file, 'r') as file:
        text = file.read()

    generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path)

if __name__ == "__main__":
    main()

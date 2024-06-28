import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import argparse
import re
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips

# Lista de palabras reservadas
reserved_words = ["for", "print", "if", "while", "import", "from", "in", "with", "open", "type", ")", ":", "def", "False", "class", "is", "return", "None", "continue", "lambda", "try", "True", "def", "nonlocal", "while", "and", "del", "not", "with", "as", "elif", "or", "yield", "assert", "else", "pass", "break", "except", "raise"]

# Crear una expresión regular para detectar palabras reservadas
reserved_pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in reserved_words) + r')\b')

def add_text_to_image(draw, text, position, font, color=(230, 255, 249)):
    x, y = position
    # Dividir el texto en palabras y separadores no alfanuméricos
    words = re.findall(r'\w+|\W+', text)
    for word in words:
        if reserved_pattern.fullmatch(word):
            draw.text((x, y), word, font=font, fill=(255, 87, 51))  # Palabras reservadas en verde
        else:
            draw.text((x, y), word, font=font, fill=color)
        x += draw.textbbox((0, 0), word, font=font)[2]
    return x, y

def generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path, audio_path):
    # Leer la imagen de fondo
    bg_image = Image.open(bg_image_path).convert("RGBA")
    bg_image = bg_image.resize(output_resolution, Image.LANCZOS)
    
    # Configuración de la fuente
    font = ImageFont.truetype(font_path, 16)
    
    # Parámetros para la animación
    x, y = margins, margins
    max_width, max_height = output_resolution[0] - 2 * margins, output_resolution[1] - 2 * margins
    text_speed = 1.0 / char_per_sec
    line_height = font.getbbox("A")[3] - font.getbbox("A")[1] + 15
    
    # Convertir texto en una lista de caracteres
    chars = list(text)
    current_text = ""
    all_lines = []

    # Crear el video
    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, output_resolution)
    
    total_frames = 0
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

        # Convertir el frame a imagen opencv y escribirlo en el video
        video_frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        video.write(video_frame)
        
        total_frames += 1
        time.sleep(text_speed)
    
    video.release()

    video_duration = total_frames / fps
    
    # Añadir el audio de fondo
    video_clip = VideoFileClip(output_path)
    audio_clip = AudioFileClip(audio_path)

    if audio_clip.duration < video_duration:
        # Repetir el audio si es más corto que el video
        num_repeats = int(np.ceil(video_duration / audio_clip.duration))
        audio_clip = concatenate_audioclips([audio_clip] * num_repeats).subclip(0, video_duration)
    else:
        # Recortar el audio si es más largo que el video
        audio_clip = audio_clip.subclip(0, video_duration)
    
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path.replace(".avi", "_with_audio.avi"), codec='libx264')

def main():
    parser = argparse.ArgumentParser(description="Generar un video de un texto escribiéndose automáticamente.")
    parser.add_argument("text_file", type=str, help="Ruta del archivo de texto.")
    
    args = parser.parse_args()

    # Parámetros fijos del script
    bg_image_path = "image1.png"
    font_path = "typewriter.ttf"
    output_resolution = (640, 480)
    fps = 25
    char_per_sec = 10
    margins = 40
    output_path = "output_video.avi"
    audio_path = "background1.mp3"

    # Leer el archivo de texto
    with open(args.text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path, audio_path)

if __name__ == "__main__":
    main()

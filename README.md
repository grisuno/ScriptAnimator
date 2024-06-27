# ScriptAnimator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

```sh
                                                                             
 @@@@@@    @@@@@@@  @@@@@@@   @@@  @@@@@@@   @@@@@@@                         
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@@@@                         
!@@       !@@       @@!  @@@  @@!  @@!  @@@    @@!                           
!@!       !@!       !@!  @!@  !@!  !@!  @!@    !@!                           
!!@@!!    !@!       @!@!!@!   !!@  @!@@!@!     @!!                           
 !!@!!!   !!!       !!@!@!    !!!  !!@!!!      !!!                           
     !:!  :!!       !!: :!!   !!:  !!:         !!:                           
    !:!   :!:       :!:  !:!  :!:  :!:         :!:                           
:::: ::    ::: :::  ::   :::   ::   ::          ::                           
:: : :     :: :: :   :   : :  :     :           :                            
                                                                             
                                                                             
 @@@@@@   @@@  @@@  @@@  @@@@@@@@@@    @@@@@@   @@@@@@@   @@@@@@   @@@@@@@   
@@@@@@@@  @@@@ @@@  @@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!@!@@@  @@!  @@! @@! @@!  @@!  @@@    @@!    @@!  @@@  @@!  @@@  
!@!  @!@  !@!!@!@!  !@!  !@! !@! !@!  !@!  @!@    !@!    !@!  @!@  !@!  @!@  
@!@!@!@!  @!@ !!@!  !!@  @!! !!@ @!@  @!@!@!@!    @!!    @!@  !@!  @!@!!@!   
!!!@!!!!  !@!  !!!  !!!  !@!   ! !@!  !!!@!!!!    !!!    !@!  !!!  !!@!@!    
!!:  !!!  !!:  !!!  !!:  !!:     !!:  !!:  !!!    !!:    !!:  !!!  !!: :!!   
:!:  !:!  :!:  !:!  :!:  :!:     :!:  :!:  !:!    :!:    :!:  !:!  :!:  !:!  
::   :::   ::   ::   ::  :::     ::   ::   :::     ::    ::::: ::  ::   :::  
 :   : :  ::    :   :     :      :     :   : :     :      : :  :    :   : :  
                                                                             
```

ScriptAnimator es una herramienta que genera un video de un texto que se escribe automáticamente sobre una imagen de fondo, con resaltado de sintaxis básico para palabras reservadas.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)

## Características

- Genera videos con texto que se escribe automáticamente.
- Resaltado de sintaxis para palabras reservadas.
- Personalización de imagen de fondo, fuente, resolución de salida, velocidad de escritura y más.

## Requisitos

- Python 3.x
- OpenCV
- NumPy
- Pillow
- MoviePy

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/grisuno/ScriptAnimator.git
cd ScriptAnimator
pip install -r requirements.txt
python script_animator.py path_to_text_file.py
```

## Personalización
Puedes personalizar varios aspectos del video generado:

- bg_image_path: Ruta de la imagen de fondo.
- font_path: Ruta de la fuente TrueType (.ttf).
- output_resolution: Resolución del video de salida (ancho, alto).
- fps: Cuadros por segundo del video.
- char_per_sec: Caracteres por segundo (velocidad de escritura).
- margins: Margen del texto en píxeles.
- output_path: Ruta del archivo de video de salida.

Estos parámetros pueden ser modificados directamente en el script

## Contribución
¡Las contribuciones son bienvenidas! Si tienes alguna mejora, abre un issue o un pull request.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

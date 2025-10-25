import os
from PIL import Image, ImageDraw, ImageFont

# === CONFIGURACIÓN ===
plantilla = "formato.png"
archivo_vocabulario = "vocabulario.txt"
carpeta_salida = "salida"

# Crear carpeta de salida si no existe
os.makedirs(carpeta_salida, exist_ok=True)

# Cargar las palabras
with open(archivo_vocabulario, "r", encoding="utf-8") as f:
    palabras = [line.strip() for line in f if line.strip()]

# Fuente para el texto
try:
    fuente = ImageFont.truetype("arial.ttf", 60)
except:
    fuente = ImageFont.load_default()

# Cargar imagen base
base = Image.open(plantilla).convert("RGB")
ancho, alto = base.size

# Coordenadas aproximadas del centro del "boom"
centro_x, centro_y = ancho // 2, alto // 2

# === GENERAR UNA IMAGEN POR PALABRA ===
for palabra in palabras:
    imagen = base.copy()
    dibujo = ImageDraw.Draw(imagen)

    # Calcular tamaño del texto
    bbox = dibujo.textbbox((0, 0), palabra, font=fuente)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Centrar texto
    x = centro_x - text_width // 2
    y = centro_y - text_height // 2

    # Dibujar el texto con sombra ligera
    sombra = (x + 3, y + 3)
    dibujo.text(sombra, palabra, font=fuente, fill=(120, 120, 120))
    dibujo.text((x, y), palabra, font=fuente, fill=(0, 0, 0))

    # Guardar imagen
    salida = os.path.join(carpeta_salida, f"{palabra.replace(' ', '_')}.png")
    imagen.save(salida)
    print(f"✅ Imagen creada: {salida}")

print("🎉 ¡Todas las imágenes fueron generadas exitosamente!")

import re

# Nombre del archivo HTML de entrada
entrada_html = "entrada.html"

# Nombre del archivo TXT de salida
salida_txt = "urls.txt"

# Leer el HTML
with open(entrada_html, "r", encoding="utf-8") as f:
    contenido = f.read()

# Buscar todas las URLs que empiecen por https://www.amazon.es/dp/ y tengan letras/números en el ASIN
urls = re.findall(r"https:\/\/www\.amazon\.es\/dp\/[A-Za-z0-9]+", contenido)

# Eliminar duplicados manteniendo el orden
urls_unicas = list(dict.fromkeys(urls))

# Guardar en un TXT
with open(salida_txt, "w", encoding="utf-8") as f:
    for url in urls_unicas:
        f.write(url + "\n")

print(f"✅ {len(urls_unicas)} URLs únicas guardadas en {salida_txt}")

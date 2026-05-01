from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 1. Configura Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # No abre ventana
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Abre navegador
driver = webdriver.Chrome(options=chrome_options)

# 3. URL de tu lista de deseos
wishlist_url = "https://www.amazon.es/hz/wishlist/ls/CPRFS7LXKV7S?ref_=abls_nvfly_yl&viewType=list"

# 4. Ir a la página
driver.get(wishlist_url)

# 5. Simula scroll para cargar todos los productos
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Baja al fondo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    # Comprueba nuevo tamaño
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # Ya no hay más contenido
    last_height = new_height

# 6. Guarda el HTML completo
html_content = driver.page_source

# 7. Guarda en un archivo
with open("wishlist_completa.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ HTML guardado como 'wishlist_completa.html'.")

# 8. Cierra navegador
driver.quit()

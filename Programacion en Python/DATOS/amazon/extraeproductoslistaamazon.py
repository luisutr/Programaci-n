import re
import time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extraer_urls_lista_deseos(wishlist_url: str, salida_txt: str = "productos_lista.txt"):
    """
    Descarga la wishlist de Amazon, extrae URLs canónicas de productos y las guarda sin duplicados.
    - wishlist_url: URL completa de la lista de deseos (ej: https://www.amazon.es/hz/wishlist/ls/XXXX...)
    - salida_txt: nombre del archivo de salida .txt
    """
    # Derivar base del dominio (https://www.amazon.es)
    parsed = urlparse(wishlist_url)
    base = f"{parsed.scheme}://{parsed.netloc}"

    # Configurar Selenium (headless + user-agent para mejorar compatibilidad)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(wishlist_url)
        time.sleep(2)  # pequeño margen para que empiece a renderizar

        # Scroll progresivo hasta que no haya más contenido
        SCROLL_PAUSE_TIME = 1.5
        max_loops = 30  # evita bucle infinito en páginas cortas
        loop = 0
        last_height = driver.execute_script("return document.body.scrollHeight")

        while loop < max_loops:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            loop += 1

        html = driver.page_source

        # Capturar ASINs tanto en /dp/ASIN como en /gp/product/ASIN (relativo o absoluto indistinto)
        # ASIN son 10 chars alfanuméricos
        asin_pat = r'(?:/dp/|/gp/product/)([A-Za-z0-9]{10})'
        asins = re.findall(asin_pat, html)

        # Deduplicar manteniendo orden y normalizando a mayúsculas
        vistos = set()
        urls_unicas = []
        for asin in asins:
            a = asin.upper()
            if a not in vistos:
                vistos.add(a)
                urls_unicas.append(f"{base}/dp/{a}")

        # Guardar a TXT
        with open(salida_txt, "w", encoding="utf-8") as f:
            for url in urls_unicas:
                f.write(url + "\n")

        print(f"✅ {len(urls_unicas)} URLs únicas guardadas en '{salida_txt}'")

    finally:
        driver.quit()



# Ejemplo de uso:
extraer_urls_lista_deseos(
    "https://www.amazon.es/hz/wishlist/ls/8Y76I3PT7NYP?ref_=abls_nvfly_yl&viewType=list",
    "ps5.txt"
)

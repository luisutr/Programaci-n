from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de Selenium con Chrome en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # No abrir ventana
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializar el driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL de prueba (sustituye con la real)
url = "https://empresite.eleconomista.es/ANFIX-SOFTWARE.html"

# Abrimos la página con Selenium
driver.get(url)

try:
    # Esperar hasta que el div con el email esté presente (máximo 10 segundos)
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.seeMoreDir a.email"))
    )

    # Extraer el email
    email = email_element.get_attribute("href").replace("mailto:", "").split("?")[0]
    print("Email encontrado:", email)

except Exception as e:
    print("No se encontró ningún email:", e)

# Cerrar el navegador
driver.quit()

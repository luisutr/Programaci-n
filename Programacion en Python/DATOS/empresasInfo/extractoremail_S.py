from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import random

# Configuración de Selenium
options = Options()
options.add_argument("--headless")  # Ejecutar sin abrir el navegador
options.add_argument("--disable-blink-features=AutomationControlled")  # Evitar detección de bot
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inicializar Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

emails = []
base_url = "https://empresite.eleconomista.es/Actividad/SOFTWARE/provincia/MADRID/PgNum-{}/?testfiltros=1&emp_email=true"

for page in range(1, 37):
    url = base_url.format(page)
    print(f"Scrapeando: {url}")

    try:
        driver.get(url)
        time.sleep(random.uniform(3, 6))  # Simular navegación humana

        # Extraer enlaces a empresas
        company_links = driver.find_elements(By.CSS_SELECTOR, "h3 a")
        company_urls = [link.get_attribute("href") for link in company_links]

        for company_url in company_urls:
            driver.get(company_url)
            time.sleep(random.uniform(3, 6))

            try:
                email_element = driver.find_element(By.CLASS_NAME, "email")
                email = email_element.text.strip()
                emails.append(email)
                print(f"Email encontrado: {email}")
            except:
                print(f"No se encontró email en {company_url}")

    except Exception as e:
        print(f"Error en {url}: {e}")

    time.sleep(random.uniform(10, 20))  # Evitar detección por demasiadas solicitudes

# Guardar emails en un CSV
with open('emails.csv', 'w', newline='') as csvfile:
    email_writer = csv.writer(csvfile, delimiter=';')
    for email in emails:
        email_writer.writerow([email])

print("Emails extraídos y guardados en 'emails.csv'.")
driver.quit()

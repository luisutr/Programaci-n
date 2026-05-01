import requests
from bs4 import BeautifulSoup
import csv
import time
import random
from fake_user_agent import user_agent  # Corrección de importación

# Inicializa la lista de correos
emails = []

# Bucle para recorrer las páginas del listado
for page in range(1, 41):
    url = "https://empresite.eleconomista.es/Actividad/SOFTWARE/provincia/MADRID/PgNum-{page}/?testfiltros=1&emp_email=true"

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    ]

    # Elegir un User-Agent aleatorio en cada solicitud
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            company_links = soup.find_all('h3')

            for link in company_links:
                try:
                    company_url = link.a['href']

                    headers = {"User-Agent": user_agent()}  # Nuevo User-Agent

                    company_response = requests.get(company_url, headers=headers)

                    if company_response.status_code == 200:
                        company_soup = BeautifulSoup(company_response.text, 'html.parser')
                        email_tag = company_soup.find('a', class_='email')

                        if email_tag:
                            email = email_tag.text.strip()
                            if email not in emails:  # Evita duplicados
                                emails.append(email)
                                print(f"Email encontrado: {email}")
                        else:
                            print(f"No se encontró email en {company_url}")

                    else:
                        print(f"Error {company_response.status_code} en {company_url}")

                except Exception as e:
                    print(f"Error al procesar {link}: {e}")

                # Retraso aleatorio entre 3 y 7 segundos
                time.sleep(random.uniform(3, 7))

        else:
            print(f"Error {response.status_code} en {url}")

    except Exception as e:
        print(f"Error en {url}: {e}")

    # Retraso aleatorio entre páginas (6 a 12 segundos)
    time.sleep(random.uniform(6, 12))

# Guarda los correos en un archivo CSV
with open('emails.csv', 'w', newline='') as csvfile:
    email_writer = csv.writer(csvfile, delimiter=';')
    for email in emails:
        email_writer.writerow([email])

print("Emails extraídos y guardados en 'emails.csv'.")

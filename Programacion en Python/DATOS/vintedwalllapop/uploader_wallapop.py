from playwright.sync_api import sync_playwright
import time

def subir_wallapop(producto):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=400)  # slow_mo = pausas humanas
        context = browser.new_context()

        # 👉 IMPORTANTE: inicia sesión manualmente la primera vez
        page = context.new_page()
        page.goto("https://es.wallapop.com/app/upload")

        # Paso 1: Resumen
        page.fill("#summary", producto["titulo"])
        page.get_by_text("Continuar").click()

        # Paso 2: Fotos
        fotos = producto["fotos"].split(";")
        for foto in fotos:
            page.set_input_files("#dropAreaPreviewInput", foto)
            time.sleep(1)
        page.get_by_text("Continuar").click()

        # Paso 3: Categoría
        page.locator('input[aria-label="Categoría y subcategoría"]').click()
        page.keyboard.type(producto["categoria"])
        page.keyboard.press("Enter")
        page.get_by_text("Continuar").click()

        # Paso 4: Detalles producto
        page.fill("#title", producto["titulo"])
        page.fill("#description", producto["descripcion"])
        page.fill("#sale_price", str(producto["precio"]))

        # Estado (ejemplo: "Nuevo")
        page.locator('input[aria-label="Estado*"]').click()
        page.keyboard.type(producto["estado"])
        page.keyboard.press("Enter")

        # Localización
        page.fill("#location", producto["localizacion"])
        time.sleep(2)  # esperar autocompletado
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")

        # Paso final: publicar
        page.get_by_text("Subir producto").click()

        time.sleep(5)
        browser.close()

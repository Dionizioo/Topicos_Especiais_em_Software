from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Inicializar o WebDriver diretamente
driver = webdriver.Chrome()

# Abrir o site do Zoom
driver.get("https://www.zoom.com.br/")

# Esperar até que o elemento dropdown esteja disponível e clicar nele
wait = WebDriverWait(driver, 10)
dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Dropdown_DropdownHeader__OwfE_")))
dropdown.click()

# Verificar se o texto "Notebook" está presente no p dentro do div do dropdown
notebook_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Notebook')]")))

# Clicar na opção "Notebook"
notebook_option.click()

# Agora, localizar o campo de busca pelo atributo data-test e digitar "acer"
search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test='input-search']")))
search_input.send_keys("Dell")
#esperar um pouco
import time
time.sleep(2)


# Localizar e clicar no botão de pesquisa
search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "AutoCompleteStyle_submitButton__VwVxN")))
search_button.click()

element = wait.until(EC.presence_of_element_located((By.ID, "orderBy")))

#criando um objeto select
select = Select(element)

#Agora vamos selecionar a opção
select.select_by_visible_text("Menor preço")


# Fechar o navegador após alguns segundos (opcional)
import time
time.sleep(30)

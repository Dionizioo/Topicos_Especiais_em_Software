from time import sleep
import By
from time import sleep
from selenium import webdriver


drive = webdriver.Chrome()

drive.get('https://www.sinepar.com.br/progno')


form = drive.find_element(By.TAG_NAME,'form')
input1 = form.find_element(By.TAG_NAME,'input')
input.send_keys('São Paulo')

print(input1)


#fazer um sleep
drive.implicitly_wait(10)
drive.close()


t = driver.find_element(By.TAG_NAME, 'h1')
print(t.get_attribute('value'))
#lista_horarios.append(t)

sleep(5)


# importam librarii
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://www.fortech.ro/')
sleep(3)
# acceptam cookies
chrome.find_element(By.XPATH, '//*[@id="accept"]').click()
sleep(3)
# apasam butonul contact
chrome.find_element(By.XPATH, '//*[@id="menu-item-9950"]/a/label').click()
sleep(3)
# completam spatiile din formular
chrome.find_element(By.XPATH, '//*[@id="wpcf7-f4234-p300-o1"]/form/div[2]/div[1]/span/input').send_keys('HurjuiDenisa')
chrome.find_element(By.XPATH, '//*[@id="wpcf7-f4234-p300-o1"]/form/div[3]/div[1]/span/input').send_keys('denisa.hurjui@yahoo.com')
chrome.find_element(By.XPATH, '//*[@id="wpcf7-f4234-p300-o1"]/form/div[3]/div[2]/span/input').send_keys('0758474001')
chrome.find_element(By.XPATH, '//*[@id="wpcf7-f4234-p300-o1"]/form/div[4]/div/span/textarea').send_keys('Hello everyone! This is my automatic test for the first stage in the selection of candidates for training.')
sleep(6)
# inchidem chrome
chrome.quit()
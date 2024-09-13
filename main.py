from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.rvinfo.com.br/wp-admin")
driver.maximize_window()

def login():
    email = driver.find_element(by=By.CSS_SELECTOR, value="#user_login")
    password = driver.find_element(by=By.CSS_SELECTOR, value="#user_pass")
    button = driver.find_element(by=By.CSS_SELECTOR, value="#wp-submit")
    
    email.send_keys("leonardo.santana@rvinfo.com.br")
    password.send_keys("10102030")
    button.click()
    
    time.sleep(3)
    
login()

def access_products(type: str):
    products_button = driver.find_element(by=By.CSS_SELECTOR, value="#menu-posts-product > a > div.wp-menu-name")
    products_button.click()

    trash_button = driver.find_element(by=By.CSS_SELECTOR, value="#wpbody-content > div.wrap > ul > li." + type + " > a")
    trash_button.click()
    
access_products("trash") #publish or trash

def delete_products():
    select_all = driver.find_element(by=By.CSS_SELECTOR, value="#cb-select-all-1")
    select_all.click()
    
    select_method = driver.find_element(by=By.CSS_SELECTOR, value="#bulk-action-selector-top > option:nth-child(3)")
    select_method.click()
    
    run_button = driver.find_element(by=By.CSS_SELECTOR, value="#doaction")
    run_button.click()
    
    driver.implicitly_wait(1)

for x in range(100):
    delete_products()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
val = input("Enter a url:")
driver.get(val)
data = {}
data['biography']= driver.find_element(By.XPATH ,"//div[@data-testid='UserDescription']//span").text
data['followers_count']= driver.find_element(By.XPATH ,"//body/div[@id='react-root']/div/div/div[@aria-hidden='false']/main[@role='main']/div/div/div/div[@data-testid='primaryColumn']/div[@aria-label='Home timeline']/div/div/div/div/div/div/div[2]/a[1]/span[1]/span[1]").text
data['following_count'] = driver.find_element(By.XPATH ,"//body/div[@id='react-root']/div/div/div[@aria-hidden='false']/main[@role='main']/div/div/div/div[@data-testid='primaryColumn']/div[@aria-label='Home timeline']/div/div/div/div/div/div/div[1]/a[1]/span[1]/span[1]").text
data['user_id']= driver.find_element(By.XPATH ,"//div[@data-testid='UserName']//div//div//div//div//div//div[@dir='ltr']//span").text
print(data)
driver.quit()


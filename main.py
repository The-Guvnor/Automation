from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Creating instance for webdriver
browser = webdriver.Chrome()
browser.get('https://digitalnetwork.rigohr.com/')
#Load Elements
time.sleep(5)
#Find Username Element and Send Username
username = browser.find_element(By.XPATH,'//*[@id="rigoId"]/div[2]/input')
username.send_keys('user.name')
#Find Password Element and Send Password
password = browser.find_element(By.XPATH,'//*[@id="password"]/div[2]/input')
password.send_keys('password')
#Load Elements
time.sleep(5)
#Using Click function to login
login = browser.find_element(By.TAG_NAME,'button')
login.click()
#Load Elements
time.sleep(5)
#Find Clock In/Out
clock = browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/header/div[1]/div/div/div[1]/div[1]/div/div[2]/div/button')
clock.click()
#Load Elements
time.sleep(5)
#Find and Check Check In/Out
check = browser.find_element(By.XPATH,'//*[@id="chakra-modal--body-:r1:"]/div/div[1]/div/div/label[1]')
check.click()
#Load Elements
time.sleep(5)
# Adding Note to Check IN/OUT
# note = browser.find_element(By.XPATH,'//*[@id="note"]')
# note.send_keys('Missed Check-Out')
#Load Elements
time.sleep(5)
#Checkin Submit
submit = browser.find_element(By.XPATH,'//*[@id="chakra-modal-:r1:"]/footer/div/button[2]')
# submit.click()
#Print Task completed
print('Task Completed')
#Close Browser
browser.close()
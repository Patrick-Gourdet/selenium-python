#Patrick GOurdet 10/13/2017
#Webdriver Selenium Script to find email and write to file 
#Contracted by ANDVARIS
#1st:Download Python34 
#2nd:Download Selenium and place it in the Python34 folder
#dowload Chrome Driver point to driver in Program 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
customerNR = 1000020
nextID = True
browser=webdriver.Chrome('C:/Users/pgourdet/Documents/chromedriver_win32/chromedriver.exe')
action = ActionChains(browser)
browser.get('https://arise.service-now.com/navpage.do')
file = open("emails.txt","a")
#print(browser.page_source)
# 
frame = browser.find_element_by_xpath('//*[@id="gsft_main"]')
browser.switch_to.frame(frame)
username = browser.find_element_by_id("user_name")
password = browser.find_element_by_id("user_password")

try:
	username.send_keys("random52")
	password.send_keys("1231kwyI*")
except: 
	print("Error while entering password")
	browser.quit()	

browser.find_element_by_name("not_important").click()
time.sleep(3)
browser.find_element_by_id("f3be2c2d139022004c26d9722244b0a5").click()


frame = browser.find_element_by_xpath('//*[@id="gsft_main"]')
browser.switch_to.frame(frame)
while (nextID ):
	search = browser.find_element_by_xpath('//*[@id="sys_display.IO:93f0734a130232008c94b0322244b0a5"]')
	parent_h = browser.current_window_handle

	search.send_keys(str(customerNR))
	browser.find_element_by_xpath('//*[@id="sys_display.IO:93f0734a130232008c94b0322244b0a5"]').send_keys(Keys.ENTER)


	time.sleep(3)
	action.move_to_element(browser.find_element_by_id('IO:93f0734a130232008c94b0322244b0a5LINK.info')).click().perform()
	time.sleep(3)
	action.key_down(Keys.SHIFT)
	try:
		browser.switch_to_alert()
		value = browser.find_element_by_xpath('//*[@id="sys_readonly.sys_user.email"]')
		customerNR += 1
		file.write(value.get_attribute("value") + ", ")
		print(str(customerNR) + " " + value.get_attribute("value") + ", ")
		action.key_up(Keys.SHIFT)
		browser.switch_to_window(parent_h)

		frame = browser.find_element_by_xpath('//*[@id="gsft_main"]')
		browser.switch_to.frame(frame)
		browser.find_element_by_xpath('//*[@id="sys_display.IO:93f0734a130232008c94b0322244b0a5"]').clear()
	except:
		print("No Email for " + str(customerNR))
		customerNR += 1
		action.key_up(Keys.SHIFT)

		browser.find_element_by_xpath('//*[@id="sys_display.IO:93f0734a130232008c94b0322244b0a5"]').clear()
		continue
	if(customerNR == 1705868):
		customerNR = 170585
	elif (customerNR == 999993):
		print("FINALLY DONE")
		browser.quit()	
		break


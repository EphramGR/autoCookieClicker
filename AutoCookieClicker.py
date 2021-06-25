import selenium

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) 
driver.get("https://orteil.dashnet.org/cookieclicker/")

#waits to load so var actualy exist
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

#creats list of all the upgrades, and at the end it has weird stuff to make it cound in reverse, so it checks higher prices first
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

#makes list of actians that you can preform in sequence. Kinda like function
actions = ActionChains(driver)
actions.double_click(cookie)

for i in range(5000):
	actions.perform()
	#this takes the cookie number along with the work cookie, and cookies per second, then splits it up, takes off the first space, then grabs the second character(s) which are the numbers
	count = int(cookie_count.text.split(" ")[0])
	print(count)

	for item in items:
		value = int(item.text)
		if value <= count: 
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform()

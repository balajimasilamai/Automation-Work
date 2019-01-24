"""
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()

driver.get('https://datatables.net/')
time.sleep(5)

precedes = driver.find_elements_by_xpath("//td[text()='Airi Satou']/../td")
for i in precedes:
    print (i.text)
precedes[0].click()
#webdriver.ActionChains(driver).move_to_element(precedes[0]).click(precedes[0]).perform() 
#precedes[1].click()

"""
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()

driver.get('https://itsm.windstream.com')
time.sleep(30)
x=driver.switch_to.active_element
x['value'].send_keys('username')
print ('done')

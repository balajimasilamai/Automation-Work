#Help disk --> Ticket Creation

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()#chrome_options=options
driver.maximize_window()
driver.get('http://oneplive.prodapt.com/oneprodapt-new/login.htm#/helpdesk')

try:
    create_button=wait(driver,15).until(EC.element_to_be_clickable((By.XPATH ,"//a[@class='primary-add-icon ng-scope']")))
    create_button.click()
except:
    try:
        create_button=wait(driver,15).until(EC.element_to_be_clickable((By.XPATH ,"//button[@title='Create Ticket']")))
        create_button.click()
        # To handle the Ratings Alert
        rating_met="//span[@class='helpdesk-rating meh-o']"
        check_all=wait(driver,2).until(EC.element_to_be_clickable((By.XPATH ,"//input[@id='checkall']")))
        check_all.click()
        rating_met=wait(driver,2).until(EC.element_to_be_clickable((By.XPATH ,"//span[@class='helpdesk-rating meh-o']")))
        rating_met.click()
    except Exception as error:
        print (erorr)
    print ('All done')

Admin=wait(driver,15).until(EC.element_to_be_clickable((By.XPATH ,"//div[@class='top-accord clearfix']//ul//li[1]//input[1]")))
Admin.click()

#location_drop_down=wait(driver,15).until(EC.element_to_be_clickable((By.XPATH ,"//select[contains(@class,'ng-pristine ng-invalid ng-invalid-required ng-touched')]")))
#location_drop_down.click()
#wait(driver,15)
location=Select(wait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/label[1]/div[1]/select[1]"))))
wait(driver,2)
try:
    location.select_by_visible_text("OMR-IT")
except:
    wait(driver,10)
    location.select_by_visible_text("OMR-IT")

wait(driver,2)
Type=Select(driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[7]/div[1]/select[1]"))
Type.select_by_visible_text("Service Request")


wait(driver,2)
category=Select(driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[8]/div[1]/select[1]"))
category.select_by_visible_text("Cab Request")

wait(driver,2)
sub_category=Select(driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[9]/div[1]/select[1]"))
sub_category.select_by_visible_text("Pick Up and Drop")

#wait(driver,15)
#//*[@id="employee"]
#Employee=Select(driver.find_element_by_xpath('//*[@id="employee"]'))
Employee=Select(wait(driver,20).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="employee"]'))))
Employee.select_by_visible_text("Balaji M")

wait(driver,2)
#//*[@id="pickuptime"]
#/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/label[1]/div[1]/select[1]
pick_up_time=Select(driver.find_element_by_xpath('//*[@id="pickuptime"]'))
pick_up_time.select_by_visible_text("21:00")

Drop_location= wait(driver,2).until(EC.element_to_be_clickable((By.XPATH ,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/label[1]/div[1]/input[1]")))
Drop_location.send_keys('Medavakkam')

wait(driver,2)
priority=Select(driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[2]/div[1]/select[1]"))
priority.select_by_visible_text("High")

wait(driver,2)
prorgram=Select(driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[5]/div[1]/div[1]/select[1]"))
prorgram.select_by_visible_text("EarthLink Wave")

#//textarea[@id='ticketDesc']
ticket_desc=wait(driver,2).until(EC.element_to_be_clickable((By.XPATH ,"//textarea[@id='ticketDesc']")))
ticket_desc.click()
ticket_desc.send_keys("""I have booked OLA can on date
                        From: Addr1
                        To: Addr2
                        CRN: CRN########""")

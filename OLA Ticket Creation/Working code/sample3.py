import win32com.client
import re
import time


def ticket_creation(ticket_summary_info):
    #Help disk --> Ticket Creation
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait as wait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    import time
    driver=webdriver.Chrome()#chrome_options=options
    driver.maximize_window()
    driver.get('http://oneplive.prodapt.com/oneprodapt-new/login.htm#/helpdesk')

    try:
            create_button=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"//a[@class='primary-add-icon ng-scope']")))
            create_button.click()
    except:
            try:
                    create_button=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"//button[@title='Create Ticket']")))
                    create_button.click()
                    # To handle the Ratings Alert
                    rating_met="//span[@class='helpdesk-rating meh-o']"
                    check_all=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"//input[@id='checkall']")))
                    check_all.click()
                    rating_met=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"//span[@class='helpdesk-rating meh-o']")))
                    rating_met.click()
            except Exception as error:
                    print (erorr)
            print ('All done')

    Admin=wait(driver,15).until(EC.element_to_be_clickable((By.XPATH ,"//div[@class='top-accord clearfix']//ul//li[1]//input[1]")))
    Admin.click()
    time.sleep(10)
    #location_drop_down=wait(driver,15).until(EC.element_to_be_clickable((By.XPATH ,"//select[contains(@class,'ng-pristine ng-invalid ng-invalid-required ng-touched')]")))
    #location_drop_down.click()
    #wait(driver,15)
    location=Select(wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/label[1]/div[1]/select[1]"))))
    wait(driver,2)
    try:
            location.select_by_value('number:1')
    except:
            wait(driver,10)
            location.select_by_visible_text("OMR-IT")
            
    Type=Select(wait(driver,60).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[7]/div[1]/select[1]"))))

    Type.select_by_visible_text("Service Request")


    time.sleep(2)
    category=Select(wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[8]/div[1]/select[1]"))))
    category.select_by_visible_text("Cab Request")

    wait(driver,2)
    sub_category=Select(wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[9]/div[1]/select[1]"))))
    sub_category.select_by_visible_text("Pick Up and Drop")

    #wait(driver,15)
    #//*[@id="employee"]
    #Employee=Select(driver.find_element_by_xpath('//*[@id="employee"]'))
    Employee=Select(wait(driver,60).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="employee"]'))))
    Employee.select_by_visible_text("Balaji M")

    #Pickuptime
    wait(driver,3)
    #//*[@id="pickuptime"]
    #/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/label[1]/div[1]/select[1]
    pick_up_time=Select(wait(driver,60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="pickuptime"]'))))
    pick_up_time.select_by_visible_text("21:00")

    #Drop location
    Drop_location= wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/label[1]/div[1]/input[1]")))
    Drop_location.send_keys('Medavakkam')

    #Priority
    wait(driver,2)
    priority=Select(wait(driver,60).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[2]/div[1]/select[1]"))))
    priority.select_by_visible_text("High")

    #Program
    wait(driver,2)
    prorgram=Select(wait(driver,60).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/framework-form[1]/div[1]/form[1]/div[1]/div[2]/div[5]/div[1]/div[1]/select[1]"))))
    prorgram.select_by_visible_text("EarthLink Wave")

    #Ticket Summary
    ticket_desc=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"//textarea[@id='ticketDesc']")))
    ticket_desc.click()
    ticket_desc.send_keys(ticket_summary_info)

    #Submit Button
    Submit_Button=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="submit"]/button')))
    Submit_Button.click()
    wait(driver,60)
    driver.close()

# Define a function to extarct only the required info from the body content
def extract_trip_info(body):
    replaced=''
    start=re.finditer('<',body)
    start_dict={}
    for i,data in enumerate(start):
        start_dict[i]=data.start()

    #print ('############################')
    #print (start_dict)
    end=re.finditer('>',body)
    end_dict={}
    for i,data in enumerate(end):
        end_dict[i]=data.end()
    remove_text={}
    for key,value in start_dict.items():
        remove_text[key]=body[start_dict[key]:end_dict[key]]
    #print ('############################')
    #print (remove_text)

    Address_list=[]
    for key,value in remove_text.items():
        if key==0:
            replaced=body.replace(remove_text[key],'')
        else:
            replaced=replaced.replace(remove_text[key],'')
    #print (replaced.replace(' ','*'))
    replace_string="".join([s for s in replaced.strip().splitlines(True) if s.strip()])
    ticket_info={}
    #print (replace_string)
    for i in replace_string.splitlines():
        text=i.strip() 
        date_match=re.match('[0-9][0-9] [A-Z][a-z][a-z], [0-9][0-9][0-9][0-9]',text)
        if date_match:
            ticket_info['Date']=date_match.group()
        if text.startswith('CRN'):
            #print (text)
            ticket_info['CRN']=text
            Address_list.append(text)
        #print (text)
        matched=re.match('(^\d{2}:\d{2} [A-Z][A-Z])',text)
        if matched:
            travel_time=matched.group()
            if travel_time in text:
                am_index=text.index(travel_time)
                #print (text[am_index+8:].strip())
                Address_list.append([travel_time,text[am_index+8:].strip()])
                #ticket_info['ADDR1']=text[am_index+8:].strip()

    for num,data in enumerate(Address_list):
        if num==0:
            ticket_info['CRN']=data
        if num==1:
            ticket_info['Pick up Time']=data[0]
            ticket_info['Pick up Location']=data[1]
        if num==2:
            ticket_info['Drop Time']=data[0]
            ticket_info['Drop Location']=data[1]

    ticket_summary1='Date: ' +str(ticket_info['Date'])
    ticket_summary2='CRN Reference: '+str(ticket_info['CRN'])
    ticket_summary3='Pick up Time: '+ticket_info['Pick up Time']
    ticket_summary4='Pick up Location: '+ticket_info['Pick up Location']
    ticket_summary5='Drop Time: '+ticket_info['Drop Time']
    ticket_summary6='Drop Location: '+ticket_info['Drop Location']
    summ=ticket_summary1+'\n'+ticket_summary2+'\n'+ticket_summary3+'\n'+ticket_summary4+'\n'+ticket_summary5+'\n'+ticket_summary6
    return summ,str(ticket_info['Date'])

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
messages = inbox.Items
#print ('#############messages############')
print (str(messages))
#message = messages.GetFirst()
messages.Sort("[ReceivedTime]", True)
import datetime

# Get yesterdays date for the purpose of getting emails from this date
Today=(datetime.date.today()).strftime("%d-%m-%y")
d = (datetime.date.today() - datetime.timedelta (days=10)).strftime("%d-%m-%y")
#print (d)
Accumulative_trip_info={}
mail_count=0
mail_body=[]
for num,m in enumerate(messages):
  try:
    matched_sub=re.match("(?P<first>\w+)\W+(?P<second>\w+)\W+(?P<third>\w+)", m.Subject)
    if matched_sub and (m.SentOn).strftime("%d-%m-%y") > d:
            if m.UnRead == True and matched_sub.group(1)=='Your' and matched_sub.group(3)== 'ride':
                #print (matched_sub)
                #print (m.SentOn)
                mail_count=mail_count+1
                message = messages.GetNext ()
                body_content = m.Body
                sender=m.Sender
                #print ('Sender :'+str(sender)+'  '+'Body :'+ str(body_content))
                print ('########body_content###########')
                content=str(body_content)
                mail_body.append(content)
                #trip_info=extract_trip_info(content)
                #Accumulative_trip_info[mail_count]=trip_info
  except Exception as error:
     print (error)

######################################################
Accumulative_trip_info={}
count=0
for i in mail_body:
    count=count+1
    address,date=extract_trip_info(i)
    Accumulative_trip_info[date]=address
#print(Accumulative_trip_info)

statement1='I have booked OLA cab on below day.'
statement2='I have booked OLA cab on below days.'

if len(Accumulative_trip_info)> 1:
    ticket_summary_info=statement2+'\n'
    for key,value in Accumulative_trip_info.items():
        addr=value+'\n'
        ticket_summary_info=ticket_summary_info+addr+'\n'
else:
    ticket_summary_info=statement1+'\n'
    for key,value in Accumulative_trip_info.items():
        addr=value+'\n'
        ticket_summary_info=ticket_summary_info+addr+'\n'
print (ticket_summary_info)
if len(ticket_summary_info)>1:
    print ('Need to create a ticket')
    #ticket_creation(ticket_summary_info)

# importing the modules
import time
import win32com.client
from selenium import webdriver
import csv
import pandas as pd
import re
from datetime import date,timedelta,datetime

from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread

import pythoncom

import win32api as win
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import shutil

def generate_Report(*args,filename_path):
        for data in os.listdir(filename_path):
                if '_Assingee_status' in data or '_Priority_status' in data:
                        print (data)
                        os.remove(filename_path+"\\"+data)
                        print (filename_path+"\\"+data + ' is deleted')

        for file in args:
                df= pd.read_csv(filename_path+"\\"+file,encoding = "ISO-8859-1")
                plt.figure(figsize=(15,10))
                sns.countplot(x='Assignee+',data=df,hue='Status*')
                plt.xticks(rotation=15,ha="right")
                plt.savefig(filename_path+"\\"+file[:-4]+'_Assingee_status.png', dpi=100)
                #plt.show()
                sns.countplot(x='Priority*',data=df,hue='Status*')
                plt.savefig(filename_path+"\\"+file[:-4]+'_Priority_status.png', dpi=100)
                #plt.show()

def copy_file(source,destination):
        for data in os.listdir(source):
                if 'WinLink_Report' in data:
                        shutil.copy(os.path.join(source,'WinLink_Report.csv'), os.path.join(destination,'WinLink_Report.csv'))

def get_download_path():
        global full_path
        name=win.GetUserNameEx(win.NameSamCompatible)
        rename=re.sub(r'\W', " ", name)
        #print (rename)
        pos=rename.find(' ')
        #print (pos)
        path2='Downloads'
        path1='Users'
        #print (name)
        #print (name[8:])        
        user_name=name[pos+1:]
        full_path='C:'+"\\"+path1+"\\"+user_name+"\\"+path2
        #print (full_path)
        print (full_path)
        return full_path,full_path+"\\"+'WinLink_Report'
    
def start_thread():
    t=Thread(target=open_browser,args=(username_entry.get(),password_entry.get(),))
    t.start()
def open_browser(username,password):
 try:
  if username!='' and password !='':
    pythoncom.CoInitialize()
    button.grid_forget()
    progessbar.grid(row=5,column=1,sticky=E+W,padx=10)
    progessbar.config(maximum=100)
    progessbar.start()
    '''
    for data in os.listdir(get_download_path()[0]):
            if 'WinLink_Report' in data:
                    try:
                        os.remove(get_download_path()[0]+"\\"+data)
                    except:
                        pass
    '''
    if os.path.exists(os.path.join(get_download_path()[1])) :
        print ('Alread Exists')
        for data in os.listdir(get_download_path()[1]):
                try:
                        os.remove(get_download_path()[1]+"\\"+data)
                except:
                        pass
    else:
        os.mkdir(get_download_path()[1])
    itsm_query=''''Assigned Group*+' = "WinLink Application Support"'''
    prefs = {'download.default_directory': get_download_path()[1]}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    window_before = driver.window_handles[0]
    try:
        driver.get('https://itsm.windstream.com/')
        time.sleep(30)
        aw=True
        while aw:
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.Sendkeys(username)
            shell.Sendkeys('{TAB}')
            shell.Sendkeys(password)
            shell.Sendkeys('{ENTER}')
            aw=False
        
    except Exception as e:
        print (e)
        progessbar.grid_forget()
        messagebox.showinfo('Warning','Connect VPN/check your username and password')
        
    try:
        alert_wait=EC.alert_is_present()
        wait(driver ,30).until(alert_wait)
        alert=driver.switch_to_alert()
        alert.accept()
    except:
        pass
    logo_present = wait(driver,60).until(EC.presence_of_element_located((By.ID, 'reg_img_304316340')))
    try:
        alert_wait=EC.alert_is_present()
        wait(driver ,10).until(alert_wait)
        alert=driver.switch_to_alert()
        alert.accept()
    except:
        pass
    level_element= wait(driver,60).until(EC.presence_of_element_located((By.ID,'reg_img_304316340')))
    level_element.click()
    wait(driver,20)
    child_element= wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"//span[text()='Incident Management']")))
    child_element.click()
    wait(driver,20)
    #Changed the code to click 'Search Change' instead of clicking 'Change management console'
    child_element_1=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,"//span[text()='Search Incident']")))
    child_element_1.click()
    wait(driver,25)
    try:
        alert_wait=EC.alert_is_present()
        wait(driver ,10).until(alert_wait)
        alert=driver.switch_to_alert()
        alert.accept()
    except:
        pass
    #Need to add the code for clicking advance search button using xpath='//*[@id="TBadvancedsearch"]'
    adv_button= wait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[3]/a[3]")))
    if adv_button.is_displayed():
        ActionChains(driver).double_click(adv_button).perform()
    else:
        print('Not displayed')
    #Need to add the code for sending ITSM query to text area
    wait(driver,50)
    text_area=wait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[5]/table[2]/tbody/tr/td[1]/textarea[@id="arid1005"]')))
    text_area.click()
    text_area.send_keys(itsm_query)
    #Need to add the code to click the search button
    wait(driver,5)
    search=wait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[2]/div/div')))
    search.click()
    wait(driver,100)
    try:
        selectall=wait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'html[1]/body[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[3]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/div[3]/fieldset[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/a[2]')))
        selectall.click()  #selectall
        time.sleep(2)
    except Exception as e:
        print (e)
        progessbar.grid_forget()
        button.tkraise()
        button.grid(row=5,column=1,pady=10)
    report=wait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[1]/a[1]')))
    report.click() #report
    window_after = driver.window_handles[1]
    wait(driver,60)
    #Trnasfreing the window control
    driver.switch_to.window(window_after)
    wait(driver,30)
    #searching the Prodapt_ASAP_Daily_Report and clicking
    prodapt_asap_daily_report=wait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Prodapt_ASAP_Daily_Report']")))
    prodapt_asap_daily_report.click()
    s=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='arid_WIN_0_2000053']")))
    s.click() #To clcick the Destination drop down
    f=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/table/tbody/tr[2]/td[1]')))
    webdriver.ActionChains(driver).move_to_element(f).click(f).perform()# to select the File
    w=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='arid_WIN_0_2000056']")))
    w.click()#Formtdropdownbutton
    c=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/table/tbody/tr[2]/td[1]')))# clicking CSV
    webdriver.ActionChains(driver).move_to_element(c).click(c).perform()
    textname=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='arid_WIN_0_2000057']")))
    wait(driver,1)
    textname.click()#to click the filename
    textname.clear()
    textname.send_keys('WinLink_Report.csv')
    run=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"reg_img_93272\"]")))
    run.click()
    time.sleep(30)
    driver.close()
    driver.switch_to.window(window_before)    
    logout=wait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="WIN_0_300000044"]/div/div')))
    logout.click()
    driver.quit
    progessbar.grid_forget()
    button.tkraise()
    button.grid(row=5,column=1,pady=10)
    
  else:
     messagebox.showinfo('Warning..','Please check your username and password')
 except Exception as error:
    messagebox.showinfo('Error..',str(error))
    progessbar.grid_forget()
    button.tkraise()
    button.grid(row=5,column=1,pady=10)


def prior_week_end():
    return datetime.now() - timedelta(days=((datetime.now().isoweekday() + 1) % 7))
    #Function to get the start day of the current week
def prior_week_start():
    return prior_week_end() - timedelta(days=6)


class month_week_report():    
    def __init__(self,previous_week_start,previous_week_end,month_start,month_end):
        self.previous_week_start=previous_week_start
        self.previous_week_end=previous_week_end
        self.month_start=month_start
        self.month_end=month_end
        
    def week_report(self,reported_date):
        if self.previous_week_end >= datetime.strptime(reported_date[0:len(reported_date)-3],'%m/%d/%Y %H:%M:%S') >= self.previous_week_start:
            return True
    def month_report(self,reported_date):
        if self.month_end >= datetime.strptime(reported_date[0:len(reported_date)-3],'%m/%d/%Y %H:%M:%S') >= self.month_start:
            return True
     


def  create_files(file_path):
  if to_address_entry.get() !='':
    #To get the last week start date and end date
    #copy_file(get_download_path()[0],get_download_path()[1])
    previous_week_start=prior_week_start()
    previous_week_end=prior_week_end()

    #To get the last month start date and end date
    month_start=(datetime.today().replace(day=1)-timedelta(days=1)).replace(day=1)
    month_end=datetime.today().replace(day=1)-timedelta(days=1)

    #initializing the class 
    mon_week_obj=month_week_report(previous_week_start,previous_week_end,month_start,month_end)
    
    with open(file_path+"\\"+'WinLink_Report.csv','r') as file:
        data=csv.reader(file,delimiter=',')
        for num,i in enumerate(data):
            if 'AM' in i[3] or 'PM' in i[3]:
                if mon_week_obj.week_report(i[3]):
                    dict_week[num]=i
                if mon_week_obj.month_report(i[3]):
                    dict_month[num]=i

    fieldnames =['Assigned Group*+',
    'Case Type*',
    'Incident ID*+',	
    'Reported Date+',
    'Last Resolved Date',
    'Assignee+',
    'Priority*',
    'Status*',	
    'SLM Real Time Status',	
    'Summary*',	
    'Notes',	
    'Resolution',	
    'Resolution Categorization Tier 1',	
    'Resolution Categorization Tier 2',	
    'Resolution Categorization Tier 3',	
    'Re-Opened Date',
    'Product Categorization Tier 1',	
    'Product Categorization Tier 2',	
    'Product Categorization Tier 3',	
    'Impact Start Date/Time+',	
    'Impact Stop Date/Time+',
    'First Name+',	
    'Last Name+',
    'Status Reason',	
    'Last Modified Date']
    
    with open(file_path+"\\"+'WinLink_Report_Week.csv','w+',newline='') as f:
        writer = csv.writer(f,delimiter = ',')
        writer.writerow(columns for columns in fieldnames)
        for key,value in dict_week.items():
             writer.writerow(data for data in value)

    with open(file_path+"\\"+'WinLink_Report_Month.csv','w+',newline='') as f:
        writer = csv.writer(f,delimiter = ',')
        writer.writerow(columns for columns in fieldnames)
        for key,value in dict_month.items():
             writer.writerow(data for data in value)
    
    generate_Report('WinLink_Report_Week.csv','WinLink_Report_Month.csv',filename_path=file_path)
    send_mail(file_path,to_address_entry.get())
  else:
     messagebox.showinfo('Warning..','Please provide To email address')

def send_mail(file_path,to_address):
 try:
    Application = win32com.client.dynamic.Dispatch('outlook.application')
    #Application= win32com.client.Dispatch('outlook.application')
    print (Application)
    print (Application.Session.Accounts)
    oacctouse= None
    for oacc in Application.Session.Accounts:
            print (oacc.SmtpAddress)
            if oacc.SmtpAddress == "Balaji.Masilamani@windstream.com" or oacc.SmtpAddress =="Mohammed.Sadik@windstream.com":
                    oacctouse = oacc                    
                    break
    #print(oacc)
    mail = Application.CreateItem(0)
    #mail_html = "<h2>Overall Backlog</h2><table border='1' style='border-collapse:collapse' class='table bg-primary'><tr><th>Incident</th><td>472</td></tr><tr><th>Request</th><td>17</td></tr></table><table border='1' style='border-collapse:collapse;text-align:left' class='table bg-info'><tr><th>IT-OSS - M6 (ASAP/TSG) </th><td>177</td></tr><tr><th>IT-OSS - M6 (NextGen) </th><td>197</td></tr><tr><th>IT-OSS - M6 (PAETEC) </th><td>103</td></tr><tr><th>IT-OSS - M6 (EarthLink) </th><td>18</td></tr></table><table class='table bg-success'><tr><td><b>Total Number of tickets assigned in Prodapt</b></td><td><b>489</b></td></tr></table>"
    #print(mail_html)
    if oacctouse:
            mail._oleobj_.Invoke(*(64209, 0, 8, 0, oacctouse))


    #mail.To = 'madanraj.c@prodapt.com;sariga.s@prodapt.com;kavitha.sekar@prodapt.com;devanand.s@prodapt.com'
    #mail.cc = 'suchitra.bc@prodapt.com;annamalai.d@prodapt.com;ravindran.n@prodapt.com;sudha.r@prodapt.com'
    mail.To=to_address       
    mail.Subject = 'Daily Backlog Report'
    mail.Body = '*WinLink Report Generation*'
    try:
            attachment0  = file_path+"\\"+'WinLink_Report.csv'
            attachment1  = file_path+"\\"+'WinLink_Report_Month.csv'
            attachment2  = file_path+"\\"+'WinLink_Report_Week.csv'
            mail.Attachments.Add(attachment0)
            mail.Attachments.Add(attachment1)
            mail.Attachments.Add(attachment2)
            attachment3=mail.Attachments.Add(file_path+"\\"+'WinLink_Report_Month_Assingee_status.png')
            attachment3.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId1")
            attachment4=mail.Attachments.Add(file_path+"\\"+'WinLink_Report_Month_Priority_status.png')
            attachment4.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId2")
            attachment5=mail.Attachments.Add(file_path+"\\"+'WinLink_Report_Week_Assingee_status.png')
            attachment5.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId3")
            attachment6=mail.Attachments.Add(file_path+"\\"+'WinLink_Report_Week_Priority_status.png')
            attachment6.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId4")
            html=""" <html>
                      <font  face="calibri" size="3"  >Hi Team,</font><br><br>
                      <font  face="calibri" size="3"  >Please find the attached WinLink_Week and WinLink_Month report.</font><br><br>
                      <font face="calibri" size="4" >Monthly Report:</h2><br>
                      <font face="calibri" size="3">Assingee vs Status </font>
                      <img src="cid:MyId1" ></img>
                      <font face="calibri" size="3">Status vs Priority </font>
                      <img src="cid:MyId2" ></img><br><br>
                      <font face="calibri" size="4" >Weekly Report:</h2><br>
                      <font face="calibri" size="3">Assingee vs Status </font>
                      <img src="cid:MyId3" ></img>
                      <font face="calibri" size="3">Status vs Priority </font>
                      <img src="cid:MyId4" ></img>
                      """
            mail.HTMLBody = html+"<br><b><span style='color:gray'>This is an automated e-mail</span></b> </html>"
    except Exception as error:
             messagebox.showinfo('Files Error..',error)
    mail.Send()
    print ('Mail Sent')
 except Exception as error:
   messagebox.showinfo('Sending Mail..',error)
         

if __name__=='__main__':    
    #creating the loging info page
    root=Tk()
    s = ttk.Style()
    s.theme_use('classic')
    s.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
    root.geometry("600x300")
    root.title('MYOS Support_ITSM Reporting Tool')
    root.resizable(False, False)
    root.configure(background='sky blue')
    username=Label(root,text='User Name/Nid:',
                   #bg='sky blue',
                   font=('Arial',10,'bold'))
    username.grid(row=0,column=0,sticky='w',padx=100,pady=25)
    username_entry=Entry(root,bd=2,width=30)
    username_entry.grid(row=0,column=1,sticky='w')
    password=Label(root,text='Password:',
                   #bg='sky blue',
                   font=('Arial',10,'bold'))
    password.grid(row=1,column=0,sticky='e',pady=10,padx=100)
    password_entry=Entry(root,bd=2,show='*',width=30)
    password_entry.grid(row=1,column=1,sticky='w')

    to_address=Label(root,text='Email To:',
                     #bg='sky blue',
                     font=('Arial',10,'bold'))
    to_address.grid(row=3,column=0,sticky=E,pady=10,padx=100)
    to_address_entry=Entry(root,bd=2,width=30)
    to_address_entry.grid(row=3,column=1,sticky=W)
    var = IntVar()
    progessbar = ttk.Progressbar (root, variable=var, orient='horizontal', length=150,style="red.Horizontal.TProgressbar")
    progessbar.grid(row=4,column=1,sticky=E,padx=10)
    var.set(0)
    progessbar.grid_forget()
    button=Button(root,text='Download Report',bg='sky blue'
                  ,command=start_thread
                  )
    button.grid(row=5,column=1,pady=10)
    report_preparation=Button(root,text='Report Preparation',bg='sky blue'
                  ,command= lambda : create_files(get_download_path()[1])
                  )
    report_preparation.grid(row=6,column=1,pady=10)


    dict_week={}
    dict_month={}
    #send_mail()
    #get_download_path()
    root.mainloop()





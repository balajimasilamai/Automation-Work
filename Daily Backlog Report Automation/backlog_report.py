"""
Created on Wed Nov 28 14:25:24 2018

@author: Balaji Masilamani,Madan Chenchuraju
"""

#Merging all the packages into single file
#============ Importing the required libraries==========================================================
#import tkinter
from  tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tkscrolled
from tkinter import ttk
#import creating_db
import os
#import Backlog_report_generator_loop
import re
#import copy_paste
import time
#import final_flow
import datetime
import sqlite3
#===============For selenium ====================
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
#import os
import win32com.client
#========== For copy paste =====================
import win32api
#import datetime
import os
import shutil
import re
#=====For final flow excel manipulation ##############

#import win32com.client as win32
#import xlwings as xw
#import win32api
import time
import csv
import pandas as pd
from threading import Thread
import pythoncom
#############################################################################
file_names=[]
file_name=[ 'backlog_',
            'graph_',
            'Open_',
            'Closed_',
            'Request_Open_',
            'Paetec_',
            'Paetec_Closed_',
            'paetec_request_',
            'paetec_ris_'
            ]

dict_day={'January':'01',
          'February':'02',
          'March':'03',
          'April':'04',
          'May':'05',
          'June':'06',
          'July':'07',
          'August':'08',
          'September':'09',
          'October':'10',
          'November':'11',
          'December':'12'}
header_list=[
	'Assigned Group*+',	
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
	'Last Modified Date',
	]
######################  creating creating_db classs  ##############################

class creating_db():
	connection=sqlite3.connect('backlog_report.db',check_same_thread=False)
	#Connecting to the database
	c=connection.cursor()
	op=c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='backlog_report'")
	print (op)
	for i,data in enumerate(op.fetchall()):
		print (i)
		print (data)
		if data[0]==1:
			print ('Table Alreay exists with some data')
			op1=c.execute("SELECT * from backlog_report")       
			for i1,data1 in enumerate(op1.fetchall()):
				print (data1)
		else:
			#creating the table if not available
			c.execute("""create table IF NOT EXISTS backlog_report (name varchar2(100))""")
			print ('table is created')
			c.execute("insert into backlog_report(name) values  ('Arivanand Murugesan')")
			c.execute("insert into backlog_report (name) values ('Jayaprakash Subramanian')") 
			c.execute("insert into backlog_report (name) values ('Krishna Nagarajan')")
			c.execute("insert into backlog_report (name) values ('Lalithkiran Gopikrishna') ")
			c.execute("insert into backlog_report (name) values ('Mohamed Musthafa Kani') ")
			c.execute("insert into backlog_report (name) values ('Praveena Mohanasundaram') ")
			c.execute("insert into backlog_report (name) values ('Ravindran Naarayanan') ")
			c.execute("insert into backlog_report (name) values ('Suchitra Chandrasekaran')") 
			c.execute("insert into backlog_report (name) values ('Suriya S Kanthan') ")
			c.execute("insert into backlog_report (name) values ('Yuvaraj Murugan') ")
			c.execute("insert into backlog_report (name) values ('Anitha Thangavel') ")
			c.execute("insert into backlog_report (name) values ('Asmita Prakash') ")
			c.execute("insert into backlog_report (name) values ('Diwakar Vasu') ")
			c.execute("insert into backlog_report (name) values ('Naresh Elango') ")
			c.execute("insert into backlog_report (name) values ('Aravind Subrmanian') ")
			c.execute("insert into backlog_report (name) values ('Santhosh Mahadevan') ")
			c.execute("insert into backlog_report (name) values ('Jeyalakshmi Sivaselvaraj')  ")
			c.execute("insert into backlog_report (name) values ('Sariga Suresh') ")
			c.execute("insert into backlog_report (name) values ('Madan Chenchuraju') ")
			c.execute("insert into backlog_report (name)  values ('Kavitha Sekar')")
			print ('Some the data are inserted')
			connection.commit()
			print ('Chanegs have been commited in DB')
	op=c.execute("SELECT * from backlog_report")       
	for i,data in enumerate(op.fetchall()):
		print (data)


	def insert(self,Name):
		global connection
		#c=connection.cursor()
		self.c.execute("insert into backlog_report (name) values (?)",(Name,))
		self.connection.commit()
	def delete(self,Name):
		global connection
		#c=connection.cursor()
		op=self.c.execute("delete from backlog_report where name =?",(Name,))
		print (op.fetchall())
		self.connection.commit()

	def Paetec_open_query(self,):
		global connection
		#c=connection.cursor()
		op=self.c.execute('select * from backlog_report')
		petec_open1='''('Assigned Group*+' = "IT-OSS - M6 (PAETEC)") AND (NOT ('Status*' = "Resolved" OR 'Status*' = "Closed" OR 'Status*' = "Cancelled")) AND ( 'Case Type*' ="Incident" ) AND  '''
		text=''' 'Assignee+' = "'''
		petec_open2=''
		for num,i in enumerate(op.fetchall()):
			#print (i[0])
			if num ==0:
				petec_open2=petec_open2+text+i[0]+'''"'''
			else:
				petec_open2=petec_open2+' OR '+text+i[0]+'''"'''        
		print (petec_open1 + '( '+petec_open2+' )' )
		return petec_open1 + '( '+petec_open2+' )' 
		connection.commit()
	
	def Paetec_Closed_query(self,current_month,next_month,respective_year1,respective_year2):
		global connection
		#c=connection.cursor()
		op=self.c.execute('select * from backlog_report')
		petec_Closed1='''('Assigned Group*+' = "IT-OSS - M6 (PAETEC)")  AND ( 'Case Type*' ="Incident" ) AND '''
		petec_Closed3=''' AND (('Last Resolved Date' >= "'''+str(current_month)+'/01/'+str(respective_year1)+'''" AND 'Last Resolved Date' < "'''+str(next_month)+'/01/'+str(respective_year2)+'"))'
		text=''' 'Assignee+' = "'''
		petec_Closed2=''
		for num,i in enumerate(op.fetchall()):
			#print (i[0])
			if num ==0:
				petec_Closed2=petec_Closed2+text+i[0]+'''"'''
			else:
				petec_Closed2=petec_Closed2+' OR '+text+i[0]+'''"'''        
		print (petec_Closed1 + '( '+petec_Closed2+' )' + petec_Closed3)
		self.connection.commit()
		return petec_Closed1 + '( '+petec_Closed2+' )' + petec_Closed3
		
	def paetec_request_query(self,):
		global connection
		#c=connection.cursor()
		op=self.c.execute('select * from backlog_report')
		paetec_request1='''('Assigned Group*+' = "IT-OSS - M6 (PAETEC)") AND (NOT ('Status*' = "Resolved" OR 'Status*' = "Closed" OR 'Status*' = "Cancelled")) AND  '''
		text=''' 'Assignee+' = "'''
		paetec_request2=''
		for num,i in enumerate(op.fetchall()):
			#print (i[0])
			if num ==0:
			   paetec_request2=paetec_request2+text+i[0]+'''"'''
			else:
			   paetec_request2=paetec_request2+' OR '+text+i[0]+'''"'''        
		print (paetec_request1 + '( '+paetec_request2+' )'  + ''' AND ( 'Case Type*' ="Request" )''')
		self.connection.commit()
		return paetec_request1 + '( '+paetec_request2+' )' + ''' AND ( 'Case Type*' ="Request" ) '''
		#connection.commit()
	def paetec_ris_query(self,):
		global connection
		#c=connection.cursor()
		op=self.c.execute('select * from backlog_report')
		paetec_ris1='''('Assigned Group*+' = "IT-OSS - M6 (PAETEC)") AND (NOT ('Status*' = "Resolved" OR 'Status*' = "Closed" OR 'Status*' = "Cancelled")) AND  '''
		text=''' 'Assignee+' = "'''
		paetec_ris2=''
		for num,i in enumerate(op.fetchall()):
			#print (i[0])
			if num ==0:
			   paetec_ris2=paetec_ris2+text+i[0]+'''"'''
			else:
			   paetec_ris2=paetec_ris2+' OR '+text+i[0]+'''"'''        
		print (paetec_ris1 + '( '+paetec_ris2+' )'  + ''' AND ( 'Case Type*' ="Ris" )''')
		self.connection.commit()
		return paetec_ris1 + '( '+paetec_ris2+' )' + ''' AND ( 'Case Type*' ="Ris" ) '''
		#connection.commit()
	def resolution_count(self,):
		return    '''(('Assigned Group*+' = "IT-OSS - M6 (ASAP/TSG)") OR ('Assigned Group*+' = "IT-OSS - M6 (PAETEC)") OR ('Assigned Group*+' = "IT-OSS - M6 (NextGen)") OR ('Assigned Group*+' = "IT-OSS - M5 (NuVox)") OR ('Assigned Group*+' = "IT-OSS - M6 (EarthLink)"))  AND (NOT('Status*' = "Resolved" OR 'Status*' = "Closed" OR 'Status*' = "Cancelled")) '''

	def close_connection(self):
		global connection
		self.connection.close()
		#print ('DB connection has been disabled')
		quit()
######################################################################################
full_path=''
def get_download_path():
        global full_path
        name=win32api.GetUserNameEx(win32api.NameSamCompatible)
        rename=re.sub(r'\W', " ", name)
        #print (rename)
        pos=rename.find(' ')
        #print (pos)
        path2='Downloads'
        path1='Users'
        #print (name)
        #print (name[8:])        
        user_name=name[pos+1:]
        #print ('user name :'+name)
        full_path='C:'+"\\"+path1+"\\"+user_name+"\\"+path2
        #print (full_path)
        return full_path
#print ('Donload path')
#print (get_download_path())
#==== Backlog generator function ========================
def download_file(query,file_name):
 try:
    file_names=file_name
    ##################################################
    #This portion is added in UI.py in order to avoid multiple importing of the same library module.
    '''
    #To get the current date and time
    file_names=['Open_',
            'Closed_',
            'Request_Open_',
            'Paetec_',
            'Paetec_Closed_',
            'paetec_request_',
            'paetec_ris_'
            ]
    current_time=datetime.date.today().strftime("%B %dth, %Y")
    a=datetime.date.today().strftime("%B")
    b=datetime.date.today().strftime("%dth")
    c=datetime.date.today().strftime("%Y")
    print (current_time)
    print (a)
    print (b)
    print (c)
    file_name=b[0:]+a[0:3]+c[2:4]
    print (file_name)

    for i in range(0,len(file_names)):
        print (file_names[i]+str(file_name))
    '''

    ###########################################
    
    #Selenium part to download the files
    #with VPN
    for i in os.listdir(get_download_path()):
            #print ()
            name=str(i)[0:-4]
            if name in file_names:
                    #print (name)
                    #print (get_download_path()+'\\'+i)
                    os.remove(get_download_path()+'\\'+i)
    files_donload.grid_forget()
    pbstyle = ttk.Style()
    #print (pbstyle.theme_names())
    pbstyle.theme_use('clam')
    pbstyle.configure("red.Horizontal.TProgressbar", foreground="Green", background="Green")

    var=IntVar()
    prog=ttk.Progressbar(frame,variable=var,
                         orient ="horizontal",
                         length = 100,
                         mode ="determinate",
                         style='red.Horizontal.TProgressbar')
    prog.grid(row=3,column=1,sticky="w")
    prog.start(1000)
    var.set(1)
    prog.configure(maximum=len(query))
    driver=webdriver.Chrome()#chrome_options=options
    driver.maximize_window()
    window_before = driver.window_handles[0]
    try:
        driver.get('https://itsm.windstream.com/')
        time.sleep(20)
        #WebDriverWait(driver,60)
        pythoncom.CoInitialize()
        try:
            alert_wait=EC.alert_is_present()
            wait(driver ,30).until(alert_wait)
            alert=driver.switch_to_alert()
            print (alert.text)
            alert.accept()
        except:
            pass
        aw=True
        while aw:
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.Sendkeys('n9941391')#n9941391#n9930786#n9936896#n9982332
            shell.Sendkeys('{TAB}')
            shell.Sendkeys('Dec2018$')#Dec2018$#MssCSO003@#God@1234#Nov@2018
            shell.Sendkeys('{ENTER}')
            aw=False
            try:
                alert_wait=EC.alert_is_present()
                wait(driver ,120).until(alert_wait)
                alert=driver.switch_to_alert()
                #alert=driver.switch_to.alert.accept()
                print (alert.text)
                alert.send_keys('{ENTER}')
                alert.accept()
            except:
                pass
        
    except Exception as e:
        print (e)
    try:
        alert_wait=EC.alert_is_present()
        wait(driver ,30).until(alert_wait)
        alert=driver.switch_to_alert()
        print (alert.text)
        alert.accept()
    except:
        pass
    try:
        alert_wait=EC.alert_is_present()
        wait(driver ,200).until(alert_wait)
        alert=driver.switch_to.alert.accept()
        print (alert.text)
        alert.accept()
    except:
        pass
    try:
        alert_wait=EC.alert_is_present()
        wait(driver ,200).until(alert_wait)
        alert=driver.switch_to.alert.accept()
        print (alert.text)
        alert.accept()
    except:
        pass
    time.sleep(10)
    appclicker=driver.find_element_by_xpath('//*[@id="reg_img_304316340"]').click()
    time.sleep(5)

    print ('Application button clicked')

    element=driver.find_element_by_xpath("//span[text()='Incident Management']") 

    webdriver.ActionChains(driver).move_to_element(element).click(element).perform() 
    time.sleep(10)

    driver.find_element_by_xpath("//span[text()='Search Incident']").click()
    #alerter()
    print ('Going to Search Indicent')
    time.sleep(15)
    # Clicking Adnavce search buton
    driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[3]/a[3]").click()
    
    for i in range(0,len(query)):
        #print (query[i])
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
        if i!=0:
            time.sleep(6)
            #Xpath to select New search
            new_search=driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[3]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/div[3]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/span[1]")
            new_search.click()
        # Clicking Text Area
        time.sleep(0.025)
        text_area=driver.find_element_by_xpath('//fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[5]/table[2]/tbody/tr/td[1]/textarea[@id="arid1005"]')
        time.sleep(0.025)
        text_area.click()
        time.sleep(0.025)
        text_area.send_keys(query[i])
        time.sleep(15)
        print ('Searching')
        # Clicking the search button
        driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[2]/div/div').click() #search
        time.sleep(30)
        #text_area.clear()
        #selecting all button
        try:
            driver.find_element_by_xpath('html[1]/body[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[3]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/div[3]/fieldset[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/a[2]').click()  #selectall
            time.sleep(2)
        except:
            insert('Unable to find any records for the file '+file_names[i]+'.csv')
            shell.Sendkeys('{ENTER}')
            if i==len(query)-1:
                    with open (get_download_path()+'\\'+file_names[i]+'.csv','w+') as file:
                        writer = csv.writer(file)
                        writer.writerow([g for g in header_list])
                    insert('Created the Empty file for '+file_names[i]+'.csv')
            continue
        #Selecting Report button
        driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[1]/a[1]').click() #report
        # New Window will open
        window_after = driver.window_handles[1]
        time.sleep(15)
        #Trnasfreing the window control
        driver.switch_to.window(window_after)
        time.sleep(15)
        #searching the Prodapt_ASAP_Daily_Report and clicking
        driver.find_element_by_xpath("//span[text()='Prodapt_ASAP_Daily_Report']").click()
        s=(driver.find_element_by_xpath("//*[@id='arid_WIN_0_2000053']")).click() #To clcick the Destination drop down
        time.sleep(0.025)
        f=driver.find_element_by_xpath('/html/body/div[3]/div[2]/table/tbody/tr[2]/td[1]')# to select the File
        webdriver.ActionChains(driver).move_to_element(f).click(f).perform()
        time.sleep(0.5)
        w=driver.find_element_by_xpath("//*[@id='arid_WIN_0_2000056']").click()#Formtdropdownbutton
        c=driver.find_element_by_xpath('/html/body/div[3]/div[2]/table/tbody/tr[2]/td[1]')# clicking CSV
        webdriver.ActionChains(driver).move_to_element(c).click(c).perform()
        time.sleep(0.5)
        #fname=driver.find_element_by_xpath('//*[@id="WIN_0_2000057"]/a/img').click() #to click the Filename menu button
        textname=driver.find_element_by_xpath("//*[@id='arid_WIN_0_2000057']")#to click the filename
        time.sleep(0.002)
        textname.click()
        textname.clear()
        textname.send_keys((file_names[i]+'.csv'))
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id=\"reg_img_93272\"]").click()
        insert(file_names[i]+'.csv'+ ' is downloaded')
        time.sleep(25)
        driver.close()
        driver.switch_to.window(window_before)
        var.set(i+1)
    driver.close()
    prog.grid_forget()
    files_donload.tkraise()
    files_donload.grid(row=3,column=1,sticky="w")
 except Exception as error:
         insert (str(error))

    

########################
###== For copy paste function =============
class copy_paste():
    def get_download_path():
        global full_path
        name=win32api.GetUserNameEx(win32api.NameSamCompatible)
        rename=re.sub(r'\W', " ", name)
        #print (rename)
        pos=rename.find(' ')
        #print (pos)
        path2='Downloads'
        path1='Users'
        #print (name)
        #print (name[8:])        
        user_name=name[pos+1:]
        #print ('user name :'+name)
        full_path='C:'+"\\"+path1+"\\"+user_name+"\\"+path2
        print (full_path)
        return full_path
    #To move the file from download path to the checkout folder
    def move_file(get_download_path,to_path,dt_time):
        #file_name=day[0:]+month[0:3]+year[2:4]
        #print (file_name)
        #file_name1='10thOct'
        #if not os.path.isdir(to_path):
            #os.mkdir(to_path)
            #print ('dir created')
        #else:
            #print ('Already exists ')
        count=0
        for i in os.listdir(get_download_path):
            if dt_time in i:
                print (i)
                print (to_path+i)
                shutil.copy(os.path.join(get_download_path,i), os.path.join(to_path,i))
                count=count+1
        return count
    def delete(delete_path):
        #delete_path='D:\\testing-backlog-report\\'
        for file in os.listdir(delete_path):
                if '.csv' in file:
                        os.remove(os.path.join(delete_path,file))
                        print (file +' is deleted')
##====== For final flow excel manipulation =========================
def start_excel(path,file_name,paetec_request,paetec_ris,current_day,date_filed,
                filename1,filename2):
 try:
    go.grid_forget()
    pbstyle = ttk.Style()
    #print (pbstyle.theme_names())
    pbstyle.theme_use('clam')
    pbstyle.configure("red.Horizontal.TProgressbar", foreground="Green", background="Green")

    var=IntVar()
    prog=ttk.Progressbar(frame,variable=var,
                         orient ="horizontal",
                         length = 100,
                         mode ="determinate",
                         style='red.Horizontal.TProgressbar')
    prog.grid(row=4,column=1,sticky="w")
    prog.start(1000)
    var.set(1)
    prog.configure(maximum=10)
    insert ('Opening the Excel sheet')
    #Get the checkout folder path
    #path='D:\\testing-backlog-report'
    excel = win32com.client.gencache.EnsureDispatch('Excel.Application')
    excel.DisplayAlerts = True
    wb = excel.Workbooks.Open(path+file_name)
    ws = wb.Worksheets("Highlevel Bench Mark")
    lastCol = ws.UsedRange.Columns.Count
    lastRow = ws.UsedRange.Rows.Count
    print (lastCol)
    print (lastRow)
    print (ws.Cells(2, lastCol).Value)
    print (ws.Cells(3, lastCol).Value)
    # create a new column in Highlevel Bench Mark sheet
    excel.Application.Run("Macro_copy")
    time.sleep(2)
    lastCol_new = ws.UsedRange.Columns.Count
    print (lastCol_new)
    print (ws.Cells(2, lastCol_new).Value)
    print (ws.Cells(3, lastCol_new).Value)
    #updating the date and day cells in Highlevel Bench Mark sheet
    ws.Cells(2, lastCol_new).Value=current_day
    ws.Cells(3, lastCol_new).Value=date_filed

    
    # Copy the values for the PAETEC Request sheet
    ws = wb.Worksheets("PAETEC Request")
    #This loop for PAETEC Request sheet
    row=1
    col=1
    with open(path+paetec_request+'.csv','r') as csv_file:
        c=csv.reader(csv_file)
        for i,val in enumerate(c):
            if i != 0:
                for num in range(0,len(val)):
                    #print (num)        
                    #print (i,val)
                    ws.Cells(row,col).Value=val[num]
                    col=col+1
            row=row+1
            col=1 
    #This loop for PAETEC RIS sheet
    ws = wb.Worksheets("PAETEC RIS")
    row=1
    col=1
    with open(path+paetec_ris+'.csv','r') as csv_file:
        c=csv.reader(csv_file)
        for i,val in enumerate(c):
            if i != 0:
                for num in range(0,len(val)):
                    #print (num)        
                    #print (i,val)
                    ws.Cells(row,col).Value=val[num]
                    col=col+1
            row=row+1
            col=1
    
    # Go to the calc sheet and update the path
    ws = wb.Worksheets("Calc")
    ws.Cells(5,2).Value = path
    #Now we have done all the neccesarry activity  so call the macro to populate the values in respective fields'
    excel.Application.Run("Macro6")
    time.sleep(1)
    #excel.Application.Run("Macro_cal_save")
    ###############################
    ws = wb.Worksheets("Calc")
    # verication of the metrics count with high level bench mark
    tc_received=ws.Cells(19,2).Value
    tc_resolved_total=ws.Cells(20,2).Value
    tc_resolved_same_day=ws.Cells(21,2).Value
    pae_tc_recieved=ws.Cells(27,2).Value
    pae_resolved=ws.Cells(28,2).Value
    pae_tc_resolved_same_day=ws.Cells(29,2).Value
    # To get the values from Metrics worksheet
    wc = wb.Worksheets("Metrics")
    metrics_row = wc.UsedRange.Rows.Count
    for row in range(1,metrics_row+3):
        if wc.Cells(row,2).Value=='Grand Total':
            metrics=wc.Cells(row,6).Value
    
    #metrics=wc.Cells(24,6).Value
    # To get the values from Metrics - Paetec worksheet
    wc = wb.Worksheets("Metrics - Paetec")
    met_paetec_row = ws.UsedRange.Rows.Count
    for row in range(1,met_paetec_row+3):
        if wc.Cells(row,1).Value=='Grand Total':
            metrics_pae=wc.Cells(row,6).Value 
    
    #metrics_pae=wc.Cells(13,6).Value#ws.Cells(23,lastCol+1).Value
    #lastCol = ws.UsedRange.Columns.Count
    #lastRow = ws.UsedRange.Rows.Count


    ws = wb.Worksheets("Highlevel Bench Mark")
    #updating the Highlevel Bench Mark to calculate the hwin count
    ws.Cells(4,lastCol_new-1).Value=tc_received
    ws.Cells(5,lastCol_new-1).Value=tc_resolved_same_day
    ws.Cells(6,lastCol_new-1).Value=tc_resolved_total-tc_resolved_same_day

    
    

    #To get the values for hwin count
    a=ws.Cells(16,lastCol_new-1).Value
    b=ws.Cells(4,lastCol_new-1).Value
    c=ws.Cells(6,lastCol_new-1).Value
    d=ws.Cells(5,lastCol_new-1).Value
    #Get the values for paetec_metrics
    ws.Cells(22,lastCol_new).Value=pae_tc_recieved
    ws.Cells(23,lastCol_new).Value=pae_tc_resolved_same_day
    ws.Cells(24,lastCol_new).Value=pae_resolved-pae_tc_resolved_same_day
    
    
    
    pa=ws.Cells(26,lastCol_new).Value
    pb=ws.Cells(22,lastCol_new).Value
    pc=ws.Cells(23,lastCol_new).Value
    pd=ws.Cells(24,lastCol_new).Value


    actual_hwin_val=ws.Cells(16,lastCol_new).Value
    actual_hpae_val=ws.Cells(26,lastCol_new).Value
    error=0
    #Checking the count for hwin
    if actual_hwin_val != metrics:
            if a+b-(c+d) < metrics:
                    diff=metrics - actual_hwin_val 
                    correct_c_value=c-diff
                    try:
                        row=2
                        for i in range(0,int(diff)):
                            ws.Cells(6,lastCol_new-row).Value=int(ws.Cells(6,lastCol_new-row).Value-1)
                            row=row+1
                    except Exception as e:
                        error=1
                        print (e)
                        #Need to add the messagebox to show the erorr
                        #--Error would be 'Issue in updating the values in High-Level-Benchmark sheet. So Kindly ReRun '
            else:
                    diff=actual_hwin_val - metrics
                    correct_c_value=c+diff
                    try:
                        row=2
                        for i in range(0,int(diff)):
                            ws.Cells(6,lastCol_new-row).Value=int(ws.Cells(6,lastCol_new-row).Value+1)
                            row=row+1
                    except Exception as e:
                        print (e)
                        error=1
                        #Need to add the messagebox to show the erorr
                        #--Error would be 'Issue in updating the values in High-Level-Benchmark sheet. So Kindly ReRun '
    else:
            insert('All the outputs look good for hwin so updation is not required')

    #Checking the count for paetec
    if actual_hpae_val != metrics_pae:
            if actual_hpae_val < metrics_pae:
                    diff=metrics_pae - actual_hpae_val
                    correct_pd_value=pd-diff
                    try:
                        row=1

                        for i in range(0,int(diff)):
                            ws.Cells(24,lastCol_new-row).Value=int(ws.Cells(24,lastCol_new-row).Value-1)
                            row=row+1
                    except Exception as e:
                        print (e)
                        error=1
                        #Need to add the messagebox to show the erorr
                        #--Error would be 'Issue in updating the values in High-Level-Benchmark sheet. So Kindly ReRun '
            else:
                    diff=actual_hpae_val - metrics_pae
                    correct_pd_value=pd+diff
                    try:
                        row=1
                        for i in range(0,int(diff)):             
                            ws.Cells(24,lastCol_new-row).Value=int(ws.Cells(24,lastCol_new-row).Value+1)
                            row=row+1
                    except Exception as e:
                        print (e)
                        error=1
                        #Need to add the messagebox to show the erorr
                        #--Error would be 'Issue in updating the values in High-Level-Benchmark sheet. So Kindly ReRun '
    else:
            insert ('All the outputs look good for hpae so updation is not required')
    ################
    #To close the opened the file
    excel.Application.Run("Macro_save")
    wb.Close()
    excel.Quit()
    if error==1:
            insert ('Excel manipulation is not completed successfully')
    else:
          insert ('Excel manipulation is completed successfully')
    insert ('Sending Mail....')
    html_ui(path,filename1,filename2)
    insert ('Email sent successfully.')
    prog.grid_forget()
    go.tkraise()
    go.grid(row=4,column=1,sticky="w")
 except Exception as error:
         insert(str(error))
         prog.grid_forget()
         go.tkraise()
         go.grid(row=4,column=1,sticky="w")


def email_thread():
        new=Thread(target=send_mail)
        new.start()

def send_mail():        
        html_ui(ck_folder_entry.get(),file_names[0],file_names[1])
########### To send a mail with an attachement such as Resolution count,Backlog count ########

def html_ui(download_path,filename1,filename2):
 try:
    #email=Button(frame,text='Send Mail',fg='blue',bg="white",command=email_thread)
    #email.grid(row=5,column=1,sticky="w")
    pythoncom.CoInitialize()
    email.grid_forget()
    pbstyle = ttk.Style()
    #print (pbstyle.theme_names())
    pbstyle.theme_use('clam')
    pbstyle.configure("red.Horizontal.TProgressbar", foreground="Green", background="Green")

    var=IntVar()
    prog=ttk.Progressbar(frame,variable=var,
                         orient ="horizontal",
                         length = 100,
                         mode ="determinate",
                         style='red.Horizontal.TProgressbar')
    prog.grid(row=5,column=1,sticky="w")
    prog.start(1000)
    var.set(1)
    prog.configure(maximum=10)
    import pandas_datareader.data as web
    import pandas as pd
    import os
    import win32com.client
    import plotly.graph_objs as go
    import numpy as np
    from numpy.random import randn
    import datetime
    import plotly.io as pio
    #get_ipython().magic(u'matplotlib inline')
    import seaborn as sns
    import matplotlib.pyplot as plt
    from plotly import __version__
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    from plotly.graph_objs import Scatter
    import cufflinks as cf
    init_notebook_mode(connected=True)
    insert('Email is sending....')
    ############## For html_UI ##############################
    #data1=pd.read_csv('C:/Users/balaji.ma/Downloads/Report.csv',encoding = "ISO-8859-1")
    data1=pd.read_csv(os.path.join(download_path,filename1+'.csv'),encoding = "ISO-8859-1")
    df = data1[pd.notnull(data1['Assignee+'])].count()
    df = data1[pd.notnull(data1['Assignee+'])]
    
    prodapt=('Madan Chenchuraju','Mahalakshmi Nagalingam','Sariga Suresh','Gayatheri Manohar','Diwakar Vasu','Santhosh Mahadevan','Balakrishnan Balasubramaniam',
                     'Anitha Thangavel','Jeyalakshmi Sivaselvaraj','Dhilipkumar Gnanasekar','Rajasekar Radhakrishnan','Roshini Beulah',
                     'Kavitha Sekar','Ravindran Naarayanan','Naresh Elango','Pavithra Mathivanan','Mohamed Musthafa Kani','Annamalai Dakshinamurthy','Vijayan Balasubramanian',
                     'Praveena Mohanasundaram','Hemachandran Mohan','Aravindan Sridharan','Suchitra Chandrasekaran','Sudha Ragavan','Gayathri Murthy','Arivanand Murugesan','Jayaprakash Subramanian',
                     'Tim Schnitter','Suresh R A','Arun Kumar','Nithyakamalam Rajkumar','Arunkumar Arjunan')

    mail_html=""
    mail_body_start='<font face="calibri" size="3" >Hi Team,</font><br>' +'<br> <font face="calibri" size="3" >Please find the backlog details in the path provided below and the resolution count attached for your reference. </font><br>'
    svn_link=svn_link='<font face="calibri" size="3" > <br><a href="https://pisvn.prodapt.com/svn/windstream/GROUP-C/ASAP/Maintenance Support/Reports/Daily Backlog tickets Report/{}/{}/"> https://pisvn.prodapt.com/svn/windstream/GROUP-C/ASAP/Maintenance Support/Reports/Daily Backlog tickets Report/{}/{}/</a> </font> <br> <br>'.format(datetime.date.today().strftime("%Y"),datetime.date.today().strftime("%B"),datetime.date.today().strftime("%Y"),datetime.date.today().strftime("%B"))
    pro_head = "<h2>Overall Backlog</h2>"
    mail_html = mail_html+mail_body_start+svn_link+str(pro_head)
    table5_head_mail= "<table border='1' style='border-collapse:collapse;background-color:#4ba1f2;' cellpadding=20 class='table bg-primary '>"
    mail_html = mail_html+str(table5_head_mail)
    a1=(df.loc[(df['Case Type*'] == 'Incident') & df['Assignee+'].isin(prodapt)]).count()
    a2=(df.loc[(df['Case Type*'] == 'Request') & df['Assignee+'].isin(prodapt)]).count()
    a3=(df.loc[(df['Case Type*'] == 'RIS') & df['Assignee+'].isin(prodapt)]).count()


    table5_body1_mail="<tr><th>Incident</th><td>"+str(a1['Assigned Group*+'])+"</td></tr>"


    table5_body1_mail=table5_body1_mail+"<tr><th>Request</th><td>"+str(a2['Assigned Group*+'])+"</td></tr>"

    mail_html = mail_html+"<style='color:Blue'>"+str(table5_body1_mail)


    table5_foot ="</table>"

    mail_html = mail_html+str(table5_foot)
    table6_head_mail= "<table border='1' style='border-collapse:collapse;text-align:left' class='table bg-info' style='border-collapse:collapse;background-color:#79c3e0;' cellpadding=10 >"
    mail_html = mail_html+"<br>"+str(table6_head_mail)

    ba=(df.loc[(df['Assigned Group*+'] == 'IT-OSS - M6 (ASAP/TSG)') & df['Assignee+'].isin(prodapt)]).count()

    bb=(df.loc[(df['Assigned Group*+'] == 'IT-OSS - M6 (NextGen)') & df['Assignee+'].isin(prodapt)]).count()

    bc=(df.loc[(df['Assigned Group*+'] == 'IT-OSS - M6 (PAETEC)') & df['Assignee+'].isin(prodapt)]).count()

    bd=(df.loc[(df['Assigned Group*+'] == 'IT-OSS - M6 (EarthLink)') & df['Assignee+'].isin(prodapt)]).count()

    table6_body1 = "<tr><th>IT-OSS - M6 (ASAP/TSG) </th><td>"+str(ba['Assigned Group*+'])+"</td></tr>"
    table6_body1 = table6_body1+"<tr><th>IT-OSS - M6 (NextGen) </th><td>"+str(bb['Assigned Group*+'])+"</td></tr>"
    table6_body1 = table6_body1+"<tr><th>IT-OSS - M6 (PAETEC) </th><td>"+str(bc['Assigned Group*+'])+"</td></tr>"
    table6_body1 = table6_body1+"<tr><th>IT-OSS - M6 (EarthLink) </th><td>"+str(bd['Assigned Group*+'])+"</td></tr>"
    mail_html = mail_html+"<br>"+str(table6_body1)
    table6_foot ="</table>"
    mail_html = mail_html+str(table6_foot)

    total=ba['Assigned Group*+']+bb['Assigned Group*+']+bc['Assigned Group*+']+bd['Assigned Group*+']-a3['Assigned Group*+']
    table1_mail = "<table class='table bg-success' border='1' style='border-collapse:collapse;background-color:#43f2b2;' cellpadding=20 ><tr><td><b>Total Number of tickets assigned in Prodapt</b></td><td><b>"+str(total)+"</b></td></tr></table>"



    mail_html = mail_html+"<br><br>"+str(table1_mail)

    a1 = pd.crosstab(df['Assignee+'] , df['Status*'])

    b1 = pd.crosstab(df['Assignee+'], df['Case Type*'])

    table4_head = "<table class='table table-striped table-hover'><tr><th>Name &nbsp <input style='width:60%;display:inline-table' type='text' class='form-control' id='search' onkeyup='funWrite(this)' placeholder='search with Assignee name' /></th><th>Assigned</th><th>In Progress</th><th>Pending</th><th>TOTAL</th></tr>"
    j=0;
    for h in a1['Assigned']:
            if a1.index.tolist()[j] in prodapt:
                    table4_body = "<tr class='each_tr' id='tr_"+str(j+1)+"' attr_tr_each='"+str(j+1)+"'><td class='name_td' id='td_"+str(j+1)+"' attr_td='"+str(j+1)+"'>"+str(a1.index.tolist()[j])+"</td><td>"+str(a1['Assigned'][j])+"</td><td>"+str(a1['In Progress'][j])+"</td><td>"+str(a1['Pending'][j])+"</td><td>"+str(a1['Pending'][j]+a1['In Progress'][j]+a1['Assigned'][j])+"</tr>"
                    print(table4_body)
            j=j+1;
    table4_foot = "<table class='table bg-info'>"

    df2 = pd.read_csv(os.path.join(download_path,filename2+'.csv'),encoding = "ISO-8859-1")
    df2['Date']  = df2['Last Resolved Date'].apply(lambda t: pd.to_datetime(t).date())
    df2['DateStr']  = df2['Date'].apply(lambda t: str(t))
    dateArr = df2['DateStr'].unique() 
    dateArr = np.sort(dateArr)
    AssArr = df2['Assignee+'].unique()
    AssArr = np.sort(AssArr)
    df3 = pd.DataFrame(randn(len(dateArr),len(AssArr)),index=dateArr,columns=AssArr)
    for n in AssArr:
	    for k in dateArr:
		    df3[n].loc[k] =df2[(df2['DateStr'] == k) & (df2['Assignee+'] == n)]['Assigned Group*+'].count()

    plt.figure(figsize=(12,3))
    sns.heatmap(data=df3,annot=True)
    plt.savefig("Resolution_count.png",dpi=1000,bbox_inches='tight')

    # ======================== To launch the outlook ===================================
    Application = win32com.client.dynamic.Dispatch('outlook.application')
    print (Application)
    print (Application.Session.Accounts)
    oacctouse= None
    for oacc in Application.Session.Accounts:                    
            if oacc.SmtpAddress == "Balaji.Masilamani@windstream.com" or  oacc.SmtpAddress == "Sariga.Suresh@windstream.com"   or  oacc.SmtpAddress == "Kavitha.Sekar@windstream.com"  or  oacc.SmtpAddress == "Madan.Chenchuraju@windstream.com" or  oacc.SmtpAddress == "Jeyalakshmi.Sivaselvaraj@windstream.com" or  oacc.SmtpAddress == "Santhosh.Mahadevan@windstream.com" or oacc.SmtpAddress == "dev.saravanan@windstream.com":
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
    mail.To ='DL-NG-Support@prodapt.com; DL-Metasolv_Leads@prodapt.com'
    #mail.To='balaji.ma@prodapt.com'        
    mail.Subject = 'Daily Backlog Report'
    mail.Body = 'This Mail is Sent by Python'

    mail.HTMLBody = mail_html+"<br><b><span style='color:gray'>This is an automated e-mail</span></b>"

    mail.Attachments.Add(os.path.join(os.getcwd(),'Resolution_count.png'))
    mail.Send()
    insert('Email Sent Successfully....')
    
    #print("success")
    prog.grid_forget()
    email.tkraise()
    email.grid(row=5,column=1,sticky="w")
 except Exception as error:
    insert(str(error))
    prog.grid_forget()
    email.tkraise()
    email.grid(row=5,column=1,sticky="w")
#html_ui('C:/Users/balaji.ma/Downloads/','Report','qeport')

#===============To get the current file names,date and time=======================

    
print (dict_day)
current_time=datetime.date.today().strftime("%B %dth, %Y")
a=datetime.date.today().strftime("%B")
b=datetime.date.today().strftime("%d")
c=datetime.date.today().strftime("%Y")

def get_day_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix
day=str(b)+str(get_day_suffix(int(b)))

date_and_time=day[0:]+a[0:3]+c[2:4]

if date_and_time[0]=='0':
    dt_time=date_and_time[1:]
else:
    dt_time=date_and_time[0:]
    
month_number=(datetime.date.today()).month
day_number=(datetime.date.today()).day
year_number=(datetime.date.today()).year


current_day_time=datetime.datetime.now()
current_day=current_day_time.strftime("%A")
date_filed=str(month_number)+'-'+str(day_number)+'-'+str(year_number)

for i in range(0,len(file_name)):
    #print (file_name[i]+str(dt_time))
    file_names.append(file_name[i]+str(dt_time))
#print ('####### File_names########')
#print (file_names)


###############Removing the older files ########################
'''
for i in os.listdir(get_download_path()):
    #print ()
    name=str(i)[0:-4]
    if name in file_names:
            #print (name)
            #print (get_download_path()+'\\'+i)
            os.remove(get_download_path()+'\\'+i)
'''
###################################################
next_month=''
current_month=''
respective_year1=''
respective_year2=''
if dict_day:
   if  dict_day[a]== '12':
           current_month=dict_day[a]
           next_month='01'
           respective_year1=c
           respective_year2=int(c)+1
   else:
        current_month=dict_day[a]
        next_month=int(dict_day[a])+1
        respective_year1=c
        respective_year2=c
#print ('The Next month will be ',next_month)
#print ('Respective year will be ',respective_year1)
#print ('Respective year will be ',respective_year2)

    
#================= Root window initialisation=====================================================
root=Tk()
root.title('Backlog Report Generation')
#root.geometry('600*400')
root.config(background="#E0FFFF")
#====================== mouse Hovering class ================================================
class HoverInfo(Menu):
 def __init__(self, parent, text, command=None):
   self._com = command
   Menu.__init__(self,parent, tearoff=0)
   if not isinstance(text, str):
      raise TypeError('Trying to initialise a Hover Menu with a non string type: ' + text.__class__.__name__)
   toktext=re.split('\n', text)
   for t in toktext:
      self.add_command(label = t)
      self._displayed=False
      self.master.bind("<Enter>",self.Display )
      self.master.bind("<Leave>",self.Remove )
 
 def __del__(self):
   self.master.unbind("<Enter>")
   self.master.unbind("<Leave>")
 
 def Display(self,event):
   if not self._displayed:
      self._displayed=True
      self.post(event.x_root, event.y_root)
   if self._com != None:
      self.master.unbind_all("<Return>")
      self.master.bind_all("<Return>", self.Click)
 
 def Remove(self, event):
  if self._displayed:
   self._displayed=False
   self.unpost()
  if self._com != None:
   self.unbind_all("<Return>")
 
 def Click(self, event):
   self._com()
 def close(self,event):
     quit()


db=creating_db()
#=================== Method to get the check out folder ====================================================
def get_chk_folder():
    count=0
    sub_file_count=0
    global a
    global day
    global c
    #download_path=copy_paste.get_download_path()
    #print (download_path)
    pythoncom.CoInitialize()
    if ck_folder_entry.get():
        if not os.path.isdir(ck_folder_entry.get()):
            #MSS - Ticket Backlog Benchmark
            messagebox.showinfo('Error','Given path is not exists in your system ')
        else:
            download_path=copy_paste.get_download_path()
            #============ Transfering files=====================
            insert('Transfering files.....')
            file_count=copy_paste.move_file(download_path,ck_folder_entry.get(),dt_time)
            if file_count > 0:
                    insert(str(file_count)+ ' has been transfered')
            else:
                insert ('Files are not available in the download path.please move the files to thr download folder')
            for i in os.listdir(ck_folder_entry.get()):
                if 'MSS - Ticket Backlog Benchmark' in i:
                    count=1
                    file_name=i                    
                    path=ck_folder_entry.get()
                    insert('Starting the Excel Manipulation')
                    start_excel(path,file_name,
                    file_names[5],
                    file_names[6],
                    current_day,
                    date_filed,
                    file_names[0],
                    file_names[1]                
                    )
                if dt_time in i:
                    sub_file_count=sub_file_count+1
                   
            if  count==0 :
                    messagebox.showinfo('Error','Base file is not exists in the specified path')
    else:
        messagebox.showinfo('Error','Path Can not be Empty ')
    
    
    
    
    
    #for i in os.listdir(ck_folder_entry.get()):
        #if '16th' in i:
            #print (os.path.join(ck_folder_entry.get(),i))

#======================= change the window to the center  ===============================================       
def center_window(width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

#================== Method to insert the data into the data base ====================================================
def insert_yes_no():
    global entry
    if entry.get():
        result=messagebox.askquestion("Insert", "Are You Sure want to insert?")
        if result=='yes':
            db.insert(entry.get())
            insert ('Name '+entry.get()+' is added to Database')            
        else:
            pass
    else:
        messagebox.showinfo('Error','Can not insert NULL value')
        insert ('Trying to insert the NULL value,Please enter the Valid name')

#================== Method to delete the data into the data base ====================================================
def delete_yes_no():
    global delete_entry
    if delete_entry.get():
        result=messagebox.askquestion("Delete", "Are You Sure want to Delete?")
        if result=='yes':
             db.delete(delete_entry.get())
             insert ('Name '+entry.get()+' is deleted from Database')
        else:
            pass
    else:
        messagebox.showinfo('Error','Can not delete the NULL value')
        insert ('Trying to delete the NULL value,Please enter the Valid name')
#=========================== To destroy the addname window ==========================================
def insert_Quit():    
    global window
    window.withdraw()
#========================= To destroy the delete name window=============================================
def delete_Quit():
    global delete_window
    delete_window.withdraw()
#=========================== Mehtod to create the Add name window ==========================================
def add_name():
    global entry
    global window
    window = Toplevel(root)
    window.title('Add New name')
    name=Label(window,text='Name')
    name.grid(column=0,row=0)
    entry=Entry(window,bd=2)
    entry.grid(column=1,row=0)
    ok=Button(window,text='Ok',command=insert_yes_no)
    ok.grid(column=1,row=1)
    cancel=Button(window,text='Cancel',fg='blue',command=insert_Quit)
    cancel.grid(column=2,row=1)
#===================== Mehtod to create the Delete name window =================================================   
def delete_name():
    global delete_entry
    global delete_window
    delete_window = Toplevel(root)
    delete_window.title('Delete name')
    delete_name=Label(delete_window,text='Name')
    delete_name.grid(column=0,row=0)
    delete_entry=Entry(delete_window,bd=2)
    delete_entry.grid(column=1,row=0)
    delete_ok=Button(delete_window,text='Ok',command=delete_yes_no)
    delete_ok.grid(column=1,row=1)
    delete_cancel=Button(delete_window,text='Cancel',fg='blue',command=delete_Quit)
    delete_cancel.grid(column=2,row=1)
#========================== Metod for excel manipulation ============================================   
def excel_thread():
        s=Thread(target=excel_manipulation)
        s.start()

def excel_manipulation():
    get_chk_folder()
    #creating_db.Paetec_Closed_query()
    #creating_db.paetec_request_query()
    #creating_db.paetec_ris_query()
#====================== Method to download the files ================================================
def start_thread():
        #print (name)
        t = Thread(target=download_files)
        t.start()
def insert(string):
            text.insert(INSERT,string+'.'+'\n')
            text.insert(INSERT,'---------------------'+'\n')
def download_files():
    global next_month
    global respective_year1
    global respective_year2
    global current_month
    insert('Calling the method to download the files'+'\n')
    open_ticket=''' ('Assigned Group*+' = "IT-OSS - M6 (ASAP/TSG)") AND ('Case Type*' = "Incident") AND (NOT('Status*' = "Resolved" OR 'Status*' = "Closed" OR 'Status*' = "Cancelled")) '''
    closed_ticket='''('Assigned Group*+' = "IT-OSS - M6 (ASAP/TSG)") AND ('Case Type*' = "Incident") AND (('Last Resolved Date' >= "'''+str(current_month)+'/01/'+str(respective_year1)+'''" AND 'Last Resolved Date' < "'''+str(next_month)+'/01/'+str(respective_year2)+'"))'
    Request_Open='''('Assigned Group*+' = "IT-OSS - M6 (ASAP/TSG)") AND ('Case Type*' = "Request") AND (NOT('Status*' = "Resolved" OR 'Status*' = "Closed" OR 'Status*' = "Cancelled"))'''
    db=creating_db()
    paetec_open=db.Paetec_open_query()
    paetec_closed=db.Paetec_Closed_query(current_month,next_month,respective_year1,respective_year2)
    paetec_request=db.paetec_request_query()
    paetec_ris=db.paetec_ris_query()
    resolution=db.resolution_count()
    #########################################
    from datetime import date,timedelta,datetime
    Today=date.today()
    yesterday= date.today() - timedelta(1)
    day=Today.strftime('%A')
    if day=='Monday':
            def get_last_friday():
                now = datetime.now()
                closest_friday = now + timedelta(days=(4 - now.weekday()))
                if closest_friday < now:
                     return closest_friday
                else:
                    return (closest_friday - timedelta(days=7))
    
            last_friday=str(get_last_friday())
            replaced_string=last_friday[0:10]
            year=replaced_string[2:4]
            month=replaced_string[5:7]
            day=replaced_string[8:]
            yesterday=month+'/'+day+'/'+year
    else:
            yesterday=str(yesterday.strftime('%m/%d/%y'))
    graph=''' (('Assigned Group*+' = "IT-OSS - M6 (NextGen)") OR ('Assigned Group*+' = "IT-OSS - M6 (ASAP/TSG)" ) OR ('Assigned Group*+' = "IT-OSS - M6 (PAETEC)")OR ('Assigned Group*+' = "IT-OSS - M6 (EarthLink)")) AND ('Case Type*' = "Incident") AND ('Status*' = "Resolved") AND ('Assignee+' = "Jeyalakshmi Sivaselvaraj" OR 'Assignee+' = "Madan Chenchuraju" OR 'Assignee+' = "Mahalakshmi Nagalingam" OR 'Assignee+' = "Sariga Suresh" OR 'Assignee+' = "Gayatheri Manohar" OR'Assignee+' = "Diwakar Vasu" OR 'Assignee+' = "Santhosh Mahadevan" OR 'Assignee+' = "Balakrishnan Balasubramaniam" OR 'Assignee+' = "Anitha Thangavel" OR 'Assignee+' = "Dhilipkumar Gnanasekar" OR 'Assignee+' = "Rajasekar Radhakrishnan" OR 'Assignee+' = "Roshini Beulah" OR 'Assignee+' = "Kavitha Sekar" OR 'Assignee+' = "Ravindran Naarayanan" OR 'Assignee+' = "Naresh Elango" OR 'Assignee+' = "Pavithra Mathivanan" OR 'Assignee+' = "Mohamed Musthafa Kani" OR 'Assignee+' = "Annamalai Dakshinamurthy" OR 'Assignee+' = "Vijayan Balasubramanian" OR 'Assignee+' = "Praveena Mohanasundaram" OR 'Assignee+' = "Hemachandran Mohan" OR 'Assignee+' = "Aravindan Sridharan" OR 'Assignee+' = "Suchitra Chandrasekaran" OR 'Assignee+' = "Sudha Ragavan" OR 'Assignee+' = "Gayathri Murthy" OR 'Assignee+' = "Arivanand Murugesan" OR 'Assignee+' = "Jayaprakash Subramanian" OR 'Assignee+' = "Tim Schnitter" OR 'Assignee+' = "Suresh R A" OR 'Assignee+' = "Arun Kumar" OR 'Assignee+' = "Arunkumar Arjunan" OR 'Assignee+' = "Nithyakamalam Rajkumar") AND ('Last Resolved Date' > '''+'"'+yesterday+'"'+''') AND ('Last Resolved Date' < '''+'"'+Today.strftime('%m/%d/%y')+'"'+')'
    ####################################
    query = [
        resolution,
        graph,
        open_ticket,
        closed_ticket,
        Request_Open,
        paetec_open,
        paetec_closed,
        paetec_request,
        paetec_ris
        ]
    insert('Start downloading...')
    download_file(query,file_names)
    

#=====================Method for place holder=================================================
def on_entry_click(event):
    if ck_folder_entry.get() == ':Specify the chekout folder':
       ck_folder_entry.delete(0, "end") # delete all the text in the entry
       ck_folder_entry.insert(0, '')
       ck_folder_entry.configure(fg='black')
#======================== Method for place holder==============================================
def on_focusin(event):
    ck_folder_entry.delete(0, "end")
    ck_folder_entry.config(fg='black')
#========================== Method for place holder============================================
def on_focusout(event):
    if ck_folder_entry.get() == '':
        ck_folder_entry.insert(0, ":Specify the chekout folder")

#==================== Labels and buttons for the main window ===============================================

center_window(400, 400)
root.resizable(0, 0)   
frame=LabelFrame(root,
                 #highlightthickness=3,
                 #highlightcolor="blue",
                 #highlightbackground="blue",
                 bd= 10
                 )
frame.grid(row=0,column=0,sticky="ew")
ck_folder_label=Label(frame,text='Speify the path/Location', bg="white")

ck_folder_label.grid(row=2, column=0,sticky="w",padx=10,pady=4)

ck_folder_entry=Entry(frame,)
ck_folder_entry.grid(row=2, column=1,sticky="w")
ck_folder_entry.insert(0,":Specify the Local folder location where you want to run the operation ")
#ck_folder_entry.bind('<Key>', on_entry_click)
ck_folder_entry.bind('<FocusIn>', on_focusin)
ck_folder_entry.bind('<FocusOut>', on_focusout)

a=Label(frame,text='Download all the CSV files using selenium',bg="white")
a.grid(row=3, column=0,sticky="w",padx=10)
files_donload=Button(frame,text='Download',fg='blue',
                     command=start_thread
                     )
files_donload.grid(row=3,column=1,sticky="w")
#HoverInfo(files_donload,'Download all the necessary reports using selenium')

b=Label(frame,text='Manipulate the Excel Sheet',bg="white")
b.grid(row=4, column=0,sticky="w",padx=10)
go=Button(frame,text='Excel Manipulation',fg='blue',bg="white",command=excel_thread)
go.grid(row=4,column=1,sticky="w")
#HoverInfo(go,'Run the excel Manipulation')

b=Label(frame,text='Overall backlog and resolution count',bg="white")
b.grid(row=5, column=0,sticky="w",padx=10)
email=Button(frame,text='Send Mail',fg='blue',bg="white",command=email_thread)
email.grid(row=5,column=1,sticky="w")

c=Label(frame,text='If you want to add new employee name',bg="white")
c.grid(row=6, column=0,sticky="w",padx=10)

Add_name=Button(frame,text='Add Name',fg='blue',bg="white",command=add_name)
Add_name.grid(row=6,column=1,sticky="w")
#HoverInfo(Add_name,'if you want we can add new employee name in the database ')

d=Label(frame,text='if you want to delete the employee name',bg="white")
d.grid(row=7, column=0,sticky="w",padx=10)
delete_name=Button(frame,text='Delete Name',fg='blue',bg="white",command=delete_name)
delete_name.grid(row=7, column=1,sticky="w")
#HoverInfo(delete_name,'if u want we can delete employee name from the database ')

frame1=LabelFrame(root,
                  padx=5, pady=5,text='Log',
                  #highlightthickness=3,
                  #highlightcolor="red",
                  #highlightbackground="red",
                  bd=10
                  )
frame1.grid(row=7,column=0)
text=tkscrolled.ScrolledText(frame1,bg="white",height=12,width=40)
text.grid(row=8, column=0,columnspan=2,padx=10)
root.mainloop()

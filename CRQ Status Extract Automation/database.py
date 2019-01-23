import sqlite3
import xlrd as xl
import xlwt as xw
conn=sqlite3.connect('crq_status_database.db')

cur=conn.cursor()

op=cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='crq_status'")
print (op)
for i,data in enumerate(op.fetchall()):
    print (i)
    print (data)
    if data[0]==1:
        print ('Table Alreay exists with some data')
        #op1=cur.execute("SELECT * from crq_status")       
        #for i1,data1 in enumerate(op1.fetchall()):
        #print (data1)
    else:
       cur.execute("""Create table if not exists crq_status (crq_number varchar2(50),
                                        Owner  varchar2(50),
                                        crq_status varchar2(50),
                                        task_status  varchar2(30),
                                        Approver_Group_Name varchar2(50),
                                        Approvers_Name varchar2(200),
                                        Approver_Sign varchar2(50),
                                        Approver_Alternate varchar2(50),
                                        Approval_date date)
                                       """)
       conn.commit()

#Checking the data exists or not
try:
   op1=cur.execute("SELECT count(*) from crq_status")       
   for i1,data1 in enumerate(op1.fetchall()):
      if int(data1[0])>1:
         print ('Data alreay exists and need to delete')
         cur.execute('DELETE FROM crq_status')
         conn.commit()
except Exception as e:
   print (e)
      
op2=cur.execute("SELECT count(*) from crq_status")
for i1,data1 in enumerate(op2.fetchall()):
   print (data1)



workbook=xl.open_workbook('CRQ Status.xls')
sheet=workbook.sheet_by_index(0)
total_rows=sheet.nrows
total_cols=sheet.ncols

for row in range(1,total_rows):
         for col in range(0,total_cols):
            if col==0:
               crq_number=sheet.cell_value(row,col)
               #print (crq_number)
            if col==1:
               Owner=sheet.cell_value(row,col)
               #print (Owner)
            if col==2:
               crq_status=sheet.cell_value(row,col)
               #print (crq_status)
            if col==3:
               task_status=sheet.cell_value(row,col)
               #print (task_status)
            if col==4:
               Approver_Group_Name=sheet.cell_value(row,col)
               #print (Approver_Group_Name)
            if col==5:
               Approvers_Name=sheet.cell_value(row,col)
               #print (Approvers_Name)
            if col==6:
               Approver_Sign=sheet.cell_value(row,col)
               #print (Approver_Sign)
            if col==7:
               Approver_Alternate=sheet.cell_value(row,col)
               #print (Approver_Alternate)
            if col==8:
               Approval_date=sheet.cell_value(row,col)
               #print (Approval_date)
         #cur.execute('insert into crq_status values ('+crq_number+','+Owner+','+crq_status+','+task_status+','+Approver_Group_Name+','+Approvers_Name+','+Approver_Sign+','+Approver_Alternate+','+Approval_date+')')
         cur.execute('insert into crq_status values (?,?,?,?,?,?,?,?,?)',(crq_number,Owner,crq_status,task_status,Approver_Group_Name,Approvers_Name,Approver_Sign,Approver_Alternate,Approval_date,))
         conn.commit()
               
              
columns=['CRQ Number','Owner','CRQ Status','Task Status','Approver Group Name','Approvers Name','Approver Sign','Approver Alternate','Approval date']
style = xw.easyxf('pattern: pattern solid, fore_colour light_blue;'
                              'font: colour white, bold True;'
                    'borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thick, bottom thin;')
new_file_name='crq_status_new.xls'
wb = xw.Workbook()
ws = wb.add_sheet('Crq_status_new',cell_overwrite_ok=True)
column=0
for i in columns:
   ws.write(0,column,i,style)
   column+=1
ws.col(0).width =256 * 20
ws.col(1).width =256 * 35
ws.col(2).width =256 * 30
ws.col(3).width =256 * 15
ws.col(4).width =256 * 20
ws.col(5).width =256 * 70
ws.col(6).width =256 * 70
ws.col(7).width =256 * 70
ws.col(8).width =256 * 70

#cur.execute("""insert into crq_status values ('CRQ000000118910','Annamalai Dakshinamurthy','Scheduled For Approval','Pending', 'Change Management','Michael A Patty;Jyotsna Koganti;William Masi;Amrita Newaskar',null,null,null)""")	
#cur.execute("""insert into crq_status values ('CRQ000000118910','Annamalai Dakshinamurthy','Scheduled For Approval','Approved','IT - Command Center','Marc Holtz;Steven Werner;Ranjitha Umapathy;Nandhini Arumugam;Anandavel Ramu;Abilash Sugavanam;Navinraj R;Janarthanan Vt;Pavithra Srinivasan;Suresh Vasudevan;Naresh Arumugam;Renukadevi V;Praveena Puttum;Sudheer K Kosgi;Mohamed Sarjoon;Adhavan Arumughaperumal;Vikas Govindraj;Mithra S Devi;Rajesh Loganathan;John F Morrissey;Hamkumar Sampath','Marc Holtz','Felix Liverman','10/9/2018 10:23:50 AM')""")	
#cur.execute("""insert into crq_status values ('CRQ000000118910','Annamalai Dakshinamurthy','Scheduled For Approval','Approved','IT-OSS - M6 (NextGen)','Michael J Sheriff;Chawn S Thompson;Bryan K Lewis;Deborah Philps;Dirk L Fox;Suriya S Kanthan',	'Michael J Sheriff',null,'10/9/2018 2:54:06 PM')""")	
#cur.execute("""insert into crq_status values ('CRQ000000118910','Annamalai Dakshinamurthy','Scheduled For Approval','Approved','DBA: Core','Timothy Brotzman;Jonathan D Mazak;Louis G Slavik;Harikrishna Rao;Joseph B Robinson Iii;Donna Menyes;Anand Buldeo',	'Anand Buldeo',null,'10/9/2018 2:19:12 PM')""")	
#cur.execute("""insert into crq_status values ('CRQ000000118809','Annamalai Dakshinamurthy','Scheduled For Approval','Pending', 'Change Management','Michael A Patty;Jyotsna Koganti;William Masi;Amrita Newaskar',null,null,null)""")				
#cur.execute("""insert into crq_status values ('CRQ000000118809','Annamalai Dakshinamurthy','Scheduled For Approval','Approved','IT - Command Center','Marc Holtz;Steven Werner;Ranjitha Umapathy;Nandhini Arumugam;Anandavel Ramu;Abilash Sugavanam;Navinraj R;Janarthanan Vt;Pavithra Srinivasan;Suresh Vasudevan;Naresh Arumugam;Renukadevi V;Praveena Puttum;Sudheer K Kosgi;Mohamed Sarjoon;Adhavan Arumughaperumal;Vikas Govindraj;Mithra S Devi;Rajesh Loganathan;John F Morrissey;Hamkumar Sampath'	,'Marc Holtz'	,'Felix Liverman'	,'10/9/2018 10:23:01 AM')""")	
#cur.execute("""insert into crq_status values ('CRQ000000118809','Annamalai Dakshinamurthy','Scheduled For Approval','Approved','IT-OSS - M6 (NextGen)','Michael J Sheriff;Chawn S Thompson;Bryan K Lewis;Deborah Philps;Dirk L Fox;Suriya S Kanthan','Michael J Sheriff'		,null,'10/9/2018 2:53:48 PM')""")	
#cur.execute("""insert into crq_status values ('CRQ000000118809','Annamalai Dakshinamurthy','Scheduled For Approval','Approved','DBA: Core','Timothy Brotzman;Jonathan D Mazak;Louis G Slavik;Harikrishna Rao;Joseph B Robinson Iii;Donna Menyes;Anand Buldeo',	'Anand Buldeo',null,		'10/9/2018 2:21:44 PM')""")	

#cur.execute('delete from crq_status ')
#conn.commit()




#To get the total number of task for the each CRQ
output=cur.execute("""select  crq_number,count(*) from crq_status   group by crq_number """)
row=1
for crq_num,count in output.fetchall():
   # if the CRQ has more than one task this block will execute
   if count>1:
      #To get the count of Approver_Group_Name
      output1=cur.execute('select  Approver_Group_Name,count(*) from crq_status where crq_number=? group by Approver_Group_Name ',(crq_num,))
      for Approver_Group_Name,count1 in output1.fetchall():
         #if the Approver_Group_Name duplicates this block will execute
         if count1>1:
            #To get the distinct task status of the Approver_Group_Name
            output2=cur.execute('select  count(distinct(task_status)) from crq_status where crq_number=? and Approver_Group_Name=?',(crq_num,Approver_Group_Name,))
            for distinct_count in output2.fetchall():
               #If the  distinct task status is equal to 1
               if distinct_count[0]==1:
                  output3=cur.execute('select  * from crq_status where crq_number=? and Approver_Group_Name=? and Approval_date=(select max(Approval_date) from crq_status where crq_number=? and Approver_Group_Name=? )',(crq_num,Approver_Group_Name,crq_num,Approver_Group_Name))
                  for data in output3.fetchall():
                     #print ('For same task_status')
                     #print (data)
                     #print (len(data))
                     for col in range(0,len(data)):
                        ws.write(row,col,str(data[col]))
                     row=row+1
               #If the  distinct task status greater than 1
               if distinct_count[0]>1:
                  output4=cur.execute("select  * from crq_status where crq_number=? and Approver_Group_Name=?  and Approval_date=''",(crq_num,Approver_Group_Name,))
                  #print ('Finding Pending status')
                  for data in output4.fetchall():
                     #print ('For different task_status')
                     #print (data)
                     for col in range(0,len(data)):
                        ws.write(row,col,str(data[col]))
                     row=row+1
         if count1==1:
            #If te count1 ==1 then it has only one 
            output5=cur.execute('select * from crq_status where crq_number=? and Approver_Group_Name=?',(crq_num,Approver_Group_Name))
            for data in output5.fetchall():
               #print ('No duplicate exists ')
               #print (data)
               for col in range(0,len(data)):
                     ws.write(row,col,str(data[col]))
               row=row+1
               
   print ('################################################################')
   if count==1:
      output6=cur.execute('select  * from crq_status where crq_number=? group by Approver_Group_Name ',(crq_num,))
      for data in output6.fetchall():
         #print ('It consists of only one entry')
         #print (data)
         for col in range(0,len(data)):
               ws.write(row,col,str(data[col]))
         row=row+1
wb.save(new_file_name)

import re
body="""
19 Dec, 2018 
	
 <http://fapp1.olacabs.com/rdz?id=24897=dUsCVQEMCFsFTgIJAgIHBwJWVR4=VFIPUwxdT18CcxIQWVNTFUcWUw1fTgMMBgcGAgVeVVsBBVAGVANS&fl=XkNGFUACH01FRUUXXV5WVFMEFkxVXA4=> 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
₹267 	
	
   CRN2588482943   
	
Thanks for travelling with us, Balaji (Prodapt Solutions Private Limited) 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
Ride Details 	
 <http://maps.googleapis.com/maps/api/staticmap?size=298x298&maptype=roadmap&markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FStart2x.png%7C12.968266600000%2C80.249981800000&markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FEnd2x.png%7C12.911145000000%2C80.194156400000&path=weight%3A5%7Ccolor%3A0x4379ai9%7Cenc%3AuzcnAkyxhNbHzJzo%40rTrO%7EDv%5EjL%7Eg%40hQ%60%5BdOpa%40rOdw%40vM%7Cy%40%7CFpp%40bF%60m%40zBk%40l  c%40yB%7C%5CqQpo%40_Kh%5BaEpa%40gTzSQpK&client=gme-anitechnologiespvt&channel=mirage&signature=r-oHRDKcTiq0TvfrYO_2v9tVeg8%3D> 	
 <http://s3-ap-southeast-1.amazonaws.com/ola-ims-drivers/production/drivers/19638155/thumb_1510817833977.jpeg> 	Selvam NA 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_Prime_Play_Icon> 	Prime Play - White Swift Dzire 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
11:27 PM <javascript:void(0)>  	 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_src_dest> 	Prince Info City II, Perungudi Chennai Tamil Nadu India 	
11:45 PM <javascript: void(0)>  	3, Medavakkam, Chennai 	
Bill Details	 
Your Trip 	
₹222.61 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
Play Convenience Fee (8%) 	
₹17.72 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
Toll/Parking Fee 	
₹27 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
Total Bill (rounded off) 	
₹267 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
Click here <http://fapp1.olacabs.com/rdz?id=24897=dUsCVQEMCFsFTgIJAgIHBwJWVR4=VFIPUwxdT18CcxIQWVNTFUcWUw1fTgMMBgcGAgVeVVsBBVAGVANS&fl=XkNGFUACH01aV15JHF1bVlEHBxEYUAxfSUcUQhNcEBYZBQddCwwIUAsGARZWQFJHXRQRTQQDVgNUBlEAUg==>  to get a copy of your invoice.
Have queries? Visit support for this ride. <http://fapp1.olacabs.com/rdz?id=24897=dUsCVQEMCFsFTgIJAgIHBwJWVR4=VFIPUwxdT18CcxIQWVNTFUcWUw1fTgMMBgcGAgVeVVsBBVAGVANS&fl=XkNGFUACH01aV15JHF1bVlEHBxEYUAxfSUcUQhNcEBYZVkIVHFRRF1xRWg==&ext=dXRtX3NvdXJjZT1pbnZvaWNlJmxhbmRpbmdfcGFnZT1iZGV0YWlscyZjYXRlZ29yeT1wcmltZV9wbGF5JmJvb2tpbmdfcmVmX25vPTI1ODg0ODI5NDM=>  	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
We've fulfilled our promise to take you to destination for pre-agreed Total Fare. Modifying the drop/route can change this fare. 	
Payment 	
.	 
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_corporate_wallet> 	Paid by Corporate Wallet 	
₹267 	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
For T&C and fare details, visit our website <http://fapp1.olacabs.com/rdz?id=24897=dUsCVQEMCFsFTgIJAgIHBwJWVR4=VFIPUwxdT18CcxIQWVNTFUcWUw1fTgMMBgcGAgVeVVsBBVAGVANS&fl=XkNGFUACH01FRUUXXV5WVFMEFkxVXA4dAFUTVxAcIQpTWVwEWg==>  	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
Didn't make this booking? Report it <http://fapp1.olacabs.com/rdz?id=24897=dUsCVQEMCFsFTgIJAgIHBwJWVR4=VFIPUwxdT18CcxIQWVNTFUcWUw1fTgMMBgcGAgVeVVsBBVAGVANS&fl=XkNGFUACH01FRUUXXV5WVFMEFkxVXA4dB0EVWkxBBxJZRUY6UlpFEVc=&ext=a2V5PVByb1pzaSUyQnhVU1Z2UEJBdzJyTmNlMVlYV3BnMHBuJTJGWlJFQXpBWWoyNXhzM2NDcjB4cjFGRWFRYk4wV0xhMEsy>  	
 <http://d2xfkvgwru9u2c.cloudfront.net/Invoice_White_line> 	
 <http://fapp1.olacabs.com/rdz?id=24897=dUsCVQEMCFsFTgIJAgIHBwJWVR4=VFIPUwxdT18CcxIQWVNTFUcWUw1fTgMMBgcGAgVeVVsBBVAGVANS&fl=XkNGFUACH01FRUUXXV5WVFMEFkxVXA4dCVgAYQZfBwFCGA==&ext=dXRtX3NvdXJjZT1pbnZvaWNlX21haWxlcg==> 

 


 <http://fapp1.olacabs.com/rdz?id=24897=eUsCVQEMCFsFTgIJAgIHBwJWVR4=VFIPUwxdT18CcxIQWVNTFUcWUw1fTgMMBgcGAgVeVVsBBVAGVANS> 
###Removing html content####
-1
-1
"""


replaced=''
start=re.finditer('<',body)
#print(len(start))
start_dict={}
for i,data in enumerate(start):
    start_dict[i]=data.start()

#print ('############################')
#print (start_dict)
end=re.finditer('>',body)
end_dict={}
for i,data in enumerate(end):
    end_dict[i]=data.end()
#print (end_dict)

#body[start_dict[0]:end_dict[0]]=''
#print (body.replace(body[start_dict[0]:end_dict[0]],''))
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
    count=0
    matched=re.match('(^\d{2}:\d{2} [A-Z][A-Z])',text)
    if matched:
            travel_time=matched.group()
            if (travel_time in text) and (count==0):
                am_index=text.index(travel_time)
                #print (text[am_index+8:].strip())
                Address_list.append([travel_time,text[am_index+8:].strip()])
                #ticket_info['ADDR1']=text[am_index+8:].strip()
                
#print (Address_list)

for num,data in enumerate(Address_list):
    if num==0:
        ticket_info['CRN']=data
    if num==1:
        ticket_info['Pick up Time']=data[0]
        ticket_info['Pick up Location']=data[1]
    if num==2:
        ticket_info['Drop Time']=data[0]
        ticket_info['Drop Location']=data[1]
#print (ticket_info)

ticket_summary1='I have booked OLA cab on ' +str(ticket_info['Date'])
ticket_summary2='CRN Reference: '+str(ticket_info['CRN'])
ticket_summary3='Pick up Time: '+ticket_info['Pick up Time']
ticket_summary4='Pick up Location: '+ticket_info['Pick up Location']
ticket_summary5='Drop Time: '+ticket_info['Drop Time']
ticket_summary6='Drop Location: '+ticket_info['Drop Location']

summ=ticket_summary1+'\n'+ticket_summary2+'\n'+ticket_summary3+'\n'+ticket_summary4+'\n'+ticket_summary5+'\n'+ticket_summary6

print (summ)


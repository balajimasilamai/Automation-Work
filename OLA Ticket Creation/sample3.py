import win32com.client
import re
i=0
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
messages = inbox.Items
#print ('#############messages############')
#print (str(messages))



for m in messages:
    matched_sub=re.match("(?P<first>\w+)\W+(?P<second>\w+)\W+(?P<third>\w+)", m.subject)
    if matched_sub:
     if matched_sub.group(1)=='Your' and matched_sub.group(3)== 'ride':
        print ('subject identified')

        if m.UnRead == True and matched_sub.group(1)=='Your' and matched_sub.group(3)== 'ride':
            #message = messages.GetFirst()
            body_content = m.body
            sender=m.sender
            #print ('Sender :'+str(sender)+'  '+'Body :'+ str(body_content))
            print ('########body_content###########')
            content=str(body_content)
            print (content)

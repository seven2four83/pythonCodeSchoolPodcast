emails = []
try:
    email_file = open('emails.txt','r')
    for emailId in email_file:
        emails.append(emailId.strip())
    print(emails)
except FileNotFoundError as err:
    print(err)   

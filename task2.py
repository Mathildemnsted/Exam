import re 

validEmail = re.compile("[a-z][a-z]*[@](hr)?(it)?(fin)?(mkt)?(ops)?\.company\.com")

email = input("Write email\n")

def validate_email(email):
   if validEmail.match(email):
      print("The email is valid.")
      return True
   else:
      print("The email is invalid.") 
      return False 
   

def get_department(email): 
   if validate_email(email) == False: 
      return None
   else: 
        if re.search('hr', email):
            department = "Human Resources"
        elif re.search('it', email):
           department = "Information technology"
        elif re.search('fin', email):
           department = "Finance"
        elif re.search('mkt', email):
           department = "Marketing"
        else:
           department = "Operations"
        return department

print(f"The department is: {get_department(email)}")


email_list = ['abbb@fin.company.com', 'accc@fin.company.com', 'baaa@mkt.company.com', 'dkjkj@mkt.company.com', 'dlll@ops.company.com', 'hjjj@hr.company.com', 'jjjss@it.company.com', 'dklj@ops.company.com']

def categorize_emails(email_list):
    allEmails = {'hr': [], 'it': [], 'fin': [], 'mkt': [], 'ops': []}
    for email in email_list:
        if validate_email(email) == True: #this will print if each email is valid (since the print statement was part of the first task), here it it used to make sure that all emails appended to the list are actually valid. 
            if re.search('hr', email):
                allEmails['hr'].append(email)
            elif re.search('it', email):
                allEmails['it'].append(email)
            elif re.search('fin', email):
                allEmails['fin'].append(email)
            elif re.search('mkt', email):
                allEmails['mkt'].append(email)
            elif re.search('ops', email):
                allEmails['ops'].append(email)
    return allEmails

print(f"All emails:\n{categorize_emails(email_list)}")
   

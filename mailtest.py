
# Import smtplib to provide email functions
import smtplib
 
# Import the email modules
from email.mime.text import MIMEText
 
# Define email addresses to use
addr_to   = 'stevegale54@gmail.com'
addr_from = 'steven.gale1@ntlworld.com'
print("set up server") 
# Define SMTP email server details
smtp_server = 'smtp.ntlworld.com'
smtp_user   = 'steven.gale1@ntlworld.com'
smtp_pass   = 'Blue2army'
print("set up msg") 
# Construct email
msg = MIMEText('This is a test email')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Test Email From RPi'
 
print("send the message via an SMTP server")
s = smtplib.SMTP(smtp_server)
s.login(smtp_user,smtp_pass)
s.sendmail(addr_from, addr_to, msg.as_string())
s.quit()
print("bye")

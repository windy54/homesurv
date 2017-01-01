# import the necessary packages
# Import smtplib to provide email functions
import smtplib
 
# Import the email modules
from email.mime.text import MIMEText
 
class HomeSurvEmail:
	def __init__(self):
		self.addr_from = 'steven.gale1@ntlworld.com'
		self.addr_to = 'stevegale54@gmail.com'
		# construct the file path
		self.msg = MIMEText('This is a test email')
		self.msg['To'] = self.addr_to
		self.msg['From'] = self.addr_from
		# Define SMTP email server details
		self.smtp_server = 'smtp.ntlworld.com'
		self.smtp_user   = self.addr_from
		self.smtp_pass   = 'abcdefgh'
 
	def sendEmail(self):
		s = smtplib.SMTP(self.smtp_server)
		s.login(self.smtp_user,self.smtp_pass)
		s.sendmail(self.addr_from, self.addr_to, self.msg.as_string())
		s.quit()

	def cleanup(self):
		# remove the file
		os.remove(self.path)



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

senderacc="sender@gmail.com"  #Change it to your email id
senderpass="app-password" #Change it to the generated app password
server='smtp.gmail.com'
port=587

def sendEmail(subject, text, receiver):
	s = smtplib.SMTP(server,port)
	s.starttls()
	s.login(senderacc, senderpass)
	message = f"Subject:{subject}\n\n{text}"
	s.sendmail(senderacc, receiver, message)
	s.quit()

if __name__=='__main__':
	subject='Test email'
	text='Hello world test'
	receiver='recipient@gmail.com'  #Change it to whom you want to send it to
	sendEmail(subject,text,receiver)


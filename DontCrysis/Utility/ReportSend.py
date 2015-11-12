__author__ = 'Madhavan'

#the following lines are the imports of the functions
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
import email.mime.application



#def main():
    #message = "Success: This is a test Post from Thunder Groudon"
    #GmailAPI('Test Email',message,'madhavan001@e.ntu.edu.sg')
    #FacebookAPI(message)

def GmailAPI(subject, message, receiver):
    #msg =  MIMEText(message)
    msg = MIMEMultipart()
    msg['From'] = 'cms.dontcrysis@gmail.com'
    msg['To'] = receiver;
    msg['Subject'] = subject
    msg.attach( MIMEText(message) )
    mailserver = smtplib.SMTP('smtp.gmail.com',587)

    # identify ourselves to smtp gmail client
    mailserver.ehlo()

    # secure our email with tls encryption
    mailserver.starttls()

    #attach the report file which is in the same directory
    filename='crisis_report.pdf'
    fp=open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('cms.dontcrysis@gmail.com', 'dontcrysis')
    mailserver.sendmail('cms.dontcrysis@gmail.com',receiver,msg.as_string())
    mailserver.quit()
    return

#if __name__ == "__main__":
  #main()
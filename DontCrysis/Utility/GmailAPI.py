from FacebookAPI import FacebookAPI
import smtplib

from email.mime.text import MIMEText

__author__ = 'Madhavan'

#def main():
#    message = "Success: This is a test Post from Thunder Groudon"
#    GmailAPI('Test Email',message,'madhavan001@e.ntu.edu.sg')
#    FacebookAPI(message)

def GmailAPI(subject, message, receiver):
    msg =  MIMEText(message)
    msg['From'] = 'cms.dontcrysis@gmail.com'
    msg['To'] = receiver;
    msg['Subject'] = subject
    #message = 'here is the email'
    #msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()

    # secure our email with tls encryption
    mailserver.starttls()

    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('cms.dontcrysis@gmail.com', 'dontcrysis')
    mailserver.sendmail('cms.dontcrysis@gmail.com',receiver,msg.as_string())
    mailserver.quit()
    return

#if __name__ == "__main__":
#  main()
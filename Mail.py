import smtplib
import keys

def Mail(mail_id , content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login(keys.MAIL,keys.PASS)
    server.sendmail(keys.MAIL, mail_id, content)
    server.close()



import smtplib

from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Qudusini De' Boss"
email['to'] = "hello@abdulqudus.com"
email['subject'] = 'Random note of Love'

email.set_content("Love yourz, - There's no life that's better than yourz")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("justleftjupiter@gmail.com", "abdqudus100")
    smtp.send_message(email)
    #smtp.sendmail(email)
    print("All Good")
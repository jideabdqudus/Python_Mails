import smtplib

from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())

email = EmailMessage()
email['from'] = "Qudusini"
email['to'] = "hello@abdulqudus.com"
email['subject'] = "Welcome to our company"

email.set_content(html.substitute({'name': 'Abdul'}), 'html')
# email.set_content("Love yourz, - There's no life that's better than yourz")

print("Begin")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    print("Start")
    smtp.ehlo()
    smtp.starttls()
    smtp.login("justleftjupiter@gmail.com", "abdqudus100")
    smtp.send_message(email)
    print("All Good")

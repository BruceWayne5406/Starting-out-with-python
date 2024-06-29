from email.message import EmailMessage
import ssl
import smtplib

email_sender="ruhilharsh80@gmail.com"
email_password="rfvk ikgq dqfq ylsi"

email_receiver="ruhilharsh8@gmail.com"

subject="Making an email sender using python"
body="here we have made an email sender using python and now we are going to post it on github"

em=EmailMessage()
em["from"]=email_sender
em["to"]=email_receiver
em["subject"]=subject
em.set_content=body

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())



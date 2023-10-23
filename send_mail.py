import smtplib , ssl
import os 



def send_alert(message , email_address):
    host = "smtp.gmail.com"
    port = 465

    username="shrijeetkumarverma140504@gmail.com"
    password = os.getenv("PASSWORD_NEWS")
    context =ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host,port=port , context=context) as server:
        server.login(username , password)
        reciever=email_address.strip()
        server.sendmail(username,reciever,message.encode("utf-8"))
        
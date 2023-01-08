import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_send(sender_email,password,receiver_email,message):

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text =message
    # html = """\
    # <html>
    #   <body>
    #     <p>Hi,<br>
    #        How are you?<br>
    #        <a href="http://www.realpython.com">Real Python</a> 
    #        has many great tutorials.
    #     </p>
    #   </body>
    # </html>
    # """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)

    # Create secure connection with server and send email
    
    server= smtplib.SMTP('smtp-mail.outlook.com', 587) 
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


# fill the details  hereV


sender_email = "dheeraj20052005@outlook.com"
receiver_email = "dlovej009@gmail.com"
password = "Dheeraj@2006"
message=""

mail_send(sender_email,password,receiver_email,message)
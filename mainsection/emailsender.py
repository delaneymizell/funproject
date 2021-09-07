import smtplib

def emailsenderclass():
    sender_email = "memesx69420@gmail.com"
    receiver_email = input(str("enter the desired email"))
    password = input(str("enter your password"))
    message  = "pee pee poo poo"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,password)
    print("Login success")
    server.sendmail(sender_email, receiver_email, message)
    print("Email has been sent")


import smtplib

myemail = "rrahul.png@gmail.com"
password = "dcyancdqvglhnitf"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=myemail, password=password)
connection.sendmail(from_addr=myemail, to_addrs="rsrangarajan01@gmail.com", msg="Subject:Hello\n\nThis is an email from Python! \nFrom,\nRahul Rangarajan")
connection.close()
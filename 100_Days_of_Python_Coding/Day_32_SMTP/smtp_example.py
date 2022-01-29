import smtplib

my_email = "xyz.gmail.com"
password = "1234abcd"

with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="abc.yahoo.com",
        msg="Subject:Hello\n\nThis is the body of email",
    )

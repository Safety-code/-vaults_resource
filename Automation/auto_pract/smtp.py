import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

#smtp over SSL connection
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
print(type(smtpObj))
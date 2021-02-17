# add 0 inplace of empty cells before sending using ->
# df.fillna(0, inplace=True, downcast='infer')

import pandas as pd
import smtplib
import string

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from PIL import Image, ImageDraw, ImageFont
from pandas import ExcelWriter
from pandas import ExcelFile

# enable less secure apps for gmail emails before using
p_wE_d = "SomePasword"  # put email password here
fromaddr = "someemail@gmail.com"  # put email here with which you want to send.

df = pd.read_csv(
    "/path/to/file.csv"
)  # put path of csv with data (email IDs and other personalisation stuff) here.
df.fillna(0, inplace=True, downcast="infer")
# df1 = df.iloc[133:]
# ^ use if there is some error in sending a specific email to continue sending the rest
df1 = df
for i in df1.index:
    name = df1["Name"][i]  # here "Name" is column (field) name
    # P1Marks=df1["P1 Marks"][i]
    # P2Marks=df1["P2 Marks"][i]
    # P3Marks=df1["P3 Marks"][i]
    # P4Marks=df1["P4 Marks"][i]
    # P5Marks=df1["P5 Marks"][i]
    # P6Marks=df1["P6 Marks"][i]
    # TotalMarks=df1["Total Marks"][i]
    # declare more variables like wise
    name.upper()
    print(i + 1, name)
    toaddr = df1["Email-ID"][i]
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "Subject of the email"  # update subject here
    body = f"""
Email Body Text. 
Use variables as {name}.
    """

    msg.attach(MIMEText(body, "plain"))
    filename = (
        "/path/to/folder/with/attachements/" + name + ".pdf"
    )  # if you want to attach some personalised files, declare path to folder with stuff here (example: certificates)
    attachment = open(filename, "rb")
    p = MIMEBase("application", "octet-stream")
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header("Content-Disposition", "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(fromaddr, p_wE_d)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)

s.quit()

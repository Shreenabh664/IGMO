from PIL import Image, ImageDraw, ImageFont
import pandas as pd
form = pd.read_csv("/content/DBx.csv") #put path to csv here
name_list = form['Name'].to_list()
#print(name_list[88]) #to test if it is loaded correctly

location = (208 , 709) #coordinates of top left corner of the box
text_color = (0, 0, 0) #black
font = ImageFont.truetype('/usr/share/fonts/truetype/FontsFree-Net-SFProDisplay-Regular.ttf', 150) #path to font (in usr/share/fonts only), font size

#dummy_list = ['Name Surname']
for i in name_list: #change to dummy_list for testing
  im = Image.open("/content/IMGO PART CERT.png") #path to template cert
  d = ImageDraw.Draw(im)
  d.text(location, i, fill=text_color, font=font)
  im.save("/content/DBx-Certs/" + i + ".pdf") #will be saved in dir as mentioned
  
#!zip -r /content/DBx-Certs.zip /content/DBx-Certs/
#to download as zip if using colab

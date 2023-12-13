#python3 -m pip install Pillow==9.5.0
from pandas import read_csv
from PIL import Image, ImageDraw, ImageFont
import random

data = read_csv("js-list.csv").values.tolist()
template = Image.open("js-list.png")
font = ImageFont.truetype("SFPro.ttf",70)
eventfont = ImageFont.truetype("SFPro.ttf",70)
color = (255,255,255)

def makeCertificate(student):
    cert = template.copy()
    draw = ImageDraw.Draw(cert)
    #name
    w, h = draw.textsize(student[0],font)
    # draw.text(xy = (960-w/2,535),text=student[0],fill=color,font=font)
    #rank
    if student[0] != "None":
        #llosr
        # draw.rectangle([(2700,1217),(1257,1076)], fill ="white") 
        # draw.rectangle([(2700,1217),(1257,1076)], fill =color) 
        draw.text(xy = (650,600),text=student[0],fill=color,font=font)
        # draw.text(xy = (3500,1100),text=student[1],fill=color,font=font)
    else:
        #rank holder
        w,h = draw.textsize(student[0],font)
        raw.text(xy = (650,600),text=student[0],fill=color,font=font)
  
    cert.save(str("img/"+student[0])+str(random.randint(1000,9999))+".png")
    
# for i in data:
#     makeCertificate(i)
def start():
    for student in data:
        cert = makeCertificate(student)
        print(student[0])

start()

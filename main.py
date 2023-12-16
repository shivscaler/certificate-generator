''' 
    -> Main.py <-

    Is responsible for carrying out the certification creation task and at
    the same time pushing the created certificates image-path respectively to
    the data dictionary.
'''

from pandas import read_csv
from agentMailer import send_emails_concurrently
from PIL import Image, ImageDraw, ImageFont
import random

data = read_csv("js-list.csv").values.tolist()
template = Image.open("testingImage.jpg")
font = ImageFont.truetype("SFPro.ttf",70)
eventfont = ImageFont.truetype("SFPro.ttf",70)
color = (255,255,255)

def makeCertificate(student):
    cert = template.copy()
    draw = ImageDraw.Draw(cert)
    #name
    nameTextLength = draw.textlength(student[0], font)
    namexpos = cert.size[0]/2 - nameTextLength/2
    # w, h = draw.textsize(student[0],font)
    # draw.text(xy = (960-w/2,535),text=student[0],fill=color,font=font)
    #rank
    if student[0] != "None":
        #llosr
        # draw.rectangle([(2700,1217),(1257,1076)], fill ="white") 
        # draw.rectangle([(2700,1217),(1257,1076)], fill =color) 
        draw.text(xy = (namexpos,400),text=student[0],fill=color,font=font)
        # draw.text(xy = (3500,1100),text=student[1],fill=color,font=font)
    else:
        #rank holder
        w,h = draw.textsize(student[0],font)
        draw.text(xy = (650,600),text=student[0],fill=color,font=font)
  
    random_int = random.randint(1000,9999)
    cert.save(str("img/"+student[0])+str(random_int)+".png")
    
    return str(student[0])+str(random_int)+".png"

# Start the certificate creation
def start():
    for i in range(0, len(data)):
        certificate_name = makeCertificate(data[i])
        data[i].append(certificate_name)
        print(data[i])
        
# Added print functions to monitor the processes in the terminal
start()
print()
print("Certificates Generated Successfully.")

print("Started with mail sending workers.")
print()
send_emails_concurrently(data)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from concurrent.futures import ThreadPoolExecutor

''' 
    -> agentMailer.py <-

    Is responsible for doing the heavy lifting of sending the emails to the participants
    with the attached certificates.

    We are leveraging the power of concurrent.futures -> ThreadPoolExecutor to asynchronously
    sending the email since each email sending process takes significant time.

    The amount of max_workers/threads can be adjusted below in the code. Which depends on the
    machines specifications.

'''

def agentMailer(receiver_name, receiver_email, image_path):
    # Email configuration
    sender_email = ""
    sender_password = ""
    receiver_email = receiver_email
    subject = "Hi, from Scaler's Discord Community."

    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_name
    msg['Subject'] = subject

    # Email body
    body = "Hope, you enjoyed participating in the event."
    msg.attach(MIMEText(body, 'plain'))

    # Attach an image to the email
    image_path = "img/"+image_path
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        image = MIMEImage(image_data, name="image.jpg")
        msg.attach(image)

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print("Email sent successfully to -", receiver_name)

def send_emails_concurrently(data):
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda x: agentMailer(*x), data)
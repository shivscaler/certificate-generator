# certificate-generator
This is a repository for the Certificate Generator

### How do I get set up? ###

1.  Install PIP:
    > python -m pip install --upgrade pip

2.  Install all the required libraries from requirements.txt file using following command:
    > pip install -r requirements.txt

3.  Also need to make sure to have your own email configures with the needed permission to
    send email via third party, after generating the smtp password.

    Add the same in the following file.
    > agentMailer.py
    sender_email = ""
    sender_password = ""

### How do I run the certificate generator? ###

1.  Make sure yo have a csv file containing all the student names in column 1 and
    their email in the column 2, replace the csv name in the main.py

2.  Download any fonts of your choice, and change the .ttf file name in main.py

3.  Have the certificate template/image of your own choice and replace it's name
    in the main.py

4.  Final step - > run the generator with the following command:
    python mani.py
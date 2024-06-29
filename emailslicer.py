def slice_email():
    print("welcome to the email slicer")
    mail=input("please enter your email address: ")
    (username,domain)=mail.split("@")
    print(f"username is {username} and domain is {domain}")

slice_email()
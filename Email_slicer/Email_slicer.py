#!/usr/bin/python3
print("Email slicer")
while True:
    email = input("Email address: ")

    email_split = email.lower().strip().split("@")
    domain = email_split[-1]
    username = email_split[0]
    if ("@" not in email) or ("." not in domain) or (" " in email) or (" " in domain):
        print('domain_error: Please give a valid email address')
        print()
    else:
        print(f"username: {username}")
        print(f"domain name: {domain}")
        break


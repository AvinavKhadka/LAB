def spam_or_not(email):
    email = email.lower()
    spam_words = ["buy now", "free", "cash prize", "win", "viagra", "lottery", "million dollars"]
    for keyword in spam_words:
        if keyword in email:
            return True
    return False

email_text = input("Please enter the email text: ")

if spam_or_not(email_text):
    print("Spam.")
else:
    print("Not spam.")

from emails import email_list
import streamlit as st

# function to remove comma(,) , dash(-) and space (" ") from the texts and convert all of it to lowercase
def textmanipulator(string):
    a = ""
    b = ""
    c = ""
    splitted = string.split(" ")
    for i in splitted:
        a = a + i
    splitted = a.split("-")
    for i in splitted:
        b = b + i
    splitted = b.split(",")
    for i in splitted:
        c = c + i
    return c.lower()

def main():
    st.title("Email Probability Checker")

    input_email = st.text_input("Enter the email to be checked")

    if st.button("Check Probability"):
        a = 0
        for i in email_list:
            if textmanipulator(i[0].split(": ", 1)[1]) == textmanipulator(input_email):
                st.success(f"The given message has a high probability of being {i[1]}")
                a += 1
                break

        if a == 0:
            st.warning("No data as such in the dataset")

if __name__ == "__main__":
    main()

import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="Email_forms"):
    user_email = st.text_input("Enter your E-mail:")
    subject = st.text_input("Subject:").title()
    raw_message = st.text_area("Your Message:")
    message = f"""\

    subject: {subject}

    from: {user_email}
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your Email was sent successfully!")

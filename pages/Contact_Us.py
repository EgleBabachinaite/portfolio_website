import streamlit as st
import pandas as pd
from send_email import send_email

df = pd.read_csv("topics.csv")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox(label="What topic do you want to discuss?",
                          key="option" , options=(df))
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic {option}
{raw_message}
"""

    button = st.form_submit_button("Submit")
    if button:
        # state = st.session_state(option[0])
        send_email(message)
        st.info("Your email was sent successfully")
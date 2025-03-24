import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker" ,page_icon="🔐")

st.title=("Password Strength Checker.")

st.markdown(""" 
## Welcome to the Password Strength Checker!
Use this tool to check your password strength and get tips to **improve it**.""")

password = st.text_input("Enter your Password",type= "password")

feedback =[]

score = 0

if password:
    if len(password) >=8:
        score+=1
    else :
        feedback.append("❌Password should at least 8 characters Long")

    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) :
        score +=1
    else :
        feedback.append("❌ Password should contain both upper and lower case characters.")
        
    if re.search(r'\d',password):
        score +=1
    else :
        feedback.append("❌ Password should contain atleast 1 digit")

    if re.search(r'[!@#$%^&*]',password):
        score +=1
    else :
        feedback.append("❌ Password should contain atleast 1 special character(!@#$%^&*)")
    
    if score == 4:
        feedback.append("✅Your Password is strong!.")
    elif score==3:
        feedback.append("🟡 Your password is decent, but it can be even stronger!.")
    else:
        feedback.append("🔴 Your Password is weak! Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Sugestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("🔑 Enter your password to begin the check!")
    
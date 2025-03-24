import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")

st.markdown(""" 
## Welcome to the Password Strength Checker!  
Use this tool to check your password strength and get tips to **make it stronger**.
""")

# Password Input
password = st.text_input("🔑 Enter your password", type="password")

# Button to trigger password check
if st.button("Check Password Strength"):
    if password:  # Only check if a password is entered
        feedback = []
        score = 0

        # Password Strength Rules
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be at least 8 characters long.")

        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("❌ Password should include both uppercase and lowercase letters.")

        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one number.")

        if re.search(r'[!@#$%^&*]', password):
            score += 1
        else:
            feedback.append("❌ Password should include at least one special character (!@#$%^&*).")

        # Strength Evaluation
        if score == 4:
            feedback.append("✅ Your password is **strong**! 🔥")
        elif score == 3:
            feedback.append("🟡 Your password is **decent**, but you can make it even stronger! 💪")
        else:
            feedback.append("🔴 Your password is **weak**! Consider improving it. ❗")

        # Display Feedback
        st.markdown("## 🔍 Password Analysis & Suggestions")
        for tip in feedback:
            st.write(tip)

    else:
        st.warning("⚠️ Please enter a password before checking!")

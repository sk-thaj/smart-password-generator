import streamlit as st
import random
import string

st.title("🔐 Smart Password Generator")

length = st.number_input("Enter password length", min_value=4, max_value=30, value=12)

password = []
char_pool = []

# own characters
use_name = st.checkbox("Include your own characters (name)")

if use_name:
    name_chars = st.text_input("Enter your characters")
    if name_chars:
        password.extend(name_chars)
        char_pool.extend(name_chars)
else:
    char_pool.extend(string.ascii_lowercase)

# uppercase
uppercase = st.checkbox("Include uppercase letters")

if uppercase:
    char_pool.extend(string.ascii_uppercase)

# numbers
numbers = st.checkbox("Include numbers")

if numbers:

    custom_num = st.checkbox("Use your own number")

    if custom_num:
        user_num = st.text_input("Enter your number")
        if user_num:
            password.extend(user_num)
            char_pool.extend(user_num)
    else:
        char_pool.extend(string.digits)

# symbols
symbols = st.checkbox("Include special characters")

if symbols:

    custom_sym = st.checkbox("Use your own symbol")

    if custom_sym:
        user_sym = st.text_input("Enter your symbol")
        if user_sym:
            password.extend(user_sym)
            char_pool.extend(user_sym)
    else:
        char_pool.extend(string.punctuation)

if st.button("Generate Passwords"):

    st.subheader("Generated Passwords")

    for i in range(3):

        temp_password = password.copy()

        while len(temp_password) < length:
            temp_password.append(random.choice(char_pool))

        random.shuffle(temp_password)

        final_password = "".join(temp_password[:length])

        st.success(f"Password {i+1}: {final_password}")
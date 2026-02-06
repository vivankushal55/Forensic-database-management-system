import pickle
from pathlib import Path
import streamlit as st
from add2 import add
from read import read
from queries import predef_queries
from queries import query_cmd
from update import update
from delete import delete
from read import add_bg_from_url
from read import sidebar_bg
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator




# --- USER AUTHENTICATION ---
names = ["Bhuvan", "Chandan"]
usernames = ["Bhuvan", "chandan"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    def main():
        st.title("Forensics Database")
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")
        add_bg_from_url()
        sidebar_bg()
        menu = ["Add Records", "View Tables", "Update Record", "Delete Records", "Run Predefined Queries", "CMD"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add Records":
            add()
        elif choice == "View Tables":
            read()
        elif choice == "Update Record":
            update()
        elif choice == "Delete Records":
            delete()
        elif choice=="Run Predefined Queries":
            predef_queries()
        elif choice=="CMD":
            query_cmd()

    if __name__ == '__main__':
     main()
   
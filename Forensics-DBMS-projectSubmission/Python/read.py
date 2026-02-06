import streamlit as st
import pandas as pd
from database import viewTables

def read():
    menu = ["Drugs", "Ballistics", "Paint", "Automobile", "Cases", "Criminal","CriminalCase"]
    choice = st.sidebar.selectbox("Menu", menu)
    result = viewTables(choice)
    #print(result)
    if choice==menu[0]:
        df = pd.DataFrame(result, columns=("Case ID", "NDC Code", "Name","Color", "Class", "Narcotic")) 
    elif choice==menu[1]:
        df = pd.DataFrame(result, columns=("Case ID", "ID", "Make", "Manufacturer", "Year of Manufacture", "Type", "Caliber", "Gauge", "Country of Origin"))
    elif choice==menu[2]:
        df = pd.DataFrame(result, columns=("Case ID", "ID", "Color", "Solvent", "Binder", "Pigment", "Additive"))
    elif choice==menu[3]:
        df = pd.DataFrame(result, columns=("Case ID", "ID", "Model", "Year of Manufacture", "Manufacturer", "Type"))
    elif choice==menu[4]:
        df = pd.DataFrame(result, columns=("Case ID", "Type", "Name", "Leading Officer", "Assissting Officer", "Time of Report", "Location", "Status"))
    elif choice==menu[5]:
        df = pd.DataFrame(result, columns=("Criminal ID", "Name", "Alias", "Age", "Number of Cases", "Dominant Hand", "Status", "DNA", "Fingerprint", "Nationality"))
    elif choice==menu[6]:
        df = pd.DataFrame(result, columns=("CriminalID", "CrimeID"))
    st.dataframe(df)

def add_bg_from_url():
        st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.rochester.edu/newscenter/wp-content/uploads/2019/03/fea-forensic-evidence-fingerprint.jpg");
             background-attachment: fixed;
             background-size: cover
           }}
         </style>
         """,
         unsafe_allow_html=True
        )

def sidebar_bg():

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(https://thumbs.dreamstime.com/z/dna-research-forensic-science-molecule-use-63632579.jpg);
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
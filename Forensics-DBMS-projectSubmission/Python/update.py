import streamlit as st
from database import updateStatus
from database import updateStatus1
from database import viewTables
import pandas as pd
from database import get_case_no
from database import get_criminal_no

def update():
    menu = ["Cases", "Criminal"]
    choice = st.sidebar.selectbox("Menu", menu)
    result = viewTables(choice)
    #print(result)
    if choice==menu[0]:
        df = pd.DataFrame(result, columns=("Case ID", "Type", "Name", "Leading Officer", "Assissting Officer", "Time of Report", "Location", "Status"))
    elif choice==menu[1]:
        df = pd.DataFrame(result, columns=("Criminal ID", "Name", "Alias", "Age", "Number of Cases", "Dominant Hand", "Status", "DNA", "Fingerprint", "Nationality")) 
    st.dataframe(df)
    c1, c2 = st.columns(2)
    with c1:
        if (choice=="Criminal"):
            id=st.selectbox("Enter Criminal ID", [i[0] for i in get_criminal_no()])
        elif(choice=="Cases"):
            id=st.selectbox("Enter Crime ID", [i[0] for i in get_case_no()])
    with c2:
        if (choice=="Criminal"):
            UpdateChoice = st.selectbox("ColumnName: ", ["CName","Alias", "Age", "NoOfCases",  "DominantHand", "CurrentStatus","DNAID","FingerprintID","nationality"])
            Name = st.text_input("Chnage To")
        elif(choice=="Cases"):
            UpdateChoice = st.selectbox("ColumnName: ", ["TypeOfCase","NameOfCase", "LeadingOfficer", "AsstOfficer",  "Loc", "statusOfCase"])
            Name = st.text_input("Change To")
    if st.button("Update Record"):
            updateStatus1(id, UpdateChoice, choice,Name)
            st.success("Successfully updated record")
    result = viewTables(choice)
    df = pd.DataFrame(result)
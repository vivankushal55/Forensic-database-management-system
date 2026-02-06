import streamlit as st
from database import updateStatus
from database import updateStatus1
from database import viewTables
import pandas as pd
from database import get_case_no
from database import get_criminal_no
from database import get_automobile_no
from database import get_ballistics_no
from database import get_drug_no
from database import get_paint_no
from database import get_case_no
from database import get_criminal_no
from database import get_criminalcase_no
def update1():
    menu = ["Cases", "Criminal","Automobile", "Ballistics","Drugs","Paint","CriminalCase"]
    choice = st.sidebar.selectbox("Menu", menu)
    result = viewTables(choice)
    #print(result)
    #Cases
    if choice==menu[0]:
        df = pd.DataFrame(result, columns=("Case ID", "Type", "Name", "Leading Officer", "Assissting Officer", "Time of Report", "Location", "Status"))
    #Criminal
    elif choice==menu[1]:
        df = pd.DataFrame(result, columns=("Criminal ID", "Name", "Alias", "Age", "Number of Cases", "Dominant Hand", "Status", "DNA", "Fingerprint", "Nationality")) 
    #Automobile
    elif choice==menu[2]:
        df = pd.DataFrame(result, columns=("Case ID", "ID", "Model", "Year of manufacture", " Manufacturer", "Type"))
    #Ballistics
    elif choice==menu[3]:
        df = pd.DataFrame(result, columns=("Case ID", "ID", "Make","Manufacturer", "Year of manufacture", " Type", "Guage","Caliber","Country Of Origin"))
    #drugs
    elif choice==menu[4]:
        df = pd.DataFrame(result, columns=("Case ID", "NDC Code", "Name", "Color", " Class", "Narcotic"))
    #paint
    elif choice==menu[5]:
        df = pd.DataFrame(result, columns=("Case ID", "ID", "Color", "Solvent", " Binder", "Pigment","Additive"))
    #CriminalCase
    elif choice==menu[6]:
        df = pd.DataFrame(result, columns=("CriminalID", "CrimeID")) 
    st.dataframe(df)
    c1, c2 = st.columns(2)
    with c1:
        if (choice=="Criminal"):
            id=st.selectbox("Enter Criminal ID", [i[0] for i in get_criminal_no()])
        elif(choice=="Cases"):
            id=st.selectbox("Enter Crime ID", [i[0] for i in get_case_no()])
        elif choice=="Automobile":
            id=st.selectbox("Enter Automobile ID", [i[0] for i in get_automobile_no()])
            #id = [i[0] for i in get_automobile_no()]
        elif choice=="Ballistics":
             id=st.selectbox("Enter Ballistics ID", [i[0] for i in get_ballistics_no()])
            #id = [i[0] for i in get_ballistics_no()]
        elif choice=="Drugs":
             id=st.selectbox("Enter Drugs ID", id = [i[0] for i in get_drug_no()])
            #id = [i[0] for i in get_drug_no()]
        elif choice=="Paint":
             id=st.selectbox("Enter Paint ID", [i[0] for i in get_paint_no()])
            #id = [i[0] for i in get_paint_no()]
        elif choice=="CriminalCase":
             id=st.selectbox("Enter Crime ID", [i[0] for i in get_criminalcase_no()])
            #id = [i[0] for i in get_criminalcase_no()]

    with c2:
        if (choice=="Criminal"):
            UpdateChoice = st.selectbox("ColumnName: ", ["CName","Alias", "Age", "NoOfCases",  "DominantHand", "CurrentStatus","DNAID","FingerprintID","nationality"])
            Name = st.text_input("Chnage To")
        elif(choice=="Cases"):
            UpdateChoice = st.selectbox("ColumnName: ", ["TypeOfCase","NameOfCase", "LeadingOfficer", "AsstOfficer",  "Loc", "statusOfCase"])
            Name = st.text_input("Change To")
        elif(choice=="Automobile"):
            UpdateChoice = st.selectbox("ColumnName: ", ["CaseID", "AID", "model", "Year", "Manufacturer", "typeOfVehicle"])
            Name = st.text_input("Change To")
        elif(choice=="Ballistics"):
            UpdateChoice = st.selectbox("ColumnName: ", ["CaseID", "B_ID", "Model", "Year","Manufacturer"," typeOfGun", "caliber","gauge","CountryOfOrigin"])
            Name = st.text_input("Change To")
        elif(choice=="Drugs"):
            UpdateChoice = st.selectbox("ColumnName: ", ["CaseID", "NDC_No", "dname", "color", "class", "narcotic"])
            Name = st.text_input("Change To")
        elif(choice=="Paint"):
            UpdateChoice = st.selectbox("ColumnName: ", ["CaseID", "PID", "Color", "Solvent", "Binder", "Pigments","Additive"])
            Name = st.text_input("Change To")
        elif(choice=="CriminalCase"):
            UpdateChoice = st.selectbox("ColumnName: ", ["CriminalID", "CrimeID"])
            Name = st.text_input("Change To")

    if st.button("Update Record"):
            updateStatus1(id, UpdateChoice, choice,Name)
            st.success("Successfully updated record")
    result = viewTables(choice)
    df = pd.DataFrame(result)
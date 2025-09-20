
import streamlit as st
import pandas as pd

st.title("BMIS3713 Management Information System")
st.subheader("Tutor: Dr Leong Lai Hoong")

# Google Sheets CSV export link
sheet_url = "https://docs.google.com/spreadsheets/d/1-SX4N8daTJqOW7nXRGB85k7Cw44VytRT/export?format=csv"

try:
    df = pd.read_csv(sheet_url)
    st.success("Student marks loaded from Google Sheets!")

    st.write("### Student Login")
    student_id = st.text_input("Enter your Student ID")
    email = st.text_input("Enter your Email ID")

    if st.button("Check Marks"):
        student = df[
            (df['student id'].astype(str).str.strip() == student_id.strip()) &
            (df['email id'].str.strip().str.lower() == email.strip().lower())
        ]
        if not student.empty:
            st.success("Record found!")
            st.write(f"**Assignment Mark:** {student.iloc[0]['Assignment mark']}")
            st.write(f"**Mid Term Mark:** {student.iloc[0]['mid term mark']}")
        else:
            st.error("Student ID or Email not found. Please check your input.")
except Exception as e:
    st.error(f"Failed to load data from Google Sheets: {e}")

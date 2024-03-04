import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Google Sheets ID
sheet_id = '1QQ-NKZ6gNwBMIVoxpo7rpWHY-fU20ZyteJGr8vNkolU'

# Streamlit app
st.title("Form Submission")

# Form fields
name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Submit"):
    # Validate form data
    if not name or not email:
        st.error("Name and email are required")
    else:
        try:
            # Open the Google Sheet
            sheet = client.open_by_key(sheet_id).sheet1

            # Append data to the sheet
            sheet.append_row([name, email])

            st.success("Form submitted successfully")
        except Exception as e:
            st.error(f"Error submitting form: {str(e)}")
import streamlit as st

st.title('F1 Driver Stats Explorer')

st.markdown("""
This app performs simple webscraping of F1 Driver stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** .
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))
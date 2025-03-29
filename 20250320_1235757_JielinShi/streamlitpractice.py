import streamlit as st
st.title("Happy Loan")


criteria_annual_salary = 50000
criteria_year_of_work = 5

salary = st.number_input('Please enter your salary: ')
work_year = st.number_input('Please enter your work year: ')
if st.button('Submit'):
    if salary >= criteria_annual_salary and work_year >= criteria_year_of_work:
        st.write("Congratulation. You have passed our loan condition.")
    else:
        st.write("Sorry, we have to reject your loan request.")
        
import streamlit as st

def sum2(a,b):
    return int(a) + int(b)

def substruct(a,b):
    return int(a) - int(b)

def multiply(a,b):
    return int(a) * int(b)

def divide(a,b):
    return int(a) / int(b)



st.title("Calculator")

first_number = st.text_input("Please provide first number")
second_number = st.text_input("Please provide second number")
math_operation = st.selectbox("Please select Math operation",("SUM", "Substriction","Multipication","Division"))

button = st.button("send")


if button:
    with st.spinner("Generuje odpowiedz ..."):
        operation = ''
        if math_operation == "SUM":
            operation =  sum2(first_number,second_number)
        elif math_operation == "Substriction":
            operation = substruct(first_number, second_number)
        elif math_operation == "Multipication":
            operation = multiply(first_number, second_number)
        elif math_operation == "Division":
            operation = divide(first_number, second_number)
        st.write(operation)


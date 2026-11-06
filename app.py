import streamlit as st
st.title("Basic Calculator")
st.write("Perform simple mathematical operations")
num1=st.number_input("Enter First Number:")
num2=st.number_input("Enter Second Number:")
operation=st.selectbox(
    "select operation",
    ["Addition","Subtraction","Multiplication","Division"]
)
if st.button("Calculate"):
    if operation=="Addition":
        result=num1+num2
    elif operation=="Subtraction":
        result=num1-num2
    elif operation=="Multiplication":
        result=num1*num2
    elif operation=="Division":
        if num2!=0:
            result=num1/num2
        else:
            st.error("Cannot Divide by Zero!")   
            result=None
        if result is not None:
            st.success(f"result:{result}")     
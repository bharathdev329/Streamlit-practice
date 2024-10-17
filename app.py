import streamlit as st
st.title('Customer lifetime valuation')

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'number1', x )

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

y=st.slider('y')
st.write(y,'Number2',y)

z=x+y
st.write(z,'sum of numbers= ',z)
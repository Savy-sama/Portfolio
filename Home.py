import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/FB.jpg", width=300)
des = """
    Given below are the python apps I have made.
    """
st.info(des)


with col2:
    st.header("Saurabh Biswas")
    content = """
    Hello! My name is Saurabh. I am a full stack web developer, student at West Bengal State University, India. 
    I am currently pursuing my Master of Science in Electronics and Tele-communication. Always in learning mode, 
    Looking forward to explore new arenas of tech and programming.
    """
    st.info(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

dataframe = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in dataframe[:10].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in dataframe[10:].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")

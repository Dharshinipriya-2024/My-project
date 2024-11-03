import streamlit as st

st.title("MY PORTFOLIO")
st.write("A Showcase of my skills and projects.")

st.header("About Me")
st.subheader("Hello! I am Dharshinipriya")
st.subheader("I am a student of IT")

col1, col2 = st.columns([1, 2])

with col1:
    st.write('''
    \n:green[**Languages Known**:] 
    \n:green[**Interested In**:] 
    \n:green[**Extracurricular Activities**:]
    \n:green[**Known Games**:] 
    \n:green[**Hobbies**: ]
   \n:green [**Aim**:] ''')

with col2:
    st.write('''\n:  Python
    \n:Coding
    \n:Dancing
    \n:Handball
     \n:Wacting webseries
    \n:I Want to place top most company in final year ''')                                           
    st.write('''I am passionate about developing projects that solve real-world problems.''')
    st.write("""
             - **Email**: [aldharshinipriya9@gmail.com](mailto:aldharshinipriya9@gmail.com)
             - **LinkedIn**: [linkedin.com/in/dharshinipriya](https://www.linkedin.com/in/dharshinipriya-234b5678)
             """)



import streamlit as st

st.title("Anurag university Student Management System")
st.subheader("SNEHA")
st.header("Welcome to the Student Management System of Anurag University")   
st.subheader("Manage student records efficiently and effectively")
st.write("Here you can add, view, update, and delete student information with ease.")
st.write(123)
st.write([1,2,3,4,5])
st.write({"name":"anurag","age":22})

#markdown method to format text
st.markdown("*Bold Text*")
st.markdown("Italic Text")
st.markdown("-item 1\n -item 2")

st.markdown("<h3 style='color:red'>Red Text</h3>", unsafe_allow_html=True)

st.code("print('hello, Anurag University!')",language='python')
st.code(""" 
        def add(a,b):
        return a+b
        """,language='python')
st.latex(r"""
a^2+b^2=c^2 
         """)

#divider line
st.divider()

#BUTTON METHOD TO CREATE A BUTTON
if st.button("Click Me"):
    st.write("Button Clicked!")
    st.success("Operation Successful!")
    st.balloons()
    st.snow()
else:
    st.write("Button not clicked yet!")
    st.error("connection error")

#text input method to get user input

name=st.text_input("enter ur name:")

if name==" ":
    st.warning("Name cannot be empty!")
elif not name.isalpha():
    st.error("invalid input. enter correct input")
else:
    st.success(f"hellow,{name}!")

feedback=st.text_area("enter feedback")
st.write(feedback)

#check box to create checkbox
if st.checkbox("i agree to the terms and conditions"):
    st.write("thanyou for agreeing!")

#radio button method to create radio buttons
gender=st.radio("select your gender:",("male","female","other"))
st.write(f"you selected :{gender}")

country=st.selectbox("select ur country:" ,("india","canada"))   
st.write(f"you selected :{country}")

a=st.multiselect(
    "select skills",
    ["pyhton","sql","ml","streamlit"]
)
st.write("skills : ",a)

#slider 
age=st.slider("select ur age:",0,100,25)
st.write(f"you are {age} years old")

#file upload
upload=st.file_uploader("choose a file:")
if upload is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename: {upload}")

#to create a form 
with st.form("my_form"):
    name=st.text_input("name")
    age=st.number_input("age" ,0,100)
    submit=st.form_submit_button("submit")
if submit:
    st.write(name,age)

#form with submit button
with st.form("login"):
    username=st.text_input("username")
    password=st.text_input("password",type="password")
    login=st.form_submit_button("login")
if login:
    st.success("login successful")

st.divider()
 
#colums to create columnns
col1,col2,col3=st.columns(3)
with col1:
    st.header("col1")
    st.write("this is col1")
with col2:
    st.header("col2")
    st.write("this is col2")
with col3:
    st.header("col3")
    st.write("this is col3")

st.divider()

#create a table
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

st.divider()

#sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

#cache
@st.cache_data
def load_data():
    return [1,2,3,4]
dats=load_data()
st.write(data)

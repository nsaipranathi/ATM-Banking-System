import streamlit as st

#header
st.header("Anurag University Student Records Management")

#title
st.title("Student CRUD Application")

#subheader
st.subheader("Manage studdent records efficiently and effectively:")

#text
st.text("succefully inserted")

#horizontal line
st.markdown("-----------------")
st.markdown("### Feature application:")
st.markdown("*italic Text*")
st.markdown("**bold Text**")
st.markdown("- item1 \n - item2")

#write to write extra info of any datatype
st.write("Hello World")
st.write("[1,2,3]")
st.write(123)
st.write({"name":"prana","age":20})
st.markdown("<h3 style='color:yellow;'>This is a blue heading</h3>", unsafe_allow_html=True)
st.caption("This is a caption")
st.code("""
def add(a,b)
    return a+b
""", language='python')

#matematical equations
st.latex(r''' e=mc^2 ''')
#divider method to separate
st.divider()
st.markdown("### End of Application")


if st.button("Click Me"):
    st.write("Button Clicked!")
    st.success("Success Message!")
    st.balloons()
    st.snow()
else:
    st.write("Button not clicked yet.")

name=st.text_input("Enter your name:")
if name == '':
    st.warning("name cannot be empty")
elif not name.isalpha():
    st.error("name should contain only alphabets")
else:
    st.success(f"Hello, {name}!") 

age=st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
st.write(f"Your age is {age}") 
feedback=st.text_area("Enter your feedback:")
st.write("Your feedback:", feedback)   



if st.checkbox("i aggree to terms and conditions"):
    st.write(f"Thank you, {name}!")
else:
    st.write("Please agree to the terms and conditions to proceed.")    
  #radio button
gender=st.radio("Select your gender:", ('Male', 'Female', 'Other'))
st.write(f"You sellected:{gender}") 
#selectbox
course=st.selectbox("Select your course:", ('B.Tech', 'M.Tech', 'MBA', 'PhD'))
st.write(f"You selected: {course}")
#multiselect
marks=st.multiselect("Select your hobbies:", ('90', '89', '80', '40', '50'))
st.write(f"Your marks are: {', '.join(marks)}")
#slider
satisfaction=st.slider("Rate your satisfaction level:", 0, 10, 5)
st.write(f"Your satisfaction level is: {satisfaction}")
#file uploader
uploaded_file=st.file_uploader("Upload your profile picture:", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    st.success(("File uploaded successfully!"))
    st.write(f"Filename: {uploaded_file.name}")
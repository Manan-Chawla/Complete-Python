import streamlit as st
from datetime import date
# title --> more like heading tag of html
st.title("Welcome to ByteEdu Learning Platform")

# text more like p tag of html
st.text("We are here to help you out with all new tech stack")

# subheader is like smaller heading tag
st.subheader("The best ed-tech platform for college students")

# write is like normal text
st.write("I am just a learning platform")

# selectbox allow user to select option like list tag
subs=st.selectbox("Select fav subject to learn : ",["Fullstack","Frontend","Backend","AI/ML"])


# for taking input text
ans=st.text_input("Enter your name : ")


# buttons 
if st.button("Fullstack developer : "):
    st.success("You are good to go")


add_subs=st.checkbox("Add new subject : Gen AI")

if add_subs:
    st.write("Your subject will be added soon")
    st.success("Thanks for choosing GEN AI as new subject ")

newsubs=st.radio("Pick your new subject  : ",["Data Analysis","Gen AI with DS","ML"])


flavor = st.sidebar.selectbox("Pick a flavor:", ["Vanilla", "Chocolate", "Strawberry"])
size = st.sidebar.radio("Pick a size:", ["Small", "Medium", "Large"])

st.write(f"You ordered a {size} {flavor} ice cream 🍨")


col1, col2 = st.columns(2)

with col1:
    st.header("📘 Left Column")
    st.write("This is the left side")

with col2:
    st.header("📗 Right Column")
    st.write("This is the right side")


with st.expander("See more details"):
    st.write("Here are the hidden details 📂")
    st.write("You can put charts, text, or anything here.")


tab1, tab2 = st.tabs(["🏠 Home", "📊 Data"])

with tab1:
    st.write("Welcome to the Home tab!")

with tab2:
    st.write("Here is some data...")
    
    
# for using image within the program we use image function
# st.image()


# this is slider , in which 
# arg are as follows:
# " "  represent the heading of slider
# 0 is starting point
# 10 is ending point
# 2 is the default value of that slider
slide=st.slider("Level of understanding Python : ",0,10,2)
st.write("Level of understanding Python : ",slide)



# for taking number input from user
nums=st.number_input("Enter your age : ")
st.write(f"Age : {nums}")
if nums==24:
    st.title(f"Welcome to the new world of coding")
else:
    st.header(f"Sorry you need to be 24 to get in")
    
# to get date input
dob = st.date_input("Enter your birthday:")

# Show DOB
st.subheader(f"DOB : {dob}")

# Calculate age
if dob:
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.subheader(f"Your Age: {age} years")


# printing extras
# st.title("USERNAME : "+ans)
# st.write(subs)


# if ans == "Manan":
#     print(f"{subs}")
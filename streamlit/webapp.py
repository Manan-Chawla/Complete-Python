import streamlit as st

col1,col2=st.columns(2)

with col1:
    st.image('logo.png',width=200)
    
with col2:
    st.title("ByteEdu Learning Platform")
    st.tabs(["Home","About","Course","Notes"])
    
st.tabs(["     ","     ","     ","     ","     ","     ","     ","     ",])

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg35HjCgLvp3fvGhMForwuiuvmAssl07yaWQ&s",width=800)


st.header("About Us ")
with st.expander("Who we are ? "):
    st.text("At ByteEdu, learning starts with understanding the fundamentals. Our beginner-friendly courses are designed to build a strong foundation, allowing students to progress confidently in their software development and engineering journeys. Each course offers interactive lessons, real-world projects, and expert guidance to make learning both practical and enjoyable.")
    
with st.expander("How do we support collobrative learning ? "):
    st.text("ByteEdu believes that learning is a collaborative journey. Through our community forums, peer discussion groups, and mentorship programs, students can connect, share knowledge, and grow together. Our instructors and support team are always available to provide feedback and answer questions, fostering a supportive and interactive learning environment.")
    
with st.expander("Why is ByteEdu the top choice for aspiring developer ? "):
    st.text("ByteEdu stands out for its industry-aligned curriculum, experienced instructors, and commitment to student success. Our courses are tailored to meet the latest industry standards, ensuring that learners acquire skills that are in demand in today’s tech job market. We also provide portfolio-building projects that showcase your skills to potential employers.")
st.tabs(["     ","     ","     ","     ","     ","     ","     ","     ",])
    
    
st.header("Course We Offer ")

st.success("AI/ML")
st.warning("Data Analytics")
st.error("Full Stack Development ")
st.success("Gen AI")
st.warning("Web Development")
st.error("Android Development ")


st.tabs(["     ","     ","     ","     ","     ","     ","     ","     ",])


st.header("Our Team")
col3,col4,col5= st.columns(3)


with col3:
    st.image("https://byteedu.co.in/images/team/anshika.jpg",width=200)
    st.subheader("Anshika Mishra")
    st.text("Co-Founder")
    
with col4:
    st.image("https://byteedu.co.in/images/team/ananya.jpg",width=200)
    st.subheader("Ananya Sharma ")
    st.text("Vice President")

with col5:
    st.image("https://byteedu.co.in/images/team/manan.png",width=200)
    st.subheader("Manan Chawla ")
    st.text("Founder")
    
st.tabs(["     ","     ","     ","     ","     ","     ","     ","     ",])



# pandas
# matplotlib   5
# seaborn     10

# will create 3 project (1 for each and then will post over linkedin)

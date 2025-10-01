import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Manan Chawla - Portfolio", page_icon="💼", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .big-font {
            font-size:30px !important;
            font-weight: bold;
            color: #2C3E50;
        }
        .title {
            font-size:50px !important;
            font-weight: 700;
            color: #1E90FF;
        }
        .subtitle {
            font-size:20px !important;
            color: #34495E;
        }
        .card {
            padding:20px;
            border-radius:12px;
            background-color:slateblue;
            box-shadow:0 2px 10px rgba(0,0,0,0.1);
            margin-bottom:20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- SIDEBAR ----
st.sidebar.image("logo.png", use_column_width=True)
menu = st.sidebar.radio("📍 Navigate", ["🏠 Home", "👨 About", "💼 Experience", "🚀 Projects", "🛠️ Skills", "🎓 Education", "📜 Certifications", "📩 Contact"])

# ---- HOME ----
if menu == "🏠 Home":
    col1, col2 = st.columns([2,3])

    with col1:
        st.image("logo.png", width=250)

    with col2:
        st.markdown('<p class="title">Hi, I\'m Manan Chawla</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Founder of ByteEdu | Tech Consultant | Full Stack Developer</p>', unsafe_allow_html=True)
        st.write("📍 Jaipur, Rajasthan | 📧 chawlamanan26@gmail.com | 📞 +91-9829296192")
        st.markdown("---")
        st.success("🚀 Welcome to my portfolio website built with Streamlit.")

# ---- ABOUT ----
elif menu == "👨 About":
    st.header("👨 About Me")
    st.markdown("""
    <div class="card">
    I am a passionate **Tech Consultant and Founder of ByteEdu**, with experience delivering 
    **technical presentations, training sessions, and digital tools** to NGOs and grassroots organizations.  

    My work supports **child protection, advocacy efforts, and efficient digital systems**.  

    I’ve also worked as a **Google Cloud Intern, Postman Student Expert, and Salesforce Trailhead achiever**.  
    My mission is to **leverage technology to create meaningful impact in communities**.
    </div>
    """, unsafe_allow_html=True)

# ---- EXPERIENCE ----
elif menu == "💼 Experience":
    st.header("💼 Work Experience")

    st.markdown("""
    <div class="card">
    <h4>Tech Consultant | AFJ</h4>
    • Delivered technical presentations and training to clients.  
    • Supported NGOs with digital tools for child protection, data management, and case tracking.  
    • Integrated tech solutions into advocacy efforts.  
    • Managed multiple projects successfully.  
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h4>Google Cloud Intern</h4>
    • Built AI-powered text translation app from images (Vision + Translation API).  
    • Enhanced efficiency by 25%.  
    • Developed scalable solutions with Google Cloud services.  
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h4>Postman Student Expert</h4>
    • Developed structured data API for user data management.  
    • Designed, tested, and documented robust APIs.  
    </div>
    """, unsafe_allow_html=True)

# ---- PROJECTS ----
elif menu == "🚀 Projects":
    st.header("🚀 Featured Projects")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h4>🌐 Aasra Foundation Jaipur</h4>
        • CSR Project (NGO website with donation integration).  
        • Payment gateway + email automation.  
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h4>🏠 Homyz Real Estate</h4>
        • MERN stack project with real-time updates & map search.  
        • Fully responsive & user-friendly.  
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h4>📊 Acowalian News</h4>
        • Platform for unbiased breaking news & analysis.  
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h4>🏨 Gaj Kesri Hotel Website</h4>
        • Luxury hotel site with booking & event sections.  
        • Focused on premium design & mobile optimization.  
        </div>
        """, unsafe_allow_html=True)

# ---- SKILLS ----
elif menu == "🛠️ Skills":
    st.header("🛠️ Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Languages")
        st.write("JavaScript, PHP, C++, Python (Basic)")

    with col2:
        st.subheader("Frontend")
        st.write("Next.js, React, TypeScript, Bootstrap")

    with col3:
        st.subheader("Backend")
        st.write("Node.js, Express.js, MongoDB, SQL, REST APIs")

    st.subheader("Other Tools")
    st.write("Firebase Auth, API Integration, Electron.js")

# ---- EDUCATION ----
elif menu == "🎓 Education":
    st.header("🎓 Education")
    st.markdown("""
    <div class="card">
    <h4>Maharishi Arvind Science Management and Studies - BCA (2021-2024)</h4>
    • Strong foundation in Computer Science & Software Development.  
    • Projects in Web Dev, Databases, and Software Engineering.  
    </div>
    """, unsafe_allow_html=True)

# ---- CERTIFICATIONS ----
elif menu == "📜 Certifications":
    st.header("📜 Certifications")
    st.markdown("""
    <div class="card">
    - Amazon AWS Solution Architect  
    - Moreton Bay Region Entrepreneurship & Innovation  
    - Postman API Student Expert  
    - Text Summarize App  
    - Inventory Management System  
    - Web Development (SkillSoft)  
    </div>
    """, unsafe_allow_html=True)

# ---- CONTACT ----
elif menu == "📩 Contact":
    st.header("📩 Contact Me")
    st.markdown("""
    <div class="card">
    📧 Email: [chawlamanan26@gmail.com](mailto:chawlamanan26@gmail.com)  
    💼 LinkedIn: [linkedin.com](https://linkedin.com)  
    🐙 GitHub: [github.com](https://github.com)  
    🌐 Founder of [ByteEdu](https://byteedu.co.in)  
    </div>
    """, unsafe_allow_html=True)

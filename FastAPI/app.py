import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

# -------------------------------
# Session state initialization
# -------------------------------
if "token" not in st.session_state:
    st.session_state.token = None

# -------------------------------
# Helper Functions
# -------------------------------
def is_logged_in():
    return st.session_state.token is not None


def get_headers():
    return {
        "Authorization": f"Bearer {st.session_state.token}"
    }


# -------------------------------
# LOGIN PAGE
# -------------------------------
def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(
            f"{BASE_URL}/login",
            data={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            token = response.json()["access_token"]
            st.session_state.token = token
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")


# -------------------------------
# DASHBOARD
# -------------------------------
def dashboard():
    st.title("🎓 Student Management System")

    # Logout
    if st.button("Logout"):
        st.session_state.token = None
        st.rerun()

    st.markdown("---")

    # -------------------------------
    # CREATE STUDENT
    # -------------------------------
    st.subheader("➕ Add Student")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)

    if st.button("Create Student"):
        response = requests.post(
            f"{BASE_URL}/students",
            json={"name": name, "age": age},
            headers=get_headers()
        )

        if response.status_code in [200, 201]:
           st.success("Student created successfully")
        else:
           st.error("Failed to create student")


    st.markdown("---")

    # -------------------------------
    # LIST STUDENTS
    # -------------------------------
    st.subheader("📋 Students List")

    response = requests.get(
        f"{BASE_URL}/students",
        headers=get_headers()
    )

    if response.status_code == 200:
        students = response.json()
        st.table(students)
    else:
        st.error("Unable to fetch students")

    st.markdown("---")

    # -------------------------------
    # UPDATE STUDENT
    # -------------------------------
    st.subheader("✏️ Update Student")

    student_id = st.number_input("Student ID", min_value=1)
    new_name = st.text_input("New Name")
    new_age = st.number_input("New Age", min_value=1, max_value=100)

    if st.button("Update Student"):
        response = requests.put(
            f"{BASE_URL}/students/{student_id}",
            json={"name": new_name, "age": new_age},
            headers=get_headers()
        )

        if response.status_code == 200:
            st.success("Student updated")
        else:
            st.error("Update failed")

    st.markdown("---")

    # -------------------------------
    # DELETE STUDENT
    # -------------------------------
    st.subheader("🗑️ Delete Student")

    delete_id = st.number_input("Delete Student ID", min_value=1, key="delete")

    if st.button("Delete Student"):
        response = requests.delete(
            f"{BASE_URL}/students/{delete_id}",
            headers=get_headers()
        )

        if response.status_code == 200:
            st.success("Student deleted")
        else:
            st.error("Delete failed")


# -------------------------------
# ROUTING
# -------------------------------
if not is_logged_in():
    login_page()
else:
    dashboard()

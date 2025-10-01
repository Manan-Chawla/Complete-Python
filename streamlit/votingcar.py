import streamlit as st

st.title("Let's get something new for collection :")
col1, col2 = st.columns(2)

with col1:
    benz = st.button("Vote me for best luxury car 🚘")
    if benz:
        st.success("Thank you for choosing me!")
        st.image(
            "https://www.mercedes-benz.co.in/content/dam/hq/passengercars/cars/amg-gt/amg-gt-2-doors-coupe-c192/overview/highlights/02-2025/images/mercedes-amg-gt-c192-highlights-gt-63-pro-3302x1858-02-2025.jpg/1752732873363.jpg?im=Crop,rect=(722,0,1858,1858);Resize=(800,800)",
            width=300
        )

        # Sidebar content for Benz
        st.sidebar.title("Pros of choosing Benz 🚙")
        with st.sidebar.expander("I'm best in : "):
            st.write("- Reliability")
            st.write("- Engine")
            st.write("- Comfort")

# Sidebar input for Benz (updates live)
benz_model = st.sidebar.text_input(
    "Enter your model to buy from Benz : ",
    key="benz_model"
)
if benz_model:
    st.sidebar.subheader(f"✅ Your Benz model: {benz_model}")




with col2:
    ferrari = st.button("Choose me for the class and speed 🏎️")
    if ferrari:
        st.success("Thanks for choosing the leader!")
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN-PG2pNFHv3sRLlNJRE31HySIr37E7Hmn8A&s",
            width=300
        )

        # Sidebar content for Ferrari
        st.sidebar.title("Pros of choosing Ferrari 🏎️")
        with st.sidebar.expander("I'm best in : "):
            st.write("- Speed")
            st.write("- Looks")
            st.write("- Luxury")
            # Sidebar input for Ferrari (updates live)
            ferrari_model = st.sidebar.text_input(
    "Enter your model to buy from Ferrari : ",
    key="ferrari_model"
)
            if ferrari_model:
                st.sidebar.subheader(f"✅ Your Ferrari model: {ferrari_model}")

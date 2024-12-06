import streamlit as st

# Instructors data
instructors = [
    {'name': 'Fatima Malik', 'subject': 'WordPress Designer & Developer | Physicist',
     'address': 'Okara District, Punjab, Pakistan', 'contact': '7223fatimamalik@gmail.com',
     'linkedin': 'https://www.linkedin.com/in/fatima-malik99/', 'github': 'https://github.com/fatima-malik99',
     'classes': 'Monday, Wednesday, Friday'},
    {'name': 'Sana Raza', 'subject': 'Biomedical Engineer | Technical Content Writer',
     'address': 'Karāchi, Sindh, Pakistan', 'contact': 'sana.raxa321@gmail.com',
     'linkedin': 'https://www.linkedin.com/in/sana-raza-engineer/', 'github': 'https://github.com/Sanarazaaa',
     'classes': 'Monday, Thursday, Saturday'},
    {'name': 'Ubaid Ur Rehman', 'subject': 'Software Engineer | Section Leader',
     'address': 'Islāmābād, Pakistan', 'contact': 'ubaid_ur_Rehman@gmail.com',
     'linkedin': 'https://www.linkedin.com/in/iubaidrmn/', 'github': 'https://github.com/',
     'classes': 'Tuesday, Thursday'},
    {'name': 'Laiba Asif', 'subject': 'Python | AI Enthusiast | Data analyst',
     'address': 'Jhang District, Punjab, Pakistan  ', 'contact': 'laibasif99@gmail.com',
     'linkedin': 'https://www.linkedin.com/in/laiba-asif-8544a0277/', 'github': 'https://github.com/',
     'classes': 'Tuesday, Thursday'}

]

# Function to display all instructors
def display_instructors():
    st.subheader('Our Beloved Python For Beginners Instructors:')
    for idx, instructor in enumerate(instructors, 1):
        st.markdown(f"<p style='font-size: 18px; color: #1e90ff;'><b>{idx}. {instructor['name']}</b></p>", unsafe_allow_html=True)

# Function to display instructor's detailed information
def view_instructors_info(instructor_number):
    instructor = instructors[instructor_number]
    st.markdown(f"<h3 style='color: #ff0000;'>{instructor['name']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 16px; color: #505050;'><b>Subject:</b> {instructor['subject']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 16px; color: #505050;'><b>Address:</b> {instructor['address']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 16px; color: #505050;'><b>Contact:</b> {instructor['contact']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 16px; color: #505050;'><b>LinkedIn:</b> <a href='{instructor['linkedin']}' style='color: #ff6347;'>LinkedIn Profile</a></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 16px; color: #505050;'><b>GitHub:</b> <a href='{instructor['github']}' style='color: #ff6347;'>GitHub Profile</a></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 16px; color: #505050;'><b>Classes:</b> {instructor['classes']}</p>", unsafe_allow_html=True)

# Function to add a new instructor
def add_instructor():
    st.subheader("Add New Instructor")
    name = st.text_input("Instructor's Name", placeholder="Enter Instructor's Full Name")
    subject = st.text_input("Instructor's Subject Specialty", placeholder="Enter Instructor's Subject Specialty")
    address = st.text_input("Instructor's Address", placeholder="Enter Instructor's Address")
    contact = st.text_input("Instructor's Contact Email", placeholder="Enter Instructor's Contact Email")
    linkedin = st.text_input("Instructor's LinkedIn URL", placeholder="Enter Instructor's LinkedIn URL")
    github = st.text_input("Instructor's GitHub URL", placeholder="Enter Instructor's GitHub URL")
    classes = st.text_input("Classes (e.g., 'Monday, Wednesday')", placeholder="Enter the Days for the Classes")

    if st.button("Add Instructor"):
        new_instructor = {
            'name': name,
            'subject': subject,
            'address': address,
            'contact': contact,
            'linkedin': linkedin,
            'github': github,
            'classes': classes
        }
        instructors.append(new_instructor)
        st.success(f"New instructor {name} added successfully!")

# Function to update an existing instructor
def update_instructor(instructor_number):
    st.subheader(f"Update Instructor: {instructors[instructor_number]['name']}")
    name = st.text_input("Instructor's Name", value=instructors[instructor_number]['name'])
    subject = st.text_input("Instructor's Subject Specialty", value=instructors[instructor_number]['subject'])
    address = st.text_input("Instructor's Address", value=instructors[instructor_number]['address'])
    contact = st.text_input("Instructor's Contact Email", value=instructors[instructor_number]['contact'])
    linkedin = st.text_input("Instructor's LinkedIn URL", value=instructors[instructor_number]['linkedin'])
    github = st.text_input("Instructor's GitHub URL", value=instructors[instructor_number]['github'])
    classes = st.text_input("Classes (e.g., 'Monday, Wednesday')", value=instructors[instructor_number]['classes'])

    if st.button("Update Instructor"):
        instructors[instructor_number] = {
            'name': name,
            'subject': subject,
            'address': address,
            'contact': contact,
            'linkedin': linkedin,
            'github': github,
            'classes': classes
        }
        st.success(f"Instructor {name} updated successfully!")

# Streamlit main function
def main():
    st.set_page_config(page_title="Instructors Management System", page_icon="📚", layout="wide")

    # Custom CSS for styling
    st.markdown("""
        <style>
        body {
            background: linear-gradient(145deg, #ff8c00, #ff6347);
            font-family: 'Roboto', sans-serif;
            color: #fff;
        }
        .stButton>button {
            background-color: #ff6347;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 12px 24px;
        }
        .stButton>button:hover {
            background-color: #ff4500;
        }
        .sidebar .sidebar-content {
            background-color: #ff6a00;
            color: #fff;
        }
        .sidebar .sidebar-header {
            color: #fff;
        }
        .stTextInput input {
            background-color: #f5f5f5;
            color: #333;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        h1, h2, h3 {
            color: #ff0000; /* Red color for header */
        }
        .footer {
            font-size: 14px;
            text-align: center;
            color: #ddd;
            margin-top: 30px;
        }
        .footer a {
            color: #ff6347;
            text-decoration: none;
        }
        .footer a:hover {
            color: #ff4500;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Instructors Management System (IMS)")
    st.markdown("---")

    # Sidebar for navigation
    st.sidebar.title("Menu")
    menu = ['View All Instructors', 'View Instructor Details', 'Add New Instructor', 'Update Instructor Details']
    choice = st.sidebar.radio("Select an option", menu)

    if choice == 'View All Instructors':
        display_instructors()

    elif choice == 'View Instructor Details':
        instructor_number = st.number_input("Enter Instructor Number (1-3)", min_value=1, max_value=len(instructors), step=1) - 1
        if instructor_number is not None:
            view_instructors_info(instructor_number)

    elif choice == 'Add New Instructor':
        add_instructor()

    elif choice == 'Update Instructor Details':
        instructor_number = st.number_input("Enter Instructor Number (1-3)", min_value=1, max_value=len(instructors), step=1) - 1
        if instructor_number is not None:
            update_instructor(instructor_number)

    # Footer with developer info
    st.markdown("""
        <div class="footer">
            <p>Developed by: <strong><a href="https://https://www.linkedin.com/in/iukhan/" target="_blank">IRFAN ULLAH KAHN</a></strong></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()

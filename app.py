import streamlit as st

# Instructors data
instructors = [
    {'name': 'Fatima Malik', 'subject': 'WordPress Designer & Developer|Physicist',
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
     'classes': 'Tuesday, Thursday'}
]

# Function to display all instructors
def display_instructors():
    st.subheader('Our Beloved Python For Beginners Instructors:')
    for idx, instructor in enumerate(instructors, 1):
        st.write(f"{idx}. {instructor['name']}")

# Function to display instructor's detailed information
def view_instructors_info(instructor_number):
    instructor = instructors[instructor_number]
    st.write(f"### Name: {instructor['name']}")
    st.write(f"**Subject:** {instructor['subject']}")
    st.write(f"**Address:** {instructor['address']}")
    st.write(f"**Contact:** {instructor['contact']}")
    st.write(f"**LinkedIn:** [{instructor['linkedin']}]({instructor['linkedin']})")
    st.write(f"**GitHub:** [{instructor['github']}]({instructor['github']})")
    st.write(f"**Classes:** {instructor['classes']}")

# Function to add a new instructor
def add_instructor():
    st.subheader("Add New Instructor")

    name = st.text_input("Instructor's Name")
    subject = st.text_input("Instructor's Subject Specialty")
    address = st.text_input("Instructor's Address")
    contact = st.text_input("Instructor's Contact Email")
    linkedin = st.text_input("Instructor's LinkedIn URL")
    github = st.text_input("Instructor's GitHub URL")
    classes = st.text_input("Classes (e.g., 'Monday, Wednesday')")

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
    st.title("Instructors Management System (IMS)")

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

if __name__ == '__main__':
    main()

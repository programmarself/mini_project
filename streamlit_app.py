import streamlit as st
import folium
from streamlit_folium import st_folium

# Sample data for the instructors
instructors = [
    {'name': 'Fatima Malik', 'subject': 'WordPress Designer & Developer | Physicist', 'address': 'Okara District, Punjab, Pakistan'},
    {'name': 'Sana Raza', 'subject': 'Biomedical Engineer | Technical Content Writer', 'address': 'Karāchi, Sindh, Pakistan'},
    {'name': 'Ubaid Ur Rehman', 'subject': 'Software Engineer | Section Leader', 'address': 'Islāmābād, Pakistan'},
    {'name': 'Laiba Asif', 'subject': 'Python | AI Enthusiast | Data analyst', 'address': 'Jhang District, Punjab, Pakistan'}
]

# Function to create a map
def create_map():
    m = folium.Map(location=[30.3753, 69.3451], zoom_start=5)  # Center of Pakistan
    for instructor in instructors:
        folium.Marker(
            location=[30.3753, 69.3451],  # Replace with actual coordinates
            popup=instructor['name'],
        ).add_to(m)
    return m

# Main function
def main():
    st.set_page_config(page_title="Instructor Management System", layout="wide")
    
    # Custom CSS for styling
    st.markdown("""
        <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Arial', sans-serif;
        }
        .header {
            background-color: #0056b3;
            color: white;
            padding: 10px;
            text-align: center;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background-color: #0056b3;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header'><h1>How It Works</h1></div>", unsafe_allow_html=True)
    st.markdown("### To participate in the program and become eligible for the most prestigious credentials for AI, Cloud, and Blockchain in the world, students must complete the following process:")
    st.markdown("1. Sign-up for a PAC. [Click Here](#) for more details.")
    
    st.markdown("### Instructors Available:")
    for instructor in instructors:
        st.write(f"**{instructor['name']}** - {instructor['subject']}")

    # Display the map
    st.markdown("### Locations of Instructors:")
    map_ = create_map()
    st_folium(map_, width=700, height=500)

    # Footer
    st.markdown("<div class='footer'><p>Developed by: <strong>IRFAN ULLAH KAHN</strong></p></div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()

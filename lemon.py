import streamlit as st

# Initialize session state if not already present
if 'total_kilometers' not in st.session_state:
    st.session_state.total_kilometers = {}

# Function to add kilometers for a vehicle type
def add_kilometers(vehicle_type, kilometers):
    if vehicle_type in st.session_state.total_kilometers:
        st.session_state.total_kilometers[vehicle_type] += kilometers
    else:
        st.session_state.total_kilometers[vehicle_type] = kilometers

# Streamlit app title
st.title('Kilometers Tracker')

# Input form for kilometers and vehicle type
with st.form(key='kilometers_form'):
    vehicle_type = st.text_input('Enter vehicle type:', '')
    kilometers = st.number_input('Enter kilometers traveled:', min_value=0.0, step=0.1)
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if vehicle_type:
            add_kilometers(vehicle_type, kilometers)
            st.success(f'Added {kilometers} km to {vehicle_type}.')
        else:
            st.error('Please enter a vehicle type.')

# Display total kilometers traveled for each vehicle type
st.subheader('Total Kilometers Traveled:')
for vehicle, kilometers in st.session_state.total_kilometers.items():
    st.write(f'{vehicle}: {kilometers} km')

# Optional: Reset the data (for testing purposes)
if st.button('Reset Data'):
    st.session_state.total_kilometers = {}
    st.success('Data has been reset.')

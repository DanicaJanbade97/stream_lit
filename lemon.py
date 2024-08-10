import streamlit as st

# Initialize session state if not already present
if 'total_kilometers_vehicle_4w' not in st.session_state:
    st.session_state.total_kilometers_vehicle_4w = 0.0
if 'total_kilometers_vehicle_2w' not in st.session_state:
    st.session_state.total_kilometers_vehicle_2w = 0.0
if 'total_kilometers_steps' not in st.session_state:
    st.session_state.total_kilometers_steps = 0.0

# Function to add kilometers for vehicle or steps
def add_kilometers(mode_of_travel, vehicle_type, kilometers):
    if mode_of_travel == 'Vehicle':
        if vehicle_type == '4-wheeler':
            st.session_state.total_kilometers_vehicle_4w += kilometers
        elif vehicle_type == '2-wheeler':
            st.session_state.total_kilometers_vehicle_2w += kilometers
    elif mode_of_travel == 'Steps':
        st.session_state.total_kilometers_steps += kilometers

# Streamlit app title
st.title('Kilometers Tracker')

# Input form for kilometers and type of travel
with st.form(key='kilometers_form'):
    mode_of_travel = st.selectbox('Select the mode of travel:', ['Vehicle', 'Steps'])
    if mode_of_travel == 'Vehicle':
        vehicle_type = st.selectbox('Select vehicle type:', ['4-wheeler', '2-wheeler'])
    else:
        vehicle_type = None
    kilometers = st.number_input('Enter kilometers traveled:', min_value=0.0, step=0.1)
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if mode_of_travel:
            add_kilometers(mode_of_travel, vehicle_type, kilometers)
            st.success(f'Added {kilometers} km to {mode_of_travel} ({vehicle_type if vehicle_type else ""}).')
        else:
            st.error('Please select a mode of travel.')

# Display total kilometers traveled for vehicle types and steps
st.subheader('Total Kilometers Traveled:')
st.write(f'4-wheeler: {st.session_state.total_kilometers_vehicle_4w} km')
st.write(f'2-wheeler: {st.session_state.total_kilometers_vehicle_2w} km')
st.write(f'Steps: {st.session_state.total_kilometers_steps} km')

# Optional: Reset the data (for testing purposes)
if st.button('Reset Data'):
    st.session_state.total_kilometers_vehicle_4w = 0.0
    st.session_state.total_kilometers_vehicle_2w = 0.0
    st.session_state.total_kilometers_steps = 0.0
    st.success('Data has been reset.')


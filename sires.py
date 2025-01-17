import streamlit as st
import pandas as pd

# Load data
file_path = "top_sires.csv"  # Update with your file path if necessary
data = pd.read_csv(file_path)

# Streamlit App
st.title("Top Sires for Season 24")

# Filters
archetypes = data['archetype'].unique()
selected_archetype = st.multiselect("Select Archetype(s):", options=archetypes, default=archetypes)

min_foals = st.number_input("Minimum Number of Foals:", min_value=5, value=5, step=5)

search_name = st.text_input("Search by Horse Name:").strip().lower()

# Filtered Data
filtered_data = data[(data['archetype'].isin(selected_archetype)) & (data['number_of_foals'] >= min_foals)]

if search_name:
    filtered_data = filtered_data[filtered_data['horse_name'].str.lower().str.contains(search_name)]

# Display Data
st.dataframe(filtered_data)
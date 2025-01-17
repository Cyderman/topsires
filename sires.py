import streamlit as st
import pandas as pd

# Load data
file_path = "top_sires.csv" 
data = pd.read_csv(file_path)

# Streamlit App
st.title("Top Sires for Season 24")

# Filters
archetypes = data['archetype'].unique()
selected_archetype = st.multiselect("Select Archetype(s):", options=archetypes, default=archetypes)

min_foals = st.number_input("Minimum Number of Foals:", min_value=0, value=1, step=1)

search_name = st.text_input("Search by Horse Name:").strip().lower()

# Filtered Data
filtered_data = data[(data['archetype'].isin(selected_archetype)) & (data['foals'] >= min_foals)]

if search_name:
    filtered_data = filtered_data[filtered_data['horse_name'].str.lower().str.contains(search_name)]

# Display Data
if filtered_data.empty:
    st.warning("No results found. Please adjust your filters or search criteria.")
else:
    st.dataframe(filtered_data)
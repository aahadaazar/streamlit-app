import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

# 2 columns
col1, col2 = st.columns(2)


# Load sample dataset
iris = sns.load_dataset("iris")

# Sidebar inputs
st.sidebar.title('Input Params')
unique_species = iris.species.unique()
unique_species = np.concatenate([['All'], unique_species])
species = st.sidebar.selectbox("Select Species", unique_species)

# Filter the data based on the selected species
if (species != 'All'):
    filtered_data = iris[iris.species == species]
else:
    filtered_data = iris

# Scatter plot
scatter_plot = sns.scatterplot(
    data=filtered_data, x="sepal_length", y="sepal_width", hue="species")

# Set plot labels
scatter_plot.set_title("Iris Dataset - Sepal Length vs Sepal Width")
scatter_plot.set_xlabel("Sepal Length")
scatter_plot.set_ylabel("Sepal Width")

# Show the plot
with col1:
    st.pyplot()

# Display the filtered data table
with col2:
    st.dataframe(filtered_data)

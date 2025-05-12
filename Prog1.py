import streamlit as st  # Importing the Streamlit library for creating interactive web applications
import pandas as pd  # Importing pandas for handling CSV file data
import seaborn as sns  # Importing seaborn for data visualization
import matplotlib.pyplot as plt  # Importing matplotlib for plotting

# Set up Streamlit app
st.title("Create a Histogram by Uploading a CSV File")  # Setting the title of the app

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")  # Allowing users to upload a CSV file

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)  # Reading the uploaded CSV file into a pandas DataFrame
    st.success("File uploaded successfully!")  # Displaying a success message after file upload

    # Select numeric columns
    numeric_columns = data.select_dtypes(include=["number"]).columns.tolist()  # Identifying numeric columns in the dataset

    if numeric_columns:
        # Select column for histogram
        selected_column = st.selectbox("Select a column to plot a histogram", numeric_columns)  # Dropdown to select a numeric column

        # Plot histogram
        st.subheader(f"Histogram of {selected_column}")  # Displaying the heading for the histogram
        fig, ax = plt.subplots()  # Creating a matplotlib figure
        sns.histplot(data[selected_column], kde=True, ax=ax)  # Plotting the histogram with Seaborn
        ax.set_title(f"Histogram of {selected_column}", fontsize=16)  # Setting the title of the plot
        ax.set_xlabel(selected_column, fontsize=14)  # Labeling the x-axis
        ax.set_ylabel("Frequency", fontsize=14)  # Labeling the y-axis
        st.pyplot(fig)  # Displaying the plot in the Streamlit app
    else:
        st.warning("No numeric columns found in the uploaded dataset.")  # Warning if no numeric columns are found
else:
    st.info("Please upload a CSV file to start.")  # Informing the user to upload a CSV file to proceed
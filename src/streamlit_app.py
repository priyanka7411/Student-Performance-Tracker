import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from utils import save_to_csv  # Import your custom function for saving the filtered data

# Title of the web app
st.title('Student Performance Tracker')

# Sidebar for better organization of input controls
st.sidebar.header("Upload & Filter Data")

# File uploader to upload CSV files
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Load data into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.write("## Original Data")
    st.dataframe(df.head())  # Display the first few rows of the dataset
    
    # Progress bar to simulate data processing
    with st.spinner('Processing data...'):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
        st.success("Data successfully processed!")
    
    # Sidebar filters
    st.sidebar.subheader("Filter Options")
    
    # Gender filter: Select which gender you want to filter by
    gender_filter = st.sidebar.selectbox("Filter by Gender", df["gender"].unique())
    
    # Filter the data by gender
    filtered_data = df[df["gender"] == gender_filter]
    
    st.write(f"## Filtered Data by {gender_filter}")
    st.dataframe(filtered_data)
    
    # Additional filters based on other columns
    race_filter = st.sidebar.selectbox("Filter by Race/Ethnicity", df["race/ethnicity"].unique())
    education_filter = st.sidebar.selectbox("Filter by Parental Level of Education", df["parental level of education"].unique())
    lunch_filter = st.sidebar.selectbox("Filter by Lunch", df["lunch"].unique())
    test_preparation_filter = st.sidebar.selectbox("Filter by Test Preparation Course", df["test preparation course"].unique())
    
    # Apply all the filters
    filtered_data = filtered_data[
        (filtered_data["race/ethnicity"] == race_filter) &
        (filtered_data["parental level of education"] == education_filter) &
        (filtered_data["lunch"] == lunch_filter) &
        (filtered_data["test preparation course"] == test_preparation_filter)
    ]
    
    st.write(f"## Further Filtered Data")
    st.dataframe(filtered_data)
    
    # Visualization 1: Scatter Plot
    st.subheader(f"Performance of {gender_filter} Students")
    fig = px.scatter(filtered_data, x="math score", y="reading score", color="writing score",
                     title=f"Math vs Reading Scores for {gender_filter} Students",
                     labels={"math score": "Math Score", "reading score": "Reading Score"})
    st.plotly_chart(fig)
    
    # Visualization 2: Bar Chart - Average Scores by Parental Level of Education
    st.subheader("Average Scores by Parental Level of Education")
    avg_scores_education = filtered_data.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axes object
    avg_scores_education.plot(kind="bar", ax=ax)  # Use the ax object
    ax.set_title("Average Scores by Parental Level of Education")
    ax.set_xlabel("Parental Level of Education")
    ax.set_ylabel("Average Score")
    st.pyplot(fig)  # Pass the figure object to st.pyplot()

    # Visualization 3: Histogram - Math Scores Distribution
    st.subheader("Math Scores Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(filtered_data["math score"], kde=True, bins=15, color="skyblue", ax=ax)
    ax.set_title("Distribution of Math Scores")
    ax.set_xlabel("Math Score")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Visualization 4: KDE Plot - Reading Scores Distribution
    st.subheader("Reading Scores Distribution (KDE Plot)")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.kdeplot(filtered_data["reading score"], shade=True, color="green", ax=ax)
    ax.set_title("Density Estimation of Reading Scores")
    ax.set_xlabel("Reading Score")
    ax.set_ylabel("Density")
    st.pyplot(fig)
    
    # Visualization 5: Pie Chart - Gender Distribution
    st.subheader("Gender Distribution of Students")
    gender_dist = filtered_data["gender"].value_counts()
    fig = px.pie(names=gender_dist.index, values=gender_dist.values, title="Gender Distribution")
    st.plotly_chart(fig)
    
    # Save the filtered data as CSV
    if st.button("Save Filtered Data"):
        save_to_csv(filtered_data, "output/filtered_students.csv")
        st.success("Filtered data saved to output/filtered_students.csv")
    
    # Option to download the filtered data directly
    st.download_button(
        label="Download Filtered Data as CSV",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_students.csv",
        mime="text/csv",
    )

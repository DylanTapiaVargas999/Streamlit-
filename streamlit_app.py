import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("📊 Data Explorer with Streamlit")
st.write("Upload your CSV file and explore your data interactively!")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # Summary statistics
    if st.checkbox("Show descriptive statistics"):
        st.write(df.describe())

    # Column selection
    numeric_columns = df.select_dtypes(include=['float64', 'int']).columns.tolist()
    selected_col = st.selectbox("Select numeric column for histogram", numeric_columns)
    
    # Histogram
    if selected_col:
        st.subheader(f"Histogram for {selected_col}")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax)
        st.pyplot(fig)

    # Scatter plot
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("X-axis", numeric_columns, key="x")
    y_axis = st.selectbox("Y-axis", numeric_columns, key="y")
    if x_axis and y_axis:
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax2)
        st.pyplot(fig2)

    # Download processed data
    st.download_button("Download Cleaned CSV", df.to_csv(index=False), "cleaned_data.csv", "text/csv")
else:
    st.warning("👆 Upload a CSV file to begin.")

import streamlit as st
import os

st.title("Download Path Test")

file_path = "./test_file.txt"

st.subheader("Testing Local Path")
st.download_button(
    label="Download Local File",
    data=file_path,
    file_name="downloaded.txt"
)

st.divider()

st.header("2. S3 URI Test")
st.write("Note: This requires 'boto3' and AWS secrets configured.")
s3_uri = "s3://my-test-bucket/data.csv" 

st.download_button(
    label="Download via S3 URI",
    data=s3_uri,
    file_name="s3_test.csv"
)

st.divider()

st.subheader("Testing URL Download")
st.download_button(
    label="Download Streamlit Logo",
    data="https://streamlit.io/images/brand/streamlit-mark-color.png",
    file_name="streamlit_logo.png"
)

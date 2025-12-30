import streamlit as st
import os

st.title("Download Path Test")

file_path = "./test_file.txt"

st.subheader("Testing Local Test")
st.download_button(
    label="Download Local File",
    data=file_path,
    file_name="downloaded.txt"
)

st.divider()

st.header("Download S3 URI Test")
s3_uri = "s3://elevation-tiles-prod/v2/reliability.txt" 
try:
    st.download_button(
        label="Download S3 File",
        data=s3_uri,
        file_name="s3_test.txt"
    )   
except Exception as e:
    st.error(f"Error downloading S3 file: {e}")

st.divider()

st.subheader("Download URL Test")
st.download_button(
    label="Download Streamlit Readme",
    data="http://textfiles.com/100/adventur.txt",
    file_name="test.txt"
)

import streamlit as st
from pytube import YouTube
import os
import platform

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        location=os.path.join(os.path.expanduser("~"), "Downloads")
        video_stream.download(output_path=location)
        st.success("Download complete.")
        
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("YouTube Video Downloader")

    # Get YouTube video URL from user input
    video_url = st.text_input("Enter YouTube Video URL:")
    
    if st.button("Download"):
        if video_url:
            download_video(video_url)
        else:
            st.warning("Please enter a valid YouTube video URL.")

if __name__ == "__main__":
    st.text(f"Operation System  {platform.system()}")
    main()

import os
# from youtube_transcript_api import YouTubeTranscriptApi

folder_path = "/Users/karansingh/learning-accelerator"
file_name = "contentTranscript.txt"
full_path = os.path.join(folder_path, file_name)

os.makedirs(folder_path, exist_ok=True)

with open(full_path, "w") as file:
    file.write("This file is inside a created directory")

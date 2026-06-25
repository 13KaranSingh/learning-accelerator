import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

video_id = "pbsTy5V_pxA"

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(video_id)

formatter = TextFormatter()
transcript_text = formatter.format_transcript(transcript)

print(transcript_text)

folder_path = "/Users/karansingh/learning-accelerator"
file_name = "contentTranscript.txt"
full_path = os.path.join(folder_path, file_name)

os.makedirs(folder_path, exist_ok=True)

# Corrected variable name match
if transcript_text:
    with open(full_path, "w") as file:
        file.write(transcript_text)
    print(f"Transcript successfully saved to {full_path}")

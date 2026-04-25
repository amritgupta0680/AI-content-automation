from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re
import os

def get_youtube_transcript(video_url):
    """Extract clean transcript from YouTube URL"""
    try:
        # Extract video ID
        video_id = video_url.split("v=")[1].split("&")[0]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        formatter = TextFormatter()
        transcript = formatter.format_transcript(transcript_list)
        
        # Clean text
        clean_text = re.sub(r'\n+', ' ', transcript)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        
        return clean_text[:4000]  # Limit length
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

def save_to_knowledge_base(text, filename="data/knowledge_base.txt"):
    """Save text to knowledge base"""
    os.makedirs("data", exist_ok=True)
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n--- NEW DOCUMENT ---\n{text}\n")
    return True

def load_knowledge_base(filename="data/knowledge_base.txt"):
    """Load knowledge base"""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        # Split by document markers
        docs = [doc.strip() for doc in content.split("--- NEW DOCUMENT ---") if doc.strip()]
        return docs
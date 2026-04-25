import os
from groq import Groq  # pip install groq

# Make sure to set:  $env:GROQ_API_KEY = "your_key"  in PowerShell
GROQ_API_KEY = ""

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY environment variable not set. "
                       "Set it in your environment before running the app.")
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# You can change model if you want, but this is a good default.[web:26][web:29]
MODEL_NAME = "llama-3.3-70b-versatile"


def _chat(prompt: str) -> str:
    """Helper to call Groq chat completion API."""
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are an expert content writer and editor.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.7,
        max_completion_tokens=800,
    )
    return completion.choices[0].message.content.strip()


def generate_blog(topic_or_text: str) -> str:
    """
    Generate a well-structured blog.
    topic_or_text: can be a topic, raw text, or YouTube transcript.
    """
    prompt = (
        "Write a detailed, well-structured blog article.\n\n"
        "Requirements:\n"
        "- Clear introduction\n"
        "- 3–5 sections with headings\n"
        "- Practical examples where useful\n"
        "- Short conclusion\n"
        "- Neutral, informative tone\n\n"
        f"Base content / topic:\n{topic_or_text}\n\n"
        "Now write the blog:"
    )
    return _chat(prompt)


def generate_summary(text: str) -> str:
    """Summarize the given text in 4–6 sentences."""
    prompt = (
        "Summarize the following content in 4–6 sentences, clear and concise, "
        "preserving the key ideas:\n\n"
        f"{text}\n\n"
        "Summary:"
    )
    return _chat(prompt)


def generate_social_post(text: str, platform: str = "linkedin") -> str:
    """
    Generate a social media post for a given platform.
    platform: 'linkedin' | 'twitter' | 'instagram'
    """
    if platform == "twitter":
        style = (
            "Write a single tweet under 280 characters. "
            "Include a strong hook, 1–2 relevant hashtags, no emoji spam."
        )
    elif platform == "instagram":
        style = (
            "Write an Instagram caption under 300 characters. "
            "Use 2–4 relevant emojis and a clear call to action."
        )
    else:  # linkedin
        style = (
            "Write a professional LinkedIn post under 700 characters. "
            "Start with a hook, share 2–3 insights, and end with a call to action."
        )

    prompt = (
        f"{style}\n\n"
        "Base content:\n"
        f"{text}\n\n"
        "Post:"
    )
    post = _chat(prompt)

    if platform == "twitter":
        post = post.replace("\n", " ")
        return post[:280]
    return post
import streamlit as st
from generator import generate_blog, generate_summary, generate_social_post
from rag_system import rag
from utils import get_youtube_transcript, save_to_knowledge_base
from ensemble import score_content
from image_gen import create_social_image

st.set_page_config(page_title="AI Content Generator", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main-header {font-size: 3rem; color: #1f77b4; text-align: center;}
.metric-card {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              padding: 1rem; border-radius: 10px; color: white;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🚀 AI Content Generator Pro (Groq)</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Settings")
platform = st.sidebar.selectbox("Social Platform", ["linkedin", "twitter", "instagram"])
add_to_kb = st.sidebar.checkbox("Save to Knowledge Base", True)

# Main input area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📥 Input")
    input_type = st.radio("Choose Input", ["Topic", "YouTube URL"], horizontal=True)

    if input_type == "Topic":
        user_input = st.text_input("Enter topic", "AI in content creation")
    else:
        user_input = st.text_input("YouTube URL", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    generate_clicked = st.button("🎯 Generate Content", type="primary")

# Placeholders for results
blog = ""
summary = ""
social_post = ""
image_path = ""
score = {"total": 0, "length": 0, "relevance": 0, "readability": 0, "structure": 0}

if generate_clicked:
    with st.spinner("Generating your content using Groq..."):
        # 1. Get base text
        if input_type == "YouTube URL":
            base_text = get_youtube_transcript(user_input)
        else:
            base_text = user_input

        # 2. RAG context
        context = rag.retrieve(base_text)
        if context:
            enhanced_prompt = base_text + "\n\nAdditional context:\n" + context
        else:
            enhanced_prompt = base_text

        # 3. Generate blog, summary, social post via Groq
        blog = generate_blog(enhanced_prompt)
        summary = generate_summary(blog)
        social_post = generate_social_post(blog, platform)

        # 4. Image generation
        image_path = create_social_image(social_post, platform)

        # 5. Scoring
        score = score_content(blog, base_text)

        # 6. Save to KB
        if add_to_kb:
            save_to_knowledge_base(enhanced_prompt)

# Results UI
st.header("📊 Generated Content")
colA, colB, colC = st.columns(3)

with colA:
    st.subheader("📝 Blog Post")
    if blog:
        st.write(blog[:2000] + "..." if len(blog) > 2000 else blog)
    else:
        st.write("Content will appear here after generation.")

with colB:
    st.subheader("📋 Summary")
    if summary:
        st.write(summary)
    else:
        st.write("Summary will appear here after generation.")

with colC:
    st.subheader("📱 Social Post")
    if social_post:
        st.write(social_post)
    else:
        st.write("Social post will appear here after generation.")

# Metrics
st.header("📈 Quality Score")
col1m, col2m, col3m, col4m = st.columns(4)
col1m.metric("Total", f"{score['total']:.0f}/100")
col2m.metric("Relevance", f"{score['relevance']:.0f}/25")
col3m.metric("Readability", f"{score['readability']:.0f}/25")
col4m.metric("Length", f"{score['length']:.0f}/25")

# Image
st.header("🖼️ Social Media Image")
if image_path:
    st.image(image_path)
else:
    st.write("Image preview will appear here after generation.")

# RAG status
st.header("🧠 Knowledge Base")
st.info(f"Documents in knowledge base: {len(rag.documents)}")

st.markdown("---")
st.markdown("✅ Powered by Groq Llama 3 for fast, high-quality generation.")
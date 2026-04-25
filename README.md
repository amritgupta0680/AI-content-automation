# 🚀 AI Content Automation Pipeline

An end-to-end AI-powered content generation system that creates blogs, summaries, social media posts, and images from a topic or YouTube link.

Built using LLMs, Retrieval-Augmented Generation (RAG), and a simple image generation pipeline.

---

## ✨ Features

* 📝 Generate full blog articles
* 📄 Create concise summaries
* 📱 Generate social media posts (LinkedIn/Twitter style)
* 🎥 Extract and process YouTube transcripts
* 🧠 RAG-based knowledge storage and retrieval
* 📊 Content quality scoring system
* 🖼️ Automated image generation for posts

---

## 🏗️ Project Architecture

User Input (Topic / YouTube Link)
↓
Streamlit UI (`app.py`)
↓
LLM Generation (`generator.py`)
↓

* RAG System (`rag_system.py`)
* Utilities (`utils.py`)
* Scoring (`ensemble.py`)
  ↓
  Image Generation (`image_gen.py`)
  ↓
  Final Output (Text + Image)

---

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit application (UI + control flow)
├── generator.py        # LLM-based content generation
├── image_gen.py        # Image generation using Pillow
├── rag_system.py       # Retrieval-Augmented Generation system
├── utils.py            # Helper functions (YouTube transcript, storage)
├── ensemble.py         # Content scoring and evaluation
├── clustering.py       # Content grouping and organization
├── requirements.txt    # Dependencies
```

---

## 🧠 How It Works

### 1. Input

* User provides a topic OR a YouTube URL

### 2. Processing

* Transcript is extracted (if YouTube link)
* Input is sent to LLM (via Groq API)

### 3. Generation

* Blog
* Summary
* Social media post

### 4. Enhancement

* RAG system retrieves relevant stored knowledge
* Ensemble model scores content quality

### 5. Image Creation

* A post image is generated using Pillow

---

## 🖼️ Image Generation Details

This project uses **Pillow (PIL)** for image generation.

### Approach:

* Creates a blank canvas
* Adds background color
* Renders text using fonts
* Saves as PNG

⚠️ Note:
This is **template-based image generation**, not AI image generation (like DALL·E or Stable Diffusion).

---

## ⚙️ Tech Stack

* Python
* Streamlit
* Groq API (LLM inference)
* Pillow (Image Processing)
* RAG (custom implementation)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📊 Example Use Cases

* Content creators
* Bloggers
* Social media managers
* Marketing teams
* AI experimentation projects

---

## 🚧 Future Improvements

* Integrate AI image generation (DALL·E / Stable Diffusion)
* Add multi-language support
* Improve RAG with vector databases
* Add export options (PDF, DOCX)
* UI enhancements

---

# 🎬 Celebrity Detector & Q&A 🤖

This project combines state-of-the-art **Large Language Models (LLMs)** to deliver an intelligent celebrity recognition and question-answering web app.

## 🌟 Overview

The app leverages **vision transformer-powered LLMs** (specifically Meta’s LLaMA 4 Scout 17B Instruct model hosted via Groq's API) to:

- 🖼️ **Recognize celebrities** in user-uploaded images by analyzing visual input and generating structured textual information.
- 💬 **Answer user questions** about the detected celebrity using natural language processing, providing concise, accurate, and context-aware responses.

## 📸 Screenshots

Here are some example snapshots of the app in action:

### 🔍 Celebrity Detection and Q&A

![Celebrity Detection Screenshot](images/ar.png)

### 
Ask questions and get concise, LLM-powered answers:
![Celebrity Q&A Screenshot](images/njr.png)



## 🚀 Key Features

- 🤝 **Vision-Language Integration:** The model processes both image and text input by embedding the uploaded image in a prompt, allowing joint understanding.
- 🎭 **Celebrity Recognition:** The LLM identifies the person in the image and outputs detailed structured information (name, profession, nationality, achievements).
- ❓ **Conversational Q&A:** Users can ask follow-up questions about the recognized celebrity, which the LLM answers using a tailored prompt to ensure accuracy and relevance.
- 👁️‍🗨️ **Face Detection Preprocessing:** OpenCV’s Haar cascade detects faces, focusing recognition on the largest face to improve LLM input quality.

## 🏗️ Architecture

- 🌐 **Frontend:** A React/Flask web interface allows image upload and interaction.
- ⚙️ **Backend:**
  - `image_handler.py` preprocesses images and detects faces.
  - `celebrity_detector.py` sends images to the Groq API with the vision transformer LLM for celebrity identification.
  - `qa_engine.py` uses the same LLM to answer questions about the detected celebrity.
- 🤖 **LLM Model:** Uses the `meta-llama/llama-4-maverick-17b-128e-instruct` model, a vision-capable transformer with strong NLP abilities, enabling multimodal understanding.

## 🛠️ Installation & Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/celebrity-detector-qa.git
   cd celebrity-detector-qa
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Add your Groq API key to a `.env` file:

   ```
   GROQ_API_KEY=your_api_key_here

   ```
4. Run the app:

   ```bash
   python app.py
   ```
5. Visit `http://localhost:5000` in your browser.

## 🎯 Usage

* Upload an image containing a celebrity’s face.
* The system detects and highlights the largest face.
* The vision transformer LLM processes the image and returns detailed information about the celebrity.
* Ask follow-up questions in natural language; the LLM answers them based on the celebrity context.

## 🔧 Technologies

* 🤖 **Large Language Model:** Meta LLaMA 4 Maverick 17B with vision capabilities
* ☁️ **API Hosting:** Groq AI API for multimodal LLM inference
* 🖥️ **Computer Vision:** OpenCV for face detection preprocessing
* 🐍 **Backend Framework:** Flask
* 🎨 **Frontend Styling:** Tailwind CSS

## 🌱 Future Improvements


* 👥 Add support for multiple faces per image with multi-identity recognition.
* 🗣️ Implement context-aware multi-turn conversational Q\&A.
* 🛡️ Improve response safety and moderation in Q\&A.

---


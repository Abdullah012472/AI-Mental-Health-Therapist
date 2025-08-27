# 🧠 AI Mental Health Therapist

An AI-powered mental health assistant that provides supportive conversations, locates nearby therapists and can place emergency calls when needed.  

This project integrates **LLMs (Gemini, MedGemma)** with **LangChain, LangGraph, Twilio, and Streamlit** to create a safe, real-time mental health chatbot.  


## 🚀 Features
- 🤝 **AI Chat Support** – Empathetic, therapeutic responses powered by MedGemma & Gemini.  
- 📍 **Find Nearby Therapists** – Uses Google Maps API to recommend professionals in the user’s area.  
- 📞 **Emergency Support** – Twilio integration for initiating emergency calls.  
- 🖥️ **User-Friendly Interface** – Streamlit frontend with chat-like interaction.  
- ⚡ **Fast & Scalable** – FastAPI backend with agent-based architecture (LangChain + LangGraph).  


## ⚙️ Setup & Installation
1. **Clone the repo**  
   ```bash
   https://github.com/Abdullah012472/AI-Mental-Health-Therapist.git
   cd AI-Mental-Health-Therapist
   ```
2. **Create virtual environment & install dependencies**
    ```bash
    uv venv
    uv sync
    ```
3. **Add your environment variables in .env**
    ```bash
    GEMINI_API_KEY=your_gemini_api_key
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_FROM_NUMBER=+123456789
    EMERGENCY_CONTACT=+112
    ```

4. **Run the backend (FastAPI)**
    ```bash
    uv run backend/main.py
    ```
5. **Run the frontend (Streamlit)**
    ```bash
    uv run streamlit run frontend.py
    ```





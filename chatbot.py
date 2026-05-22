from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os
import time

# =========================================================
# LOAD ENV
# =========================================================

load_dotenv()

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="🚀 Smart AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
MAIN BACKGROUND
========================================================= */

.stApp {
    background: linear-gradient(
        135deg,
        #0F172A,
        #1E1B4B,
        #312E81,
        #7E22CE
    );
    color: white;
}

/* =========================================================
REMOVE HEADER
========================================================= */

header {
    background: transparent !important;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #111827,
        #1E1B4B
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Sidebar Text */

[data-testid="stSidebar"] * {
    color: white;
}

/* =========================================================
TITLE
========================================================= */

.main-title {

    text-align: center;

    font-size: 60px;

    font-weight: bold;

    color: #F472B6;

    margin-top: 10px;

    margin-bottom: 10px;

    text-shadow: 0 0 15px rgba(244,114,182,0.5);
}

/* =========================================================
SUBTITLE
========================================================= */

.sub-title {

    text-align: center;

    color: #E5E7EB;

    font-size: 18px;

    margin-bottom: 35px;
}

/* =========================================================
CHAT MESSAGE
========================================================= */

.stChatMessage {

    background: rgba(255,255,255,0.06);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 18px;

    border-radius: 18px;

    margin-bottom: 18px;

    overflow-wrap: break-word;

    word-break: break-word;

    white-space: pre-wrap;

    line-height: 1.8;

    font-size: 16px;

    box-shadow: 0 4px 15px rgba(0,0,0,0.25);
}

/* =========================================================
CHAT INPUT
========================================================= */

.stChatInput {

    background: rgba(255,255,255,0.05);

    border-radius: 16px;

    border: 1px solid rgba(255,255,255,0.08);

    padding: 8px;

    margin-top: 20px;
}

/* =========================================================
INPUT BOX
========================================================= */

.stChatInput input {

    background-color: #111827 !important;

    color: white !important;

    border-radius: 14px !important;

    border: 1px solid #8B5CF6 !important;

    padding: 14px !important;

    font-size: 16px !important;
}

/* =========================================================
PLACEHOLDER
========================================================= */

.stChatInput input::placeholder {

    color: #9CA3AF !important;
}

/* =========================================================
SEND BUTTON
========================================================= */

.stChatInput button {

    background: linear-gradient(
        to right,
        #8B5CF6,
        #EC4899
    ) !important;

    color: white !important;

    border-radius: 12px !important;

    border: none !important;
}

/* =========================================================
BUTTONS
========================================================= */

.stButton>button {

    width: 100%;

    background: linear-gradient(
        to right,
        #8B5CF6,
        #EC4899
    );

    color: white;

    border-radius: 12px;

    height: 3em;

    border: none;

    font-size: 16px;

    font-weight: bold;

    transition: 0.3s ease;
}

/* Hover */

.stButton>button:hover {

    transform: scale(1.03);

    background: linear-gradient(
        to right,
        #7C3AED,
        #DB2777
    );
}

/* =========================================================
SELECTBOX
========================================================= */

.stSelectbox div[data-baseweb="select"] {

    background-color: #111827;

    border-radius: 12px;

    border: 1px solid #8B5CF6;
}

/* =========================================================
FOOTER
========================================================= */

.footer {

    text-align: center;

    color: #D1D5DB;

    margin-top: 35px;

    font-size: 15px;

    opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.title("⚙️ AI Assistant Panel")

    st.markdown("---")

    selected_model = st.selectbox(
        "🌐 Select AI Model",
        [
            "llama-3.1-8b-instant",
            "llama-3.3-70b-versatile",
            "gemma2-9b-it",
            "mixtral-8x7b-32768",
            "deepseek-r1-distill-llama-70b"
        ]
    )

    temperature = st.slider(
        "🌡️ Temperature",
        0.0,
        1.0,
        0.7
    )

    st.markdown("---")

    st.subheader("🚀 Features")

    st.write("✅ Multi AI Models")
    st.write("✅ Streaming Response")
    st.write("✅ Typing Animation")
    st.write("✅ Chat Memory")
    st.write("✅ Professional UI")
    st.write("✅ Structured Answers")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_llm(model_name, temp):

    return ChatGroq(
        model=model_name,
        temperature=temp
    )

llm = load_llm(selected_model, temperature)

# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<h1 class="main-title">✨ Multi-Model AI Assistant</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Powered by Groq + LangChain + Streamlit</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="footer">
🌟 Built with Groq + LangChain + Streamlit <br>
⚡ Fast · Smart · Professional AI Assistant
</div>
""", unsafe_allow_html=True)

# =========================================================
# SYSTEM PROMPT
# =========================================================

system_prompt = """
You are a smart AI learning assistant.

Always answer in this format:

📌 Topic Overview
- Short explanation of the topic

🧠 Step-by-Step Explanation
1. Step one explanation
2. Step two explanation
3. Step three explanation

💻 Example
- Give simple code examples when needed

✅ Final Summary
- Short conclusion

Rules:
- Explain like a teacher
- Use simple beginner-friendly language
- Use bullet points and emojis
- Keep answers clean and structured
"""

# =========================================================
# CHAT HISTORY
# =========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================================================
# DISPLAY CHAT
# =========================================================

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================================================
# USER INPUT
# =========================================================

user_prompt = st.chat_input("💬 Ask your AI assistant anything...")

# =========================================================
# AI RESPONSE
# =========================================================

if user_prompt:

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        full_response = ""

        try:

            with st.spinner("🤖 Thinking..."):

                stream = llm.stream(
                    [
                        {
                            "role": "system",
                            "content": system_prompt
                        },

                        *st.session_state.chat_history
                    ]
                )

                for chunk in stream:

                    if chunk.content:

                        full_response += chunk.content

                        time.sleep(0.01)

                        message_placeholder.markdown(
                            full_response + "▌"
                        )

                message_placeholder.markdown(full_response)

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )

        except Exception as e:

            st.error(f"❌ Error: {e}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
Made with ❤️ using Streamlit + Groq + LangChain
</div>
""", unsafe_allow_html=True)
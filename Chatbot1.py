import streamlit as st
import ollama
import time

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            font-family: 'Arial', sans-serif;
        }
        .chat-container {
            max-width: 700px;
            margin: auto;
            padding: 10px;
            border-radius: 10px;
        }
        .user-message {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 10px;
            text-align: right;
            margin-bottom: 10px;
        }
        .bot-message {
            background-color: #2196F3;
            color: white;
            padding: 10px;
            border-radius: 10px;
            text-align: left;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center;'>🤖 Ollama AI Chatbot \n (DeepSeek)</h1>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    role = "user-message" if message["role"] == "user" else "bot-message"
    st.markdown(f'<div class="{role}">{message["content"]}</div>', unsafe_allow_html=True)

# User input
user_input = st.chat_input("💡 Ask me anything...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

    # Simulate typing effect
    with st.spinner("🤖 Thinking..."):
        time.sleep(1.5)
        response = ollama.chat(model="deepseek-r1:8b", messages=st.session_state.messages)
        bot_reply = response["message"]["content"]
    
    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.markdown(f'<div class="bot-message">{bot_reply}</div>', unsafe_allow_html=True)












    

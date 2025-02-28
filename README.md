# Chatbot-Deepseek-
CHATBOT
Building an Interactive AI with DeepSeek and Streamlit
Introduction:
The development of conversational AI has revolutionized human-computer interaction, enabling seamless and intuitive communication. This document outlines the creation of a chatbot using the DeepSeek language model, integrated with a user-friendly interface powered by Streamlit. This project demonstrates the practical application of large language models (LLMs) in building interactive and engaging chatbot experiences.
We will explore the implementation of the chatbot, focusing on the integration of DeepSeek via Ollama, the design of the Streamlit interface, and the handling of user interactions. This project aims to provide a clear understanding of how to build and deploy a functional chatbot using modern AI tools.
1. Technology Stack:
●	DeepSeek: A powerful language model used for generating conversational responses.
●	Ollama: A tool that enables running LLMs locally, providing an interface to interact with DeepSeek.
●	Streamlit: A Python library used to create interactive web applications for the chatbot's front-end.
●	Python: The programming language used for the chatbot's implementation.
2. Implementation Details:
●	Setting up the Environment:
○	Ensure that Ollama is installed and the DeepSeek model ("deepseek-r1:8b") is downloaded.
○	Install the necessary Python libraries: streamlit and ollama.
●	Streamlit Interface:
○	The Streamlit application is designed with a clean and intuitive user interface.
○	Custom CSS is used to style the chat interface, providing a visually appealing experience.
○	The st.markdown function is used to render HTML content, enabling custom styling and formatting.
○	The application includes a title, chat input, and chat display area.
●	Chat Interaction:
○	The st.chat_input function is used to capture user input.
○	User messages and bot responses are stored in st.session_state.messages to maintain chat history.
○	Messages are displayed in the chat display area using st.markdown and custom CSS classes (user-message and bot-message).
○	Ollama is used to make a request to the Deepseek model.
○	The Deepseek model returns a response.
○	A simulated typing effect is implemented using st.spinner and time.sleep to enhance the user experience.
●	DeepSeek Integration:
○	The ollama.chat function is used to send user messages to the DeepSeek model.
○	The model's response is extracted and displayed in the chat display area.
●	Chat History Management:
○	The st.session_state.messages list is used to store the chat history, ensuring that the conversation context is maintained.
○	This allows the model to have some memory of the current conversation.
3. Code Snippets (Illustrative):
●	Ollama Integration:
Python
response = ollama.chat(model="deepseek-r1:8b", messages=st.session_state.messages)
bot_reply = response["message"]["content"]

●	Streamlit Chat Display:
Python
st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="bot-message">{bot_reply}</div>', unsafe_allow_html=True)

●	Streamlit Chat Input:
Python
user_input = st.chat_input("💡 Ask me anything...")
 
4. User Experience:
●	The chatbot provides a seamless and interactive conversational experience.
●	The simulated typing effect enhances the feeling of real-time interaction.
●	The styled interface contributes to a visually appealing and engaging user experience.


Conclusion:
This project demonstrates the creation of a functional and engaging chatbot using the DeepSeek language model and Streamlit. The integration of these technologies enables the development of interactive conversational AI applications. The chatbot's design and implementation highlight the power of LLMs in building user-friendly and intelligent interfaces. The use of Streamlit simplifies the front-end development process, allowing developers to focus on the core functionality of the chatbot. This project serves as a practical example of how to leverage modern AI tools to create interactive and engaging chatbot experiences.

# ChatGuru - AI Chatbot using LangChain & Ollama

## Overview

ChatGuru is an AI-powered conversational chatbot built using Streamlit, LangChain, and Ollama. The application leverages the Gemma 2B Large Language Model (LLM) to provide intelligent, context-aware responses to user queries through a simple and interactive web interface.

The chatbot runs locally using Ollama, eliminating the need for external API keys while ensuring fast and secure conversations.

## Features

* Interactive chat interface built with Streamlit
* Powered by Gemma 2B model via Ollama
* Prompt engineering using LangChain
* Real-time AI-generated responses
* Conversation history tracking
* Lightweight and easy to run locally
* No external API dependency

## Technologies Used

* Python
* Streamlit
* LangChain
* Ollama
* Gemma 2B
* LangChain Core
* LangChain Community

## Project Structure

```text
ChatGuru/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd ChatGuru
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama from its official website.

### Pull the Gemma Model

```bash
ollama pull gemma2:2b
```

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

1. User enters a question.
2. LangChain formats the prompt.
3. Ollama sends the prompt to the Gemma 2B model.
4. The model generates a response.
5. The response is displayed in the Streamlit interface.
6. Previous conversations are stored and displayed in the sidebar.

## Future Enhancements

* Multi-turn conversation memory
* Voice input support
* Document-based question answering
* Multiple LLM support
* Chat export functionality
* User authentication

## Author

Mohini Navghare

## License

This project is developed for educational and learning purposes.

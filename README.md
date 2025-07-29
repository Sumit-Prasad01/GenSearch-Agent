# GenSearch-Agent

# 🔎 LangChain Chat with Search

A powerful conversational AI chatbot built with LangChain and Streamlit that can search the web, query academic papers, and access Wikipedia information in real-time.

## ✨ Features

- **Multi-Source Search**: Integrates DuckDuckGo web search, ArXiv academic papers, and Wikipedia
- **Real-time Streaming**: Powered by Groq's Llama3-8b-8192 model with streaming responses
- **Interactive UI**: Clean Streamlit interface with chat history
- **Agent-based Architecture**: Uses LangChain's ZERO_SHOT_REACT_DESCRIPTION agent for intelligent tool selection
- **Object-Oriented Design**: Clean, maintainable code structure with separation of concerns

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Groq API Key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd langchain-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (Optional)
   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
langchain>=0.0.350
langchain-groq>=0.1.0
langchain-community>=0.0.10
python-dotenv>=1.0.0
arxiv>=1.4.0
wikipedia>=1.4.0
duckduckgo-search>=3.9.0
```

## 🏗️ Architecture

The application follows a clean object-oriented architecture:

```
LangChainChatBot (Main Controller)
├── StreamlitUI (User Interface)
├── ChatSession (Session Management)
├── SearchTools (Tool Management)
└── LLMAgent (AI Agent Operations)
```

### Class Overview

- **`SearchTools`**: Manages initialization and access to search tools
- **`ChatSession`**: Handles message storage and session state
- **`LLMAgent`**: Manages LLM and agent operations
- **`StreamlitUI`**: Handles all UI components and interactions
- **`LangChainChatBot`**: Main orchestrator class

## 🛠️ Usage

1. **Launch the application**
   ```bash
   streamlit run app.py
   ```

2. **Enter your Groq API Key** in the sidebar

3. **Start chatting!** Ask questions like:
   - "What is machine learning?"
   - "Find recent papers about quantum computing"
   - "Search for information about climate change"
   - "Explain the latest developments in AI"

## 🔧 Configuration

### Search Tools Configuration

You can modify the search tools configuration in the `SearchTools` class:

```python
# Arxiv configuration
arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=1,           # Number of results
    doc_content_chars_max=200  # Max characters per result
)

# Wikipedia configuration
wiki_wrapper = WikipediaAPIWrapper(
    top_k_results=1,           # Number of results
    doc_content_chars_max=200  # Max characters per result
)
```

### LLM Configuration

Modify the LLM settings in the `LLMAgent` class:

```python
self.llm = ChatGroq(
    groq_api_key=self.api_key,
    model_name="Llama3-8b-8192",  # Change model here
    streaming=True                 # Enable/disable streaming
)
```

## 📁 Project Structure

```
langchain-chatbot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (optional)
├── README.md             # This file
└── .gitignore           # Git ignore file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Install missing dependencies
pip install langchain-groq langchain-community
```

**2. API Key Issues**
- Ensure your Groq API key is valid
- Check if the key is properly entered in the sidebar
- Verify API rate limits haven't been exceeded

**3. Search Tool Errors**
```bash
# Update search dependencies
pip install --upgrade duckduckgo-search arxiv wikipedia
```

**4. Streamlit Issues**
```bash
# Clear Streamlit cache
streamlit cache clear
```

## 🔗 Useful Links

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Documentation](https://console.groq.com/docs)
- [ArXiv API](https://arxiv.org/help/api)



import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv


class SearchTools:
    """Class to manage and initialize search tools"""
    
    def __init__(self):
        self.tools = self._initialize_tools()
    
    def _initialize_tools(self):
        """Initialize all search tools"""
        # Arxiv tool
        arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
        arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
        
        # Wikipedia tool
        wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
        wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)
        
        # DuckDuckGo search tool
        search = DuckDuckGoSearchRun(name="Search")
        
        return [search, arxiv, wiki]
    
    def get_tools(self):
        """Return list of initialized tools"""
        return self.tools


class ChatSession:
    """Class to manage chat session state"""
    
    def __init__(self):
        self._initialize_session()
    
    def _initialize_session(self):
        """Initialize session state for messages"""
        if "messages" not in st.session_state:
            st.session_state["messages"] = [
                {"role": "assisstant", "content": "Hi,I'm a chatbot who can search the web. How can I help you?"}
            ]
    
    def add_message(self, role, content):
        """Add a message to the session state"""
        st.session_state.messages.append({"role": role, "content": content})
    
    def get_messages(self):
        """Get all messages from session state"""
        return st.session_state.messages
    
    def display_messages(self):
        """Display all messages in the chat interface"""
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg['content'])


class LLMAgent:
    """Class to manage LLM and agent operations"""
    
    def __init__(self, api_key, tools):
        self.api_key = api_key
        self.tools = tools
        self.llm = None
        self.agent = None
        self._initialize_llm()
        self._initialize_agent()
    
    def _initialize_llm(self):
        """Initialize the LLM with Groq"""
        self.llm = ChatGroq(
            groq_api_key=self.api_key,
            model_name="Llama3-8b-8192",
            streaming=True
        )
    
    def _initialize_agent(self):
        """Initialize the search agent"""
        self.agent = initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handling_parsing_errors=True
        )
    
    def run_agent(self, messages, callback_handler):
        """Run the agent with given messages and callback"""
        return self.agent.run(messages, callbacks=[callback_handler])


class StreamlitUI:
    """Class to manage Streamlit UI components"""
    
    def __init__(self):
        self.api_key = None
    
    def setup_page(self):
        """Setup the main page layout"""
        st.title("🔎 LangChain - Chat with search")
    
    def setup_sidebar(self):
        """Setup sidebar for settings"""
        st.sidebar.title("Settings")
        self.api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")
        return self.api_key
    
    def get_user_input(self):
        """Get user input from chat interface"""
        return st.chat_input(placeholder="Ask Anything...............")
    
    def display_user_message(self, prompt):
        """Display user message in chat"""
        st.chat_message("user").write(prompt)
    
    def create_assistant_response_container(self):
        """Create container for assistant response"""
        return st.chat_message("assistant")
    
    def write_response(self, response):
        """Write the final response"""
        st.write(response)


class LangChainChatBot:
    """Main chatbot application class"""
    
    def __init__(self):
        self.ui = StreamlitUI()
        self.chat_session = ChatSession()
        self.search_tools = SearchTools()
    
    def run(self):
        """Main application run method"""
        # Setup UI
        self.ui.setup_page()
        api_key = self.ui.setup_sidebar()
        
        # Display existing messages
        self.chat_session.display_messages()
        
        # Handle user input
        if prompt := self.ui.get_user_input():
            # Add user message to session
            self.chat_session.add_message("user", prompt)
            self.ui.display_user_message(prompt)
            
            # Initialize LLM agent
            llm_agent = LLMAgent(api_key, self.search_tools.get_tools())
            
            # Generate response
            with self.ui.create_assistant_response_container():
                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = llm_agent.run_agent(self.chat_session.get_messages(), st_cb)
                
                # Add assistant response to session and display
                self.chat_session.add_message('assistant', response)
                self.ui.write_response(response)


# Application entry point
if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Create and run the chatbot
    chatbot = LangChainChatBot()
    chatbot.run()
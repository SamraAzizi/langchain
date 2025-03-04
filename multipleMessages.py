
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the chat model
chat = ChatOpenAI(openai_api_key=api_key)

# Create a conversation history
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello!"),
    AIMessage(content="Hi! How can I assist you today?"),
    HumanMessage(content="Can you tell me a joke?"),
]

# Get a response based on the conversation history
response = chat(messages)

# Print the response
print(response.content)

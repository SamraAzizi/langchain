from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the chat model
chat = ChatOpenAI(openai_api_key=api_key)

# Generate a response
response = chat.predict("What is the capital of France?")
print(response)


api_key = os.getenv(

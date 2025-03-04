
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the chat model
chat = ChatOpenAI(openai_api_key=api_key)

# Define a prompt template
template = PromptTemplate(
    input_variables=["topic"],
    template="Can you provide a brief explanation about {topic}?"
)

# Format the prompt with a specific topic
formatted_prompt = template.format(topic="Machine Learning")

# Get AI response
response = chat.predict(formatted_prompt)

# Print the response
print(response)

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

# Define a prompt template for translation
translation_prompt = PromptTemplate(
    input_variables=["text", "language"],
    template="Translate the following English text to {language}: \"{text}\""
)

# Example usage
english_text = "Hello, how are you?"
target_language = "Spanish"

# Format the prompt with the given text and language
formatted_prompt = translation_prompt.format(text=english_text, language=target_language)

# Get AI response
response = chat.predict(formatted_prompt)

# Print the translated text
print(response)

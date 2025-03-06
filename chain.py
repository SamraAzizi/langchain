from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI chat model
chat_model = ChatOpenAI(openai_api_key=api_key)

# Define a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are an AI assistant. Answer the following question: {question}"
)

# Create a chain that connects the prompt to the model
chain = LLMChain(llm=chat_model, prompt=prompt)

# Example question
question = "What is the capital of France?"

# Run the chain
response = chain.run(question)

# Print the output
print(response)

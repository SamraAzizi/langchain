from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the OpenAI API key


api_key = os.getenv("OPENAI_API_KEY")

# Initialize the chat model
chat = ChatOpenAI(openai_api_key=api_key)

# Define the expected structured output using ResponseSchema
response_schemas = [
    ResponseSchema(name="solution", description="The final answer to the math problem."),
    ResponseSchema(name="steps", description="Step-by-step solution (if allowed)."),
]

# Create an Output Parser
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Create a prompt template with output instructions
prompt_template = PromptTemplate(
    input_variables=["problem", "show_steps"],
    template=(
        "Solve the following math problem: {problem}\n"
        "{% if show_steps %} Show the solution with steps.{% else %} Show only the final answer.{% endif %}\n"
        "{format_instructions}"

print(parsed_output)

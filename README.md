#  LangChain Examples  

This repository contains multiple examples demonstrating how to use **LangChain** for various tasks, such as:  
 Basic Chat Model Usage  
 Multi-turn Conversations  
 Prompt Templates  
 Output Parsing (Math Solver)  
 Creating a Chain  

##  Installation  

Before running the examples, install the required dependencies:  

```bash
pip install langchain openai python-dotenv
```
Also, create a .env file and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-api-key-here
```

# Project Structure

📁 simpleExample.py → Basic usage of LangChain's Chat Model
📁 multiMessages.py → Handling multiple messages in a conversation
📁 promptTemplate.py → Using a prompt template for language translation
📁 outputParser.py → Solving math problems with optional step-by-step solutions
📁 chain.py → Creating a simple LangChain pipeline

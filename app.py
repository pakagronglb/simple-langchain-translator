from typing import List
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

# 1. Create prompt template
system_template = 'Translate the following into {target_language}:'
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model - explicitly pass API key
model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser

# create FastAPI app
app = FastAPI(
  title='LangChain Server',
  version='1.0',
  description='A simple API server using LangChain\'s Runnable interfaces',
)

# Adding a root endpoint
@app.get('/')
async def read_root():
    return {'message': 'This is the home page of the LangChain Server!'}

add_routes(
    app,
    chain,
    path='/chain',
)

if __name__ == '__main__':
    import uvicorn
    
    # Change host to '0.0.0.0' to allow external access
    # Remove port specification to allow platform to set it
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", 8000)))
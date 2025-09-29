from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import Client

load_dotenv()

# Simple one-line prompt
client = Client()

prompt = PromptTemplate.from_template("{question}")   # is equivalent to PromptTemplate(input_variable=["question"], template="{question}")

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of india?"})
print(result)

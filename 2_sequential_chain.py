from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['LANGCHAIN_PROJECT'] = 'Sequential LLM APP'

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model1 = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash', temperature = 0.7)
model2 = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash-lite', temperature = 0.5)

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

config = {
    'run_name': 'sequential chain',
    'tags' : ['llm app', 'report generation', 'summerization'],
    'metadata': {'model1': 'gemini-2.5-flash', 'model_temp': 0.7, 'parser': 'stroutputparser'}
}

result = chain.invoke({'topic': 'Unemployment in India'}, config = config)

print(result)

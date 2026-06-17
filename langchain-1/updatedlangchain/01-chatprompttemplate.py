import os
from langchain_classic.prompts.chat import ChatPromptTemplate
from langchain.chat_models import init_chat_model
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
 
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model("google_genai:gemini-2.5-flash")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Agile Coach. Answer any questions about Agile processes."),
        ("human", "{input}")
    ]
)

st.title("Agile Guide")

user_input = st.text_input("Enter the question:")
chain = prompt_template | llm

if user_input:
    response = chain.invoke({"input": user_input})
    st.write(response.content)
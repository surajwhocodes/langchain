import os
# from langchain.prompts  import ChatPromptTemplate , MessagesPlaceholder
from langchain_classic.prompts.chat import ChatPromptTemplate , MessagesPlaceholder
from langchain.chat_models import init_chat_model
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import  StreamlitChatMessageHistory
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
 
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model("google_genai:gemini-2.5-flash")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Agile Coach. Answer any questions about Agile processes."),
        MessagesPlaceholder(variable_name="chat_hitory"),
        ("human", "{input}")
    ]
)

st.title("Agile Guide")

chain = prompt_template | llm

history_for_chain = StreamlitChatMessageHistory()
print("Agile Guide")
input = st.text_input("Enter the question")

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)


# while True:
    # question = input("Enter the question")
if input:
    response = chain_with_history.invoke({"input": input},{"configurable":{"session_id":"abc123"}})
    st.write(response.content)
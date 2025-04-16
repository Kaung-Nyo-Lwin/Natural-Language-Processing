import torch
from langchain import PromptTemplate
from langchain.vectorstores import FAISS
import os
from langchain_groq import ChatGroq
import InstructorEmbedding
import huggingface_hub
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ChatMessageHistory
from langchain.chains import LLMChain
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import ConversationalRetrievalChain



# prompt_template = """
#     I know about Kaung Nyo Lwin. You can ask me about him.
#     {context}
#     Question: {question}
#     Answer:
#     """.strip()

# PROMPT = PromptTemplate.from_template(
#     template = prompt_template
# )

# history = ChatMessageHistory()

# model_name = 'hkunlp/instructor-base'

# embedding_model = HuggingFaceInstructEmbeddings(
#     model_name = model_name,
#     # model_kwargs = {"device" : device}
# )

# vector_path = './vector-store'
# db_file_name = 'a6'

# vectordb = FAISS.load_local(
#     folder_path = os.path.join(vector_path, db_file_name),
#     embeddings = embedding_model,
#     index_name = 'a6', #default index
#     allow_dangerous_deserialization=True
# )   

# retriever = vectordb.as_retriever()

# if "GROQ_API_KEY" not in os.environ:
#     os.environ["GROQ_API_KEY"] = "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"

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # other params...
# )

# question_generator = LLMChain(
#     llm = llm,
#     prompt = CONDENSE_QUESTION_PROMPT,
#     verbose = True
# )

# memory = ConversationBufferWindowMemory(
#     k=3, 
#     memory_key = "chat_history",
#     return_messages = True,
#     output_key = 'answer'
# )
# doc_chain = load_qa_chain(
#     llm = llm,
#     chain_type = 'stuff',
#     prompt = PROMPT,
#     verbose = True
# )

# chain = ConversationalRetrievalChain(
#     retriever=retriever,
#     question_generator=question_generator,
#     combine_docs_chain=doc_chain,
#     return_source_documents=True,
#     memory=memory,
#     verbose=True,
#     get_chat_history=lambda h : h
# )

# prompt_question = "Who are you by the way?"
# answer = chain({"question":prompt_question})
# answer['answer']

class Chatbot():
                        
    def __init__(self):
                
        self.prompt_template = """
            I know about Kaung Nyo Lwin. You can ask me about him.
            {context}
            Question: {question}
            Answer:
            """.strip()

        self.PROMPT = PromptTemplate.from_template(
            template = self.prompt_template
        )

        self.history = ChatMessageHistory()

        self.model_name = 'hkunlp/instructor-base'

        self.embedding_model = HuggingFaceInstructEmbeddings(
            model_name = self.model_name,
            # model_kwargs = {"device" : device}
        )

        self.vector_path = '../vector-store'
        self.db_file_name = 'a6'

        self.vectordb = FAISS.load_local(
            folder_path = os.path.join(self.vector_path, self.db_file_name),
            embeddings = self.embedding_model,
            index_name = 'a6', #default index
            allow_dangerous_deserialization=True
        )   

        self.retriever = self.vectordb.as_retriever()

        if "GROQ_API_KEY" not in os.environ:
            os.environ["GROQ_API_KEY"] = "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"

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            # other params...
        )

        self.question_generator = LLMChain(
            llm = self.llm,
            prompt = CONDENSE_QUESTION_PROMPT,
            verbose = True
        )

        self.memory = ConversationBufferWindowMemory(
            k=3, 
            memory_key = "chat_history",
            return_messages = True,
            output_key = 'answer'
        )
        self.doc_chain = load_qa_chain(
            llm = self.llm,
            chain_type = 'stuff',
            prompt = self.PROMPT,
            verbose = True
        )

        self.chain = ConversationalRetrievalChain(
            retriever=self.retriever,
            question_generator=self.question_generator,
            combine_docs_chain=self.doc_chain,
            return_source_documents=True,
            memory=self.memory,
            verbose=True,
            get_chat_history=lambda h : h
        )
        
        
        
    def chat(self, question):
        return self.chain({"question":question})['answer']

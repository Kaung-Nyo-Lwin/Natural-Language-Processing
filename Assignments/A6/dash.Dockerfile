FROM python:3.10.12

WORKDIR /root/app
# WORKDIR /home/knl/DSAI/NLP/w1/a1/app

RUN pip3 install dash
RUN pip3 install pandas
RUN pip3 install dash_bootstrap_components
RUN pip3 install torch==2.6.0
# langchain library
RUN pip3 install langchain==0.3.20
RUN pip3 install langchain-community==0.3.19
# LLM
RUN pip3 install accelerate==0.25.0
RUN pip3 install transformers==4.36.2
RUN pip3 install bitsandbytes==0.45.3
# text Embedding
RUN pip3 install sentence-transformers==2.2.2
RUN pip3 install InstructorEmbedding==1.0.1
# vectorstore
RUN pip3 install pymupdf==1.25.4
RUN pip3 install faiss-cpu==1.7.4
# huggingface_hub
RUN pip3 install huggingface-hub==0.20.0



COPY ./app /root/app/
# COPY . ./
# CMD tail -f /dev/null

CMD python3 main.py
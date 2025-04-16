FROM python:3.10.12

WORKDIR /root/app
# WORKDIR /home/knl/DSAI/NLP/w1/a1/app

RUN pip3 install dash
RUN pip3 install dash_bootstrap_components
RUN pip3 install dash-bootstrap-components[pandas]
RUN pip3 install torch==2.2
RUN pip3 install datasets
RuN pip3 install transformers
RUN pip3 install safetensors==0.4.5
RUN pip3 install huggingface_hub==0.26.1



COPY ./app /root/app/
# COPY . ./
# CMD tail -f /dev/null

CMD python3 main.py
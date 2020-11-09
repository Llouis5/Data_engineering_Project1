FROM python:3.6

WORKDIR /home/

COPY requirements.txt .
COPY app.py .
COPY lemmatized_data_reduced.csv .
COPY model .
COPY templates/ .

RUN pip install -r requirements.txt

EXPOSE 5000

RUN python app.py


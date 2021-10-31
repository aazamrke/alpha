FROM python:3
ENV PYTHONUNBUFFERED=1 APIKEY=4QGQRX9C1RBBTEVK
WORKDIR /alphavantage
COPY requirements.txt /alphavantage/
RUN pip install -r requirements.txt
COPY . /alphavantage/
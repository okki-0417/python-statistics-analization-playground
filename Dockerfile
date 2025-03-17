FROM python:3.11

WORKDIR /app

COPY ./app .

RUN pip install --upgrade pip && \
      pip install pandas matplotlib seaborn


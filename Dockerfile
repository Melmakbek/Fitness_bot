FROM python:3.12.3

WORKDIR /fitness_bot

COPY . /fitness_bot/

RUN pip install -r requirements.txt

ENTRYPOINT python bot.py
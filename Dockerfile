FROM python:3.8

RUN mkdir -p /usr/src/app RUN
WORKDIR /usr/src/app
COPY ./ ./

RUN pip install aiogram emoji
RUN pip show aiogram

CMD ["python", "LeagueBot.py"]

FROM python:3.12
WORKDIR /bot
COPY deps.txt /bot/
RUN pip install -r deps.txt
COPY . /bot/
CMD ["python", "main.py"]
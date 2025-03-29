FROM python:3.13
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python3","main.py"]

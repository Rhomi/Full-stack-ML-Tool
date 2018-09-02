FROM python:3.6.4
ADD . /app
WORKDIR /app
EXPOSE 4000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python","index.py"]
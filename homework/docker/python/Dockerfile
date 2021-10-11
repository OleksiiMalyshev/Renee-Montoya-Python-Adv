FROM python:3.9
WORKDIR /docker
COPY requirements.txt /docker
RUN pip install --upgrade pip -r requirements.txt
COPY app.py /docker
COPY . /docker
CMD python3 app.py
EXPOSE 5050

FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN mkdir app
WORKDIR /app

COPY ./app/ /app/
RUN /usr/local/bin/python -m pip install --upgrade pip

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# EXPOSE 5000

# CMD ["python", "app.py"]
# CMD ["flask run --host=0.0.0.0 --port=5080"]

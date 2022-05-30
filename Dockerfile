FROM python:3.9
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
WORKDIR /code/src
CMD [ "python", "app.py" ]
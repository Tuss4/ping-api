FROM python:3.6
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
WORKDIR /code/pingapi

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "pingapi.wsgi"]

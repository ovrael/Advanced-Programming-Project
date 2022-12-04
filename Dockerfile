FROM python:3.11.0-bullseye
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

RUN set PYTHONPATH=.
COPY main.py /code

EXPOSE 20333
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "20333"]
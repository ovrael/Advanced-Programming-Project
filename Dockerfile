FROM python:3.11.0-bullseye

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get install libgl1
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN set PYTHONPATH=.

COPY ./app /code/app

EXPOSE 20222
ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "20222"]
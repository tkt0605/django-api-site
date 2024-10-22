FROM python:3.9
WORKDIR /django
COPY ./backend /django
RUN pip install -r requirements.txt
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application" ]
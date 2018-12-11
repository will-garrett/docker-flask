FROM python:3.7
#ENV APP /code
ENV FLASK_APP=microblog.py

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
#CMD python microblog.py
#EXPOSE 5000
CMD flask run
FROM python:3.7
MAINTAINER genughaben

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
ADD . /code
WORKDIR /code

RUN useradd -ms /bin/bash user
USER user

CMD ["bash", "app/start.sh"]
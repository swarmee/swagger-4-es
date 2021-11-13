FROM python:3.9-alpine

# install wget and unzip
#RUN apk update && apk add wget bash curl unzip && rm -rf /var/cache/apk/*

#USER root

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /scripts/

COPY ./* /scripts/ 

# give everybody access
RUN chmod -R 770 /scripts/*

RUN pip install --no-cache-dir -r /scripts/requirements.txt

CMD ["python", "/scripts/setup_elastic.py"]

# use this to keep a temporary container alive for trouble shooting
#ENTRYPOINT ["tail", "-f", "/dev/null"]
#ENTRYPOINT ["/usr/bin/curl"]
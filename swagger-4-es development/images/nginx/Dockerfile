FROM nginx:stable-alpine

# install wget and unzip
RUN apk update && apk add bash openssl && rm -rf /var/cache/apk/*

RUN mkdir -p /etc/nginx/ssl/ \
    && openssl req \
            -x509 \
            -subj "/C=AU/ST=HELLO/L=MYPLACE/O=ALONGWAY" \
            -nodes \
            -days 365 \
            -newkey rsa:2048 \
            -keyout /etc/nginx/ssl/certificate.key \
            -out /etc/nginx/ssl/certificate.crt

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf
#COPY ./app.htpasswd /etc/nginx/conf.d/app.htpasswd

#
#COPY ../certificate.crt:/etc/nginx/ssl/certificate.crt
#COPY ../certificate.key:/etc/nginx/ssl/certificate.key
#COPY ../kibana.htpasswd:/etc/nginx/conf.d/kibana.htpasswd

# remove log symlinks
#RUN unlink /var/log/nginx/access.log
#RUN unlink /var/log/nginx/error.log
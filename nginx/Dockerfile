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

# remove log symlinks
#RUN unlink /var/log/nginx/access.log
#RUN unlink /var/log/nginx/error.log
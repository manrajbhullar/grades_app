FROM nginx:latest

RUN apt-get update 

RUN apt-get install apache2-utils -y

RUN htpasswd -b -c /password admin password

COPY ./default.conf /etc/nginx/conf.d/default.conf
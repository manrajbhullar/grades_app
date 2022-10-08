FROM mysql

ENV MYSQL_ROOT_PASSWORD root

ENV MYSQL_USER grades_app

ENV MYSQL_PASSWORD grades_app

ENV MYSQL_DATABASE grades_app

COPY ./create_db.sql /tmp

CMD [ "mysqld", "--init-file=/tmp/create_db.sql" ]

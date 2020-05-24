FROM python:3.6.7

ENV NGINX_PATH=/etc/nginx NGINX_SITE_CONF_PATH=/etc/nginx/sites-enabled

# upgrade pip
RUN pip install --upgrade pip

# Removing Nginx Default files
RUN rm -Rf /etc/nginx/conf.d/*  /etc/nginx/nginx.conf /etc/nginx/sites-available/default

# add nginx configuration files
COPY nginx/nginx.conf ${NGINX_PATH}/nginx.conf
COPY nginx/snippets   ${NGINX_PATH}/snippets
COPY nginx/sites-enabled   ${NGINX_SITE_CONF_PATH}/

# create flask project directory
RUN mkdir /skthon
WORKDIR /skthon

# copy the requirements file and install the dependencies
COPY skthon/requirements.txt /skthon
RUN pip install --no-cache-dir -r /skthon/requirements.txt

ADD ./skthon /skthon/

EXPOSE 8081
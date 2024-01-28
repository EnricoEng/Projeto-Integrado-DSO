FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf .

COPY nginx-selfsigned.crt /etc/nginx/ssl/nginx-selfsigned.crt
COPY nginx-selfsigned.key /etc/nginx/ssl/nginx-selfsigned.key


RUN cp nginx.conf /etc/nginx/conf.d/

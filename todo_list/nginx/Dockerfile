FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf .
RUN cp nginx.conf /etc/nginx/conf.d/

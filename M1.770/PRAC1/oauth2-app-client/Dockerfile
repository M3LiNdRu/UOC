FROM docker.io/nginx:latest
COPY default.conf /etc/nginx/conf.d/default.conf
COPY dist/oauth2-app/* /usr/share/nginx/html
COPY certs/nginx-selfsigned.key /etc/ssl/private/
COPY certs/nginx-selfsigned.crt /etc/ssl/certs/
RUN chown -R nginx:nginx /usr/share/nginx/html/
EXPOSE 4200
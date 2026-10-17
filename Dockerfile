FROM nginxinc/nginx-unprivileged:1.30-alpine
COPY public/ /usr/share/nginx/html/
EXPOSE 8080

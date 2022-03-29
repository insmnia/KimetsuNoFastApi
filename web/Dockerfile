FROM nginx:1.15-alpine

COPY ./web/app.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
# Use the Nginx image
FROM nginx:alpine

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80

# ENTRYPOINT ["/bin/bash"]
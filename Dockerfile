# Python
FROM python:3-alpine
COPY . /usr/src/
WORKDIR /usr/src/
RUN apk add --no-cache curl && pip install -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/ || exit 1
CMD ["flask","run","--host","0.0.0.0"]


# Stress
#FROM fedora:latest
#RUN yum -y install stress && yum clean all
#ENTRYPOINT ["stress"]

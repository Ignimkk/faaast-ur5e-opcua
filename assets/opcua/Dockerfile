FROM adoptopenjdk/openjdk11:latest
RUN mkdir /opt/app
COPY server-2.0.0-all.jar /opt/app
COPY config.json /opt/app
CMD ["java", "-jar", "/opt/app/server-2.0.0-all.jar", "/opt/app/config.json"]
EXPOSE 12686
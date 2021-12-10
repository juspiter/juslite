FROM python:3.9.7

WORKDIR /app

RUN pip install --no-cache-dir flask==2.0.2 flask-cors==3.0.10 \
        elasticsearch==7.15.2 elasticsearch-dsl==7.4.0

COPY . .

EXPOSE 3001

CMD ["sleep", "60", "--", "python", "api.py"]

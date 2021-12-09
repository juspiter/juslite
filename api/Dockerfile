FROM python:3.9.7

WORKDIR /usr/src/app

RUN pip install --no-cache-dir flask==2.0.2 flask-cors==3.0.10 \
        elasticsearch==7.15.2 elasticsearch-dsl==7.4.0

COPY . .

COPY ./common/wait-for-it.sh .

CMD ["./wait-for-it.sh", "juslite_elastic:9200", "--", "python", "api.py"]

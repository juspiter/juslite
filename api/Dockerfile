FROM python:3.9.7

WORKDIR /app

RUN pip install --no-cache-dir fastapi==0.74.1 uvicorn[standard]==0.17.5 \
        elasticsearch==7.15.2 elasticsearch-dsl==7.4.0

COPY . .

EXPOSE 3001

RUN chmod +x wait-for-it.sh

CMD [ "./wait-for-it.sh", "juslite_elastic:9200", "--timeout=0", "--", "uvicorn", "api:app", "--host", "juslite_api", "--port", "3001" ]

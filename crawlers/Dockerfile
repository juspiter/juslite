FROM python:3.9.7

WORKDIR /app

RUN pip install beautifulsoup4==4.10.0 scrapy==2.5.1 \
			elasticsearch==7.15.2 elasticsearch-dsl==7.4.0

ENV PYTHONPATH=/app:/app/teste_scrapy/tstSpider/tstSpider

COPY . .

CMD ["sleep", "60", "--", "bash", "es_config.sh", "--" "python", "main.py"]

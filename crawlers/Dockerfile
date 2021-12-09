FROM python:3.9.7

WORKDIR /usr/src/app

RUN pip install beautifulsoup4==4.10.0 scrapy==2.5.1 \
			elasticsearch==7.15.2 elasticsearch-dsl==7.4.0

COPY . .

COPY ./common/wait-for-it.sh .

CMD ["./wait-for-it.sh", "juslite_elastic:9200", "--", "python", "main.py"]

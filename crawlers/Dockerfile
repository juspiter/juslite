FROM python:3.9.7

WORKDIR /app

RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/timezone && \
			ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN pip install requests==2.26.0 beautifulsoup4==4.10.0 scrapy==2.5.1 \
			elasticsearch==7.15.2 elasticsearch-dsl==7.4.0

ENV PYTHONPATH=/app:/app/teste_scrapy/tstSpider/tstSpider

COPY . .

RUN chmod +x wait-for-it.sh

CMD [ "./wait-for-it.sh", "juslite_elastic:9200", "--timeout=0", "--", "bash", "start_all.sh"]

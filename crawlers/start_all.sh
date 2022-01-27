#!/usr/bin/env bash

curl -X PUT "juslite_elastic:9200/tjal?pretty"
curl -X PUT "juslite_elastic:9200/tjce?pretty"
curl -X PUT "juslite_elastic:9200/tst?pretty"
curl -X PUT "juslite_elastic:9200/_all/_mappings?pretty" -H 'Content-Type: application/json' -d'
{
    "dynamic_date_formats": ["dd/MM/yyyy"]
}
'

sh crawl.sh

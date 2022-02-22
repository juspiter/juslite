#!/usr/bin/env bash

curl -X PUT "juslite_elastic:9200/tjal?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "analysis": {
      "analyzer": {
        "default": {
          "type": "brazilian"
        }
      }
    }
  }
}
'

curl -X PUT "juslite_elastic:9200/tjce?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "analysis": {
      "analyzer": {
        "default": {
          "type": "brazilian"
        }
      }
    }
  }
}
'

curl -X PUT "juslite_elastic:9200/tst?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "analysis": {
      "analyzer": {
        "default": {
          "type": "brazilian"
        }
      }
    }
  }
}
'

curl -X PUT "juslite_elastic:9200/_all/_mappings?pretty" -H 'Content-Type: application/json' -d'
{
  "dynamic_date_formats": ["dd/MM/yyyy"]
}
'

sh crawl.sh

from fastapi import FastAPI
from searchengine import SearchEngine

se = SearchEngine('juslite_elastic:9200')

app = FastAPI()


@app.get("//query/{term}")
def query_term(term: str = "", sort: str = "relevante", court: str = "todos", field: str = "todos", page: int = 1):
    return se.get_results(term, sort, court, field, page)


@app.get("//lawsuit/{number_id}")
def get_lawsuit(number_id: str = ""):
    return se.get_one_lawsuit(number_id)

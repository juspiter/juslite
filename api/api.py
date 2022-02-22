from fastapi import FastAPI
from searchengine import SearchEngine

se = SearchEngine('juslite_elastic:9200')

app = FastAPI()


@app.get("//lawsuit/{term}")
def query_lawsuit(term: str = "", sort: str = "relevante", court: str = "todos", field: str = "todos", page: int = 1):
    return se.get_results(term, sort, court, field, page)

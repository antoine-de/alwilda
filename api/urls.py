from apistar import Route
from .search import search_address


api_urls = [
    Route('/instant_answer', 'GET', instant_answer)
]

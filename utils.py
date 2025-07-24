import random
import string
from sqlalchemy.orm import Query
from math import ceil

def paginate(query: Query, page:str = "1", page_size=10) -> dict:
    if page == "0": page = "1"
    paginated_query = query.offset(
        (int(page) - 1) * page_size
    ).limit(page_size).all()

    return {
        'current_page': int(page), 
        'data': paginated_query, 
        'last_page': ceil(query.count() / page_size), 
        'per_page': page_size,
        'current_length': len(paginated_query)
    }

def get_random_string(length = 10):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

def has_bearer_token(authorization_header: str) -> bool:
    if (authorization_header is None): return False
    return (
        ('Bearer' in authorization_header or 
        'bearer' in authorization_header) and 
        len(authorization_header.split(' ')) > 1)

def get_bearer_token(authorization_header: str) -> str | None:
    if (has_bearer_token(authorization_header) is False): return None
    return authorization_header.split(' ')[1]
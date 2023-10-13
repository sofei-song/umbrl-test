from typing import Union

from fastapi import APIRouter

# import psycopg2

 

router = APIRouter(

    prefix='/users',

    tags=['users']

)

@router.get("/")

def get_users(id: int):

    # conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")

    # cur = conn.cursor()

    # cur.execute("SELECT first_name FROM datacamp_courses WHERE ID=${id};")

    # rows = cur.fetchall()

    # return rows

    return id

 

@router.get("/items/{item_id}")

def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}
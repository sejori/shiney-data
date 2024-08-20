from utils.db_utils import sql
from dtos.card_dtos import CreateCardRequest

def CreateCard(body: CreateCardRequest):
    if (body.content and body.deck_id):
        result = sql(f'INSERT INTO card (content, deck_id) VALUES ("{body.content}", {body.deck_id})')
    elif (body.content):
        result = sql(f'INSERT INTO card (content) VALUES ("{body.content}")')
    elif (body.deck_id):
        result = sql(f'INSERT INTO card (deck_id) VALUES ({body.deck_id})')
    else:
        result = sql(f'INSERT INTO card DEFAULT VALUES')

    return result

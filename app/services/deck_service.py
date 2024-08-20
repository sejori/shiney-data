from utils.db_utils import sql
from dtos.deck_dtos import GetDeckWithCardsRequest

def ListDeckItems(body: GetDeckWithCardsRequest):
    if body.deck_id:
        card_results = sql(f'SELECT * FROM card WHERE deck_id = {body.deck_id} ORDER BY lexorank')
        deck_results = sql(f'SELECT * FROM deck WHERE deck_id = {body.deck_id} OR parent_id = {body.deck_id} ORDER BY lexorank')
    else:
        card_results = sql('SELECT * FROM card ORDER BY lexorank')
        deck_results = sql('SELECT * FROM deck ORDER BY lexorank')

    return {'deck_results': deck_results, 'card_results': card_results}

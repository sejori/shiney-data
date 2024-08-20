from utils.db_utils import sql
from dtos.deck_dtos import GetDeckWithCardsRequest

def ListDeckItems(body: GetDeckWithCardsRequest):
    if body.deck_id:
        card_results = sql(f'SELECT * FROM card WHERE deck_id = {body.deck_id}')
        deck_results = sql(f'SELECT * FROM deck WHERE parent_id = {body.deck_id}')
    else:
        card_results = sql('SELECT * FROM card')
        deck_results = sql('SELECT * FROM deck')

    return {'deck_results': deck_results, 'card_results': card_results}

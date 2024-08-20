from services.card_service import ListCards
from utils.db_utils import sql
from dtos.deck_dtos import GetDeckWithCardsRequest

def ListDecks(body: GetDeckWithCardsRequest):
    if body.deck_id:
        results = sql(f'SELECT * FROM deck WHERE deck_id = {body.deck_id} OR parent_id = {body.deck_id} ORDER BY lexorank')
    else:
        results = sql('SELECT * FROM deck ORDER BY lexorank')
    return results

def ListDeckItems(body: GetDeckWithCardsRequest):
    return {'deck_results': ListDecks(body), 'card_results': ListCards(body)}

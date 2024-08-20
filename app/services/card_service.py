from dtos.deck_dtos import GetDeckWithCardsRequest
from utils.db_utils import sql, calcLexorank
from dtos.card_dtos import CreateCardRequest, GetCardByIdRequest, RepositionCardRequest, UpdateCardRequest

def GetCardById(body: GetCardByIdRequest):
    result = sql(f'SELECT * FROM card WHERE card_id = {body.card_id}')
    if len(result) > 0:
        return result[0]
    else:
        return Exception('Card not found.')
    
def ListCards(body: GetDeckWithCardsRequest):
    if body.deck_id:
        results = sql(f'SELECT * FROM card WHERE deck_id = {body.deck_id} ORDER BY lexorank')
    else:
        results = sql('SELECT * FROM card ORDER BY lexorank')
    return results

def CreateCard(body: CreateCardRequest):
    # new cards default to the end of the deck/list
    cards = ListCards(GetDeckWithCardsRequest(deck_id=body.deck_id))
    lexorank = calcLexorank(cards[len(cards) - 1]['lexorank'], None)

    if (body.content and body.deck_id):
        result = sql(f'INSERT INTO card (content, deck_id, lexorank) VALUES ("{body.content}", {body.deck_id}, "{lexorank}")')
    elif (body.content):
        result = sql(f'INSERT INTO card (content, lexorank) VALUES ("{body.content}", "{lexorank}")')
    elif (body.deck_id):
        result = sql(f'INSERT INTO card (deck_id, lexorank) VALUES ({body.deck_id}, "{lexorank}")')
    else:
        result = sql(f'INSERT INTO card (lexorank) VALUES ("{lexorank}")')

    return result

def UpdateCard(body: UpdateCardRequest):
    setStatements = []
    if (body.content):
        setStatements.append(f'content = "{body.content}"')
    elif (body.deck_id):
        setStatements.append(f'deck_id = {body.deck_id}')

    setClause = ', '.join(setStatements)
    return sql(f'UPDATE card SET {setClause} WHERE card_id = {body.card_id}')

def DeleteCard(body: GetCardByIdRequest):
    return sql(f'DELETE FROM card WHERE card_id = {body.card_id}')

def RepositionCard(body: RepositionCardRequest):
    preceding_card = GetCardById(GetCardByIdRequest(card_id=body.preceding_card_id))
    deck_cards = ListCards(GetDeckWithCardsRequest(deck_id=preceding_card.get('deck_id')))
    following_card = deck_cards[deck_cards.index(preceding_card) + 1] if preceding_card in deck_cards[:-1] else None

    new_rank = calcLexorank(preceding_card.get('lexorank'), following_card.get('lexorank') if following_card else None)
    return sql(f'UPDATE card SET lexorank = "{new_rank}" WHERE card_id = {body.card_id}')

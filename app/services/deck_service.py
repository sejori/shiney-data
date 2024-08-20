from services.card_service import ListCards
from utils.db_utils import calcLexorank, sql
from dtos.deck_dtos import CreateDeckRequest, GetDeckByIdRequest, GetDeckWithCardsRequest, RepositionDeckRequest, UpdateDeckRequest

def GetDeckById(body: GetDeckByIdRequest):
    result = sql(f'SELECT * FROM deck WHERE deck_id = {body.deck_id}')
    if len(result) > 0:
        return result[0]
    else:
        return Exception('Deck not found.')

def ListDecks(body: GetDeckWithCardsRequest):
    if body.deck_id:
        results = sql(f'SELECT * FROM deck WHERE deck_id = {body.deck_id} OR parent_id = {body.deck_id} ORDER BY lexorank')
    else:
        results = sql('SELECT * FROM deck ORDER BY lexorank')
    return results

def ListDeckItems(body: GetDeckWithCardsRequest):
    return {'deck_results': ListDecks(body), 'card_results': ListCards(body)}

def CreateDeck(body: CreateDeckRequest):
    # new deck default to the end of the deck/list
    cards = ListDecks(GetDeckWithCardsRequest())
    lexorank = calcLexorank(cards[len(cards) - 1]['lexorank'], None)

    if (body.name and body.parent_id):
        result = sql(f'INSERT INTO deck (name, parent_id, lexorank) VALUES ("{body.name}", {body.parent_id}, "{lexorank}")')
    elif (body.name):
        result = sql(f'INSERT INTO deck (name, lexorank) VALUES ("{body.name}", "{lexorank}")')
    elif (body.parent_id):
        result = sql(f'INSERT INTO deck (parent_id, lexorank) VALUES ({body.parent_id}, "{lexorank}")')
    else:
        result = sql(f'INSERT INTO deck (lexorank) VALUES ("{lexorank}")')

    return result

def UpdateDeck(body: UpdateDeckRequest):
    setStatements = []
    if (body.name):
        setStatements.append(f'name = "{body.name}"')
    elif (body.parent_id):
        setStatements.append(f'parent_id = {body.parent_id}')

    # TODO: update updated_timestamp

    setClause = ', '.join(setStatements)
    return sql(f'UPDATE deck SET {setClause} WHERE deck_id = {body.deck_id}')

def DeleteDeck(body: GetDeckByIdRequest):
    return sql(f'DELETE FROM deck WHERE deck_id = {body.deck_id}')

def RepositionDeck(body: RepositionDeckRequest):
    preceding_deck = GetDeckById(GetDeckByIdRequest(deck_id=body.preceding_deck_id))
    decks = ListDecks(GetDeckWithCardsRequest(deck_id=preceding_deck.get('deck_id')))
    following_deck = decks[decks.index(preceding_deck) + 1] if preceding_deck in decks[:-1] else None

    new_rank = calcLexorank(preceding_deck.get('lexorank'), following_deck.get('lexorank') if following_deck else None)
    return sql(f'UPDATE deck SET lexorank = "{new_rank}" WHERE deck_id = {body.deck_id}')

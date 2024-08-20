
from flask import Flask, jsonify, request
from services.card_service import CreateCard, DeleteCard, RepositionCard, UpdateCard
from services.deck_service import CreateDeck, DeleteDeck, ListDeckItems, RepositionDeck, UpdateDeck
from dtos.card_dtos import CreateCardRequest, GetCardByIdRequest, RepositionCardRequest, UpdateCardRequest
from dtos.deck_dtos import CreateDeckRequest, GetDeckByIdRequest, GetDeckWithCardsRequest, RepositionDeckRequest, UpdateDeckRequest
from utils.db_utils import sql

app = Flask(__name__)

"""
Here are two sample endpoints to test the connection to the database and posting to the server.
Here's a sample curl request to test the post to the below sample route.
curl -X POST -H "Content-Type: application/json" -d '{"test_string":"test"}' http://localhost:5001/post

Please add the endpoint to this file.

You can specify the interface to the frontend using a pydantic model like the Body model below if you want, or do something better.
"""


@app.route('/')
def sample_get_route():
    deck_id = request.args.get('deck_id')
    body = GetDeckWithCardsRequest(deck_id=deck_id)
    json_results = ListDeckItems(body)
    return jsonify(json_results)


"""
CRUD operations for cards
"""
@app.route('/post', methods=['POST'])
def sample_post_route():
    body = CreateCardRequest(**request.json)
    result = CreateCard(body)
    return jsonify(result)

@app.route('/reposition_card', methods=['POST'])
def reposition_card():
    body = RepositionCardRequest(**request.json)
    result = RepositionCard(body)
    return jsonify(result)

@app.route('/update_card', methods=['POST'])
def update_card():
    body = UpdateCardRequest(**request.json)
    result = UpdateCard(body)
    return jsonify(result)

@app.route('/delete_card', methods=['POST'])
def delete_card():
    body = GetCardByIdRequest(**request.json)
    result = DeleteCard(body)
    return jsonify(result)


"""
CRUD operations for decks
"""
@app.route('/post_deck', methods=['POST'])
def post_deck():
    body = CreateDeckRequest(**request.json)
    result = CreateDeck(body)
    return jsonify(result)

@app.route('/reposition_deck', methods=['POST'])
def reposition_deck():
    body = RepositionDeckRequest(**request.json)
    result = RepositionDeck(body)
    return jsonify(result)

@app.route('/update_deck', methods=['POST'])
def update_deck():
    body = UpdateDeckRequest(**request.json)
    result = UpdateDeck(body)
    return jsonify(result)

@app.route('/delete_deck', methods=['POST'])
def delete_deck():
    body = GetDeckByIdRequest(**request.json)
    result = DeleteDeck(body)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

from flask import Flask, jsonify, request
from services.card_service import CreateCard
from services.deck_service import ListDeckItems
from dtos.card_dtos import CreateCardRequest
from dtos.deck_dtos import GetDeckWithCardsRequest
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
    body = GetDeckWithCardsRequest()
    json_results = ListDeckItems(body)
    return jsonify(json_results)


@app.route('/post', methods=['POST'])
def sample_post_route():
    body = CreateCardRequest(**request.json)
    result = CreateCard(body)
    return jsonify(result)



@app.route('/get_deck', methods=['POST'])
def get_deck():
    """A method to get all of a deck's cards and child decks
    """
    body = GetDeckWithCardsRequest(**request.get_json())
    json_results = ListDeckItems(body)
    return jsonify(json_results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
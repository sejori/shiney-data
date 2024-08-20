
from flask import Flask, jsonify, request
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
    card_results = sql('SELECT * FROM card')
    deck_results = sql('SELECT * FROM deck')
    json_results = {'deck_results': deck_results, 'card_results': card_results}
    return jsonify(json_results)


@app.route('/post', methods=['POST'])
def sample_post_route():
    body = CreateCardRequest(**request.get_json())
    return jsonify(body.model_dump())



@app.route('/get_deck', methods=['POST'])
def get_deck():
    """A method to get all of a deck's cards and child decks
    """
    body = GetDeckWithCardsRequest(**request.get_json())
    card_results = sql(f'SELECT * FROM card WHERE deck_id = {body.deck_id}')
    deck_results = sql('SELECT * FROM deck WHERE parent_id = {body.deck_id}')
    json_results = {'deck_results': deck_results, 'card_results': card_results}
    return jsonify(json_results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
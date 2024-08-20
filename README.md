# Card & Deck Organiser

This is a proof of concept backend application to organise virtual cards and decks of cards.

It is built with Flask and Pydantic.

# Run the app

1. Initialise db: `$ python init_db.py`

2. Start app server: `$ python app/wsgi.py`

# Basic testing

The easiest way to test the app is to open `localhost:5001` in a web browser.

You will see a JSON response of cards and decks. Click "prettify" in Google Chrome to make it readable.

## POSTing data

To post data, open the web inspector console in chrome and use a fetch command like so:

```js
fetch('/post', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        content: 'This is a new card'
        // deck_id: 1 <- to add to a deck on creation
    })
})
```
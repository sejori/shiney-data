# Card & Deck Organiser

This is a proof of concept backend application to organise virtual cards and decks of cards.

It is built with Flask and Pydantic.

# Run the app

1. Initialise db: `$ python init_db.py`

2. Start app server: `$ python app/wsgi.py`

## Requirements

The app has two models:
- Decks - contain cards and other decks
- Cards - contain content for users to revise

Users need to be able to move the cards and decks around with a drag and drop interface like on the homepage of a smartphone. 

The position of the cards and decks needs to be persisted, with the number of writes to the database being kept to a minimum.

## Technical solution

The data can be modelled quite simply in a relational database with two tables: card and deck. We can then build a basic CRUD API on top of these data models for updating data. 

The challenge is persist the order of items whilst minimising database writes. An obvious solution is to store the position of a deck or card as an integer in a database column. However, consider the case where a card is reordered to appear before other cards: it's position would need to be updated and so would all of the following cards'.

Is there a better way? Indeed there is: Lexorank. 

We will use alphabetical characters to store the order of items in the database. This may seem odd but is actually a brilliant technique!

For example, a card has position "A" and another has position "B". We want to insert card "C" in between "A" and "B". We can simply update the position of "C" to "AN". 

Now when ordered by lexorank (alphabetically) the cards will appear:

"A" -> "AN" -> "B"

Notice that we did not need to adjust the position values of A or B to achieve this.


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

To demonstrate the lexorank adjustments, try repoisitioning a card like so:

```js
fetch('/reposition_card', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        card_id: 4,
        preceding_card_id: 1 
    })
})
```

# Further changes:

- Generate OpenAPI / swagger docs 
- Expand e2e / unit tests
- Refactor to DDD if number of entities will increase
- Better data validation out of DB
- Consider a junction table to optimise db and dedupe cards across users
- Extract db logic to repository classes/modules and implement into a DRY service for both card and deck as logic is quite repetitive between them
- CI/CD pipeline to test and deploy to GCP CloudRun with GitHub actions

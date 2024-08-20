DROP TABLE IF EXISTS deck;
CREATE TABLE deck (
    deck_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    parent_id INTEGER,
    lexorank TEXT NOT NULL,
    created_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(parent_id) references deck(deck_id)
);

DROP TABLE IF EXISTS card;
CREATE TABLE card (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    deck_id integer references deck(deck_id),
    lexorank TEXT NOT NULL,
    created_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(deck_id) references deck(deck_id)
);




INSERT INTO deck (name, parent_id, lexorank) VALUES ('deck1', NULL, 'a');
INSERT INTO deck (name, parent_id, lexorank) VALUES ('deck2', NULL, 'b');
INSERT INTO deck (name, parent_id, lexorank) VALUES ('deck3', 1, 'a');

INSERT INTO card (content, deck_id, lexorank) VALUES ('card 1', 1, 'a');
INSERT INTO card (content, deck_id, lexorank) VALUES ('card 2', 1, 'd');
INSERT INTO card (content, deck_id, lexorank) VALUES ('card 3', 1, 'b');
INSERT INTO card (content, deck_id, lexorank) VALUES ('card 4', 1, 'c');



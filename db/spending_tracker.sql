DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE tags(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    amount INT,
    merchant_id INT REFERENCES merchants(id),
    tag_id INT REFERENCES tags(id),
    timestamp VARCHAR(255)
);
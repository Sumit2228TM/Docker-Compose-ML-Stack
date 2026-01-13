CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    input_value FLOAT NOT NULL,
    prediction FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

CREATE INDEX idx_timestamp ON predictions(timestamp DESC);

INSERT INTO predictions (input_value, prediction, timestamp) VALUES
(1.0, 2.0, NOW()),
(2.5, 5.0, NOW()),
(3.7, 7.4, NOW());
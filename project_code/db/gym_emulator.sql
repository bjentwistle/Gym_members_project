DROP TABLE IF EXISTS MOCK_MEMBERS;

CREATE TABLE MOCK_MEMBERS (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255), 
    gender VARCHAR(255), 
    postcode VARCHAR(255), 
    premium_member BOOLEAN

);
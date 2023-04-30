DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255), 
    postcode VARCHAR(255), 
    premium_member BOOLEAN

);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    duration INT,
    premium_session BOOLEAN,
    capacity INT

);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    -- members_id INT REFERENCES members(id) ON DELETE CASCADE,
    members_id INT ,
    -- sessions_id INT REFERENCES sessions(id) ON DELETE CASCADE
    sessions_id INT 

);
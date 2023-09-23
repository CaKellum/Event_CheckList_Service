-- NOTE: All 'X_id INTEGER PRIMARY KEY NOT NULL' should act as if autoincrementing values
-- the NOT NULL is added because there is a known issue w/ some versions fo SQL that 
-- PRIMARY KEY won't garuntee the value being populated

CREATE TABLE person (
    person_id INTEGER PRIMARY KEY NOT NULL, 
    person_name TEXT
);

CREATE TABLE event (
    event_id INTEGER PRIMARY KEY NOT NULL, 
    event_name TEXT,
    event_date TEXT
);

CREATE TABLE event_service (
    event_id INTEGER, 
    service_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (service_id) REFERENCES service_table(service_id),
    PRIMARY KEY (event_id, service_id)
);

-- there are going to be alot of activity on this from many clients likely to have the
-- highest chance of data corruption
-- BIGGEST argument for a noSQL database solution
CREATE TABLE event_people (
    person_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    person_checked_equip INTEGER DEFAULT 0,  --Defaluts to false
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    PRIMARY KEY (person_id, event_id)
);

CREATE TABLE service_table (
    service_id INTEGER PRIMARY KEY NOT NULL,
    service_name TEXT
);

CREATE TABLE service_equipment(
    service_id INTEGER,
    equipment_id INTEGER,
    FOREIGN KEY (service_id) REFERENCES service_table(service_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
    PRIMARY KEY (service_id, equipment_id)
);

CREATE TABLE equipment (
    equipment_id INTEGER PRIMARY KEY NOT NULL,
    equipment_name TEXT,
    amount INTEGER
);

CREATE TABLE auth_table (
    auth_user_id INTEGER PRIMARY KEY NOT NULL,
    auth_hash INTEGER UNIQUE DEFAULT (random() % 101),
    person_id INTEGER,
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);

CREATE TABLE auth_user_table (
    auth_login_id INTEGER PRIMARY KEY NOT NULL,
    user TEXT UNIQUE NOT NUll,
    pass_hash TEXT UNIQUE NOT NULL
    is_temp_pass INTEGER DEFAULT 1 -- Defaluts true, as to make it easyier for the user creation flow
);
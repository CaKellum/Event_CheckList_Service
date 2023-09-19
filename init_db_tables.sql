CREATE TABLE person (
    person_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT, 
    person_name TEXT
);

CREATE TABLE event (
    event_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT, 
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

CREATE TABLE event_people (
    person_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    person_checked_equip INTEGER DEFAULT 0, 
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    PRIMARY KEY (person_id, event_id)
);

CREATE TABLE service_table (
    service_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    service_name TEXT
);

CREATE TABLE service_equipment(
    service_id INTEGER,
    equipment_id INTEGER,
    FOREIGN KEY (service_id) REFERENCES service_table(service_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
    PRIMARY KEY (service_id, equipment_id);
);

CREATE TABLE equipment (
    equipment_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    equipment_name TEXT,
    amount INTEGER
);
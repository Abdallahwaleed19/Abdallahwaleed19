CREATE TABLE users (
    user_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR2(20) UNIQUE NOT NULL,
    password VARCHAR2(25) NOT NULL,
    role VARCHAR2(10) CHECK (role IN ('admin', 'user')) NOT NULL,
    event_id NUMBER REFERENCES events(event_id)
);

CREATE TABLE events (
    event_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(25) NOT NULL,
    description CLOB,
    schedule VARCHAR2(30),
    location VARCHAR2(30),
    image_name VARCHAR2(25),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bookings (
    booking_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id NUMBER REFERENCES users(user_id),
    event_id NUMBER REFERENCES events(event_id),
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR2(15) DEFAULT 'active' CHECK (status IN ('active', 'cancelled', 'completed')),
    CONSTRAINT unique_user_event UNIQUE (user_id, event_id)
);

CREATE TABLE event_schedules (
    schedule_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    event_id NUMBER REFERENCES events(event_id),
    schedule_date DATE,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    capacity NUMBER DEFAULT 15,
    available_slots NUMBER,
    CONSTRAINT check_times CHECK (end_time > start_time)
);

INSERT INTO users (username, password, role)
VALUES ('admin', 'admin123', 'admin');

CREATE OR REPLACE TRIGGER events_update_trigger
BEFORE UPDATE ON events
FOR EACH ROW
BEGIN
    :NEW.updated_at := CURRENT_TIMESTAMP;
END;
/

CREATE OR REPLACE TRIGGER schedule_slots_trigger
BEFORE INSERT OR UPDATE ON event_schedules
FOR EACH ROW
BEGIN
    IF :NEW.available_slots IS NULL THEN
        :NEW.available_slots := :NEW.capacity;
    END IF;
END;
/

CREATE OR REPLACE VIEW event_details_view AS
SELECT 
    e.event_id,
    e.name AS event_name,
    e.description,
    e.schedule,
    e.location,
    e.image_name,
    es.schedule_date,
    es.start_time,
    es.end_time,
    es.available_slots
FROM events e
LEFT JOIN event_schedules es ON e.event_id = es.event_id;

CREATE OR REPLACE VIEW user_bookings_view AS
SELECT 
    u.username,
    e.name AS event_name,
    b.booking_date,
    b.status,
    es.schedule_date,
    es.start_time,
    es.end_time
FROM bookings b
JOIN users u ON b.user_id = u.user_id
JOIN events e ON b.event_id = e.event_id
LEFT JOIN event_schedules es ON e.event_id = es.event_id;
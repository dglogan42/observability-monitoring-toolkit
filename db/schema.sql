CREATE TABLE alerts (id SERIAL PRIMARY KEY, title TEXT, description TEXT, region TEXT, timestamp TIMESTAMPTZ);
CREATE TABLE trips (id SERIAL PRIMARY KEY, user_id INT, start TEXT, end TEXT, alerts JSONB);

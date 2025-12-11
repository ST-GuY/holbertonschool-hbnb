
CREATE TABLE IF NOT EXIST `user` {
	id CHAR(36) PRIMARY KEY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	email VARCHAR(255) UNIQUE,
	password VARCHAR(255),
	is_admin BOOLEAN DEFAULT FALSE
};

CREATE TABLE IF NOT EXIST `place` {
	id CHAR(36) PRIMARY KEY,
	title VARCHAR(255),
	description TEXT,
	price DECIMAL(10, 2),
	latitude FLOAT,
	longitude FLOAT,
	owner_id CHAR(36),
	FOREIGN KEY (owner_id) REFERENCES users(id)
};

CREATE TABLE IF NOT EXIST `review` {
    id CHAR(36) PRIMARY KEY,
    text TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    user_id CHAR(36),
    place_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES place(id),
    
    -- Empêche un utilisateur de laisser plusieurs avis sur un même lieu
    UNIQUE (user_id, place_id)
};

CREATE TABLE IF NOT EXIST `amenity` {
	id CHAR(36) PRIMARY KEY,
	name VARCHAR(255) UNIQUE
};

CREATE TABLE IF NOT EXIST `Place_Amenity` {
	place_id CHAR(36),
    amenity_id CHAR(36),

    -- Clé primaire composée
    PRIMARY KEY (place_id, amenity_id),

    -- Clés étrangères
    FOREIGN KEY (place_id) REFERENCES place(id),
    FOREIGN KEY (amenity_id) REFERENCES amenity(id)
};

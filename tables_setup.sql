CREATE TABLE Persons {
    person_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    iPhone BOOLEAN NOT NULL,
    Android BOOLEAN NOT NULL,
    Desktop BOOLEAN NOT NULL,
};

CREATE TABLE Promotions {
    promotion_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    client_email VARCHAR(255) NOT NULL,
    person_id INT NOT NULL,
    promotion_item VARCHAR(50) NOT NULL,
    responded BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
};

CREATE TABLE Transactions {
    transaction_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    person_id INT NOT NULL,
    item VARCHAR(50) NOT NULL,
    price DECIMAL NOT NULL,
    store_name VARCHAR(100) NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
}

CREATE TABLE Transfers {
    transfer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sender_id INT NOT NULL,
    recipient_id INT NOT NULL,
    transfer_amount DECIMAL NOT NULL,
    transfer_date DATE NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES Persons(person_id)
    FOREIGN KEY (recipient_id) REFERENCES Persons(person_id)
}
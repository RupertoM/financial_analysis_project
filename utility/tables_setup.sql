CREATE TABLE Persons (
    person_id INT PRIMARY KEY,
    firstName VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    Android BOOLEAN NOT NULL,
    iPhone BOOLEAN NOT NULL,
    Desktop BOOLEAN NOT NULL
);

CREATE TABLE Promotions (
    promotion_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    client_email VARCHAR(255) NOT NULL,
    telephone VARCHAR(20),
    promotion_item VARCHAR(50) NOT NULL,
    responded VARCHAR(20) NOT NULL,
    person_id INT NOT NULL,
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
);

CREATE TABLE Transactions (
    transaction_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    person_id INT NOT NULL,
    item VARCHAR(50) NOT NULL,
    price DECIMAL(4, 2) NOT NULL,
    store VARCHAR(255) NOT NULL,
    transactionDate DATE NOT NULL,
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
);

CREATE TABLE Transfers (
    transfer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sender_id INT NOT NULL,
    recipient_id INT NOT NULL,
    amount DECIMAL NOT NULL,
    transferDate DATE NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES Persons(person_id),
    FOREIGN KEY (recipient_id) REFERENCES Persons(person_id)
);

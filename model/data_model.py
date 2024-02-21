import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from collections import OrderedDict

class DataModel():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='venmito-database.ch2o2eoaqxux.us-east-1.rds.amazonaws.com',
            user='adminUser',
            password='userPassword!',
            database='venmito',
            port=3306
        )
        self.engine = create_engine('mysql+mysqlconnector://adminUser:userPassword!@venmito-database.ch2o2eoaqxux.us-east-1.rds.amazonaws.com/venmito')

    def get_clients_promotion(self):
        query = """
        SELECT p.promotion_item, p.responded, pr.firstName, pr.surname, pr.email, pr.telephone
        FROM Promotions p
        JOIN Persons pr ON p.person_id = pr.person_id
        ORDER BY p.promotion_item
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

    def get_no_response_clients(self):
        query = """
        SELECT p.promotion_item, pr.firstName, pr.surname, p.client_email, p.telephone
        FROM Promotions p
        JOIN Persons pr ON p.person_id = pr.person_id
        WHERE p.responded = "No"
        ORDER BY p.promotion_item
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_top_selling_item(self):
        query = """
        SELECT t.item, COUNT(t.item) as amount_sales
        FROM Transactions t
        GROUP BY t.item
        ORDER BY amount_sales DESC
        LIMIT 1
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

    def get_most_profitable_item(self):
        query = """
        SELECT t.item, SUM(t.price) as total_sales
        FROM Transactions t
        JOIN Persons pr ON t.person_id = pr.person_id
        GROUP BY t.item
        ORDER BY total_sales DESC
        LIMIT 1
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

    def get_most_profitable_store(self):
        query = """
        SELECT t.store, SUM(t.price) as total_profit
        FROM Transactions t
        GROUP BY t.store
        ORDER BY total_profit DESC
        LIMIT 1
        """

        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_store_insights(self):
        query = """
        SELECT t.store, SUM(t.price) as total_profit
        FROM Transactions t
        GROUP BY t.store
        ORDER BY total_profit DESC
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

    def get_transfer_insights(self):
        query = """
        SELECT sender.email as sender_email, recipient.email as recipient_email, tr.amount, tr.transferDate
        FROM Transfers tr
        JOIN Persons sender ON tr.sender_id = sender.person_id
        JOIN Persons recipient ON tr.recipient_id = recipient.person_id
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')


##SQL SCHEMA

# TABLE Persons (
#     person_id INT PRIMARY KEY,
#     firstName VARCHAR(100) NOT NULL,
#     surname VARCHAR(100) NOT NULL,
#     email VARCHAR(255) NOT NULL,
#     telephone VARCHAR(20) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     country VARCHAR(50) NOT NULL,
#     Android BOOLEAN NOT NULL,
#     iPhone BOOLEAN NOT NULL,
#     Desktop BOOLEAN NOT NULL
# );

# TABLE Promotions (
#     promotion_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     client_email VARCHAR(255) NOT NULL,
#     telephone VARCHAR(20),
#     promotion_item VARCHAR(50) NOT NULL,
#     responded VARCHAR(20) NOT NULL,
#     person_id INT NOT NULL,
#     FOREIGN KEY (person_id) REFERENCES Persons(person_id)
# );

# TABLE Transactions (
#     transaction_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     person_id INT NOT NULL,
#     item VARCHAR(50) NOT NULL,
#     price DECIMAL NOT NULL,
#     store VARCHAR(255) NOT NULL,
#     transactionDate DATE NOT NULL,
#     FOREIGN KEY (person_id) REFERENCES Persons(person_id)
# );

# TABLE Transfers (
#     transfer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     sender_id INT NOT NULL,
#     recipient_id INT NOT NULL,
#     amount DECIMAL NOT NULL,
#     transferDate DATE NOT NULL,
#     FOREIGN KEY (sender_id) REFERENCES Persons(person_id),
#     FOREIGN KEY (recipient_id) REFERENCES Persons(person_id)
# );

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

#PERSONS
    def get_all_persons(self):
        query = """
        SELECT person_id, CONCAT(firstName, ' ', surname) AS full_name, email, telephone, city, country
        FROM Persons
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_clients_promotion(self):
        query = """
        SELECT p.promotion_item, CONCAT(pr.firstName, ' ', pr.surname) AS full_name, p.responded, pr.email, pr.telephone
        FROM Promotions p
        JOIN Persons pr ON p.person_id = pr.person_id
        ORDER BY p.promotion_item
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

    def get_no_response_clients(self):
        query = """
        SELECT p.promotion_item, CONCAT(pr.firstName, ' ', pr.surname) AS full_name, p.client_email, p.telephone, GROUP_CONCAT(DISTINCT t.store) AS visited_stores
        FROM Promotions p
        JOIN Persons pr ON p.person_id = pr.person_id
        LEFT JOIN Transactions t ON p.person_id = t.person_id
        WHERE p.responded = 'No'
        GROUP BY p.promotion_item, full_name, p.client_email, p.telephone
        ORDER BY p.promotion_item, full_name
        """
        result = pd.read_sql(query, self.engine)
        #Change all null values to "None"
        result['visited_stores'] = result['visited_stores'].fillna('None')
        return result.to_dict(orient='records')
    
    def get_individuals_transactions(self):
        query = """
        SELECT CONCAT(pr.firstName, ' ', pr.surname) AS full_name, t.item, t.price, t.store, t.transactionDate
        FROM Transactions t
        JOIN Persons pr ON t.person_id = pr.person_id
        ORDER BY full_name, t.transactionDate
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_persons_favorite_store(self):
        query = """
        SELECT CONCAT(pr.firstName, ' ', pr.surname) AS full_name, t.store as favorite_store, COUNT(t.store) as visits
        FROM Transactions t
        JOIN Persons pr ON t.person_id = pr.person_id
        GROUP BY full_name, favorite_store
        ORDER BY full_name, visits DESC
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_individuals_favorite_items(self):
        query = """
        SELECT CONCAT(pr.firstName, ' ', pr.surname) AS full_name, GROUP_CONCAT(t.item) as favorite_items
        FROM Transactions t
        JOIN Persons pr ON t.person_id = pr.person_id
        GROUP BY full_name
        ORDER BY full_name
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_probable_connections(self):
        query = """
        SELECT CONCAT(sender.firstName, ' ', sender.surname) AS sender_name,
            CONCAT(recipient.firstName, ' ', recipient.surname) AS recipient_name,
            COUNT(tr.transfer_id) AS number_of_transfers, SUM(tr.amount) AS total_amount_transferred
        FROM Transfers tr
        JOIN Persons sender ON tr.sender_id = sender.person_id
        JOIN Persons recipient ON tr.recipient_id = recipient.person_id
        GROUP BY sender_name, recipient_name
        ORDER BY total_amount_transferred DESC
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

#STORES
    def get_store_insights(self):
        #Select individual items and put them in a list within "item" column
        query = """
        SELECT t.store, SUM(t.price) as total_profit_usd, COUNT(t.item) as amount_of_sales, GROUP_CONCAT(t.item) as items_sold
        FROM Transactions t
        GROUP BY t.store
        ORDER BY total_profit_usd DESC
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_top_selling_item(self):
        query = """
        SELECT store, item, amount_of_sales FROM (
            (SELECT 'Overall' AS store, t.item, COUNT(t.item) as amount_of_sales,
            ROW_NUMBER() OVER (ORDER BY COUNT(t.item) DESC) as rn
            FROM Transactions t
            GROUP BY t.item)

            UNION ALL

            (SELECT t.store, t.item, COUNT(t.item) as amount_of_sales,
            ROW_NUMBER() OVER (PARTITION BY t.store ORDER BY COUNT(t.item) DESC) as rn
            FROM Transactions t
            GROUP BY t.store, t.item)
        ) subquery
        WHERE rn = 1
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

    def get_most_profitable_items(self):
        query = """
        SELECT store, item, total_sales FROM (
            (SELECT 'Overall' AS store, t.item, SUM(t.price) as total_sales,
            ROW_NUMBER() OVER (ORDER BY SUM(t.price) DESC) as rn
            FROM Transactions t
            JOIN Persons pr ON t.person_id = pr.person_id
            GROUP BY t.item)

            UNION ALL

            (SELECT t.store, t.item, SUM(t.price) as total_sales,
            ROW_NUMBER() OVER (PARTITION BY t.store ORDER BY SUM(t.price) DESC) as rn
            FROM Transactions t
            JOIN Persons pr ON t.person_id = pr.person_id
            GROUP BY t.store, t.item)
        ) subquery
        WHERE rn = 1
        """
        result = pd.read_sql(query, self.engine)
        print(result)
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
    
    def get_best_selling_stores(self):
        query = """
        SELECT t.store, COUNT(t.item) as amount_of_sales, SUM(t.price) as total_profit
        FROM Transactions t
        GROUP BY t.store
        ORDER BY amount_of_sales DESC
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_no_response_by_item(self):
        query = """
        SELECT p.promotion_item, COUNT(p.responded) as attempts_made, GROUP_CONCAT(DISTINCT CONCAT(pr.firstName, ' ', pr.surname)) as attempted_clients
        FROM Promotions p
        JOIN Persons pr ON pr.person_id = p.person_id
        WHERE p.responded = 'No'
        GROUP BY p.promotion_item
        ORDER BY attempts_made DESC
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
    def get_yes_response_by_item(self):
        query = """
        SELECT p.promotion_item, COUNT(p.responded) as attempts_made, GROUP_CONCAT(DISTINCT CONCAT(pr.firstName, ' ', pr.surname)) as attempted_clients
        FROM Promotions p
        JOIN Persons pr ON pr.person_id = p.person_id
        WHERE p.responded = 'Yes'
        GROUP BY p.promotion_item
        ORDER BY attempts_made DESC
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')

#TRANSFERS
    def get_transfer_insights(self):
        query = """
        SELECT sender.email as sender_email, recipient.email as recipient_email, tr.amount, tr.transferDate
        FROM Transfers tr
        JOIN Persons sender ON tr.sender_id = sender.person_id
        JOIN Persons recipient ON tr.recipient_id = recipient.person_id
        """
        result = pd.read_sql(query, self.engine)
        return result.to_dict(orient='records')
    
#TRANSACTIONS
    def get_all_transactions(self):
        query = """
        SELECT t.transaction_id, pr.firstName, pr.surname, t.item, t.price, t.store, t.transactionDate
        FROM Transactions t
        JOIN Persons pr ON t.person_id = pr.person_id
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

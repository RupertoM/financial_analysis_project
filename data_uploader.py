import mysql.connector
from sqlalchemy import create_engine

class DataUploader:
    def __init__(self, people_df, promotions_df, transactions_df, transfers_df):
        # Initialize DataFrames
        self.people = people_df
        self.promotions = promotions_df
        self.transactions = transactions_df
        self.transfers = transfers_df

        # Set up AWS MySQL connection
        self.connection = mysql.connector.connect(
            host='venmito-database.ch2o2eoaqxux.us-east-1.rds.amazonaws.com',
            user='adminUser',
            password='userPassword!',
            database='venmito',
            port=3306
        )
        self.engine = create_engine('mysql+mysqlconnector://adminUser:userPassword!@venmito-database.ch2o2eoaqxux.us-east-1.rds.amazonaws.com/venmito')

        # Create tables
        self.setup_tables()
        
        #Populate tables
        self.upload_data()

        # #Check data
        # self.check_data()

    def setup_tables(self):
        try:
            with open('tables_setup.sql', 'r') as file:
                sql_script = file.read()

            cursor = self.connection.cursor()

            # Drop tables if they already exist
            cursor.execute("DROP TABLE IF EXISTS Persons, Promotions, Transactions, Transfers;")
            self.connection.commit()

            # Create SQL tables
            sql_commands = sql_script.split(';')
            for command in sql_commands:
                if command.strip() != '':
                    cursor.execute(command)
                    self.connection.commit()

            cursor.close()

            print("Tables successfully created.")

        except Exception as e:
            print(f"Error setting up tables: {e}")

    def upload_data(self):
        try:
            # Upload Persons data
            self.upload_to_mysql(self.people, 'Persons')

            # Upload Promotions data
            self.upload_to_mysql(self.promotions, 'Promotions')

            # Upload Transactions data
            self.upload_to_mysql(self.transactions, 'Transactions')

            # Upload Transfers data
            self.upload_to_mysql(self.transfers, 'Transfers')

            print("Data upload to MySQL successful.")

        except Exception as e:
            print(f"Error uploading data to MySQL: {e}")

    def upload_to_mysql(self, df, table_name):
        try:
            df.to_sql(table_name, con=self.engine, if_exists='append', index=False)
            print(f"Data uploaded to {table_name} successfully.")
        except Exception as e:
            print(f"Error uploading data to {table_name}: {e}")
    
    # def check_data(self):
    #     try:
    #         queries = [
    #             "SELECT * FROM Persons;",
    #             "SELECT * FROM Promotions;",
    #             "SELECT * FROM Transactions;",
    #             "SELECT * FROM Transfers;",
    #             "SELECT firstName FROM Persons"
    #         ]

    #         for query in queries:
    #             result = self.connection.cursor()
    #             result.execute(query)
    #             data = result.fetchall()
    #             print(data)
    #             print("\n")

    #         print("Data check successful.")

    #     except Exception as e:
    #         print(f"Error checking data: {e}")
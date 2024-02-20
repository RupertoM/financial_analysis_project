from flask import Flask
import sys
from data_processor import DataProcessor
from data_uploader import DataUploader

app = Flask(__name__)

# Base function as filler (REMOVE)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    # Check for database creation argument
    # if len(sys.argv) > 1 and sys.argv[1] == "--restart-db":
        #Process Data using DataProcessor
        data_processor = DataProcessor()
        persons, promotions, transactions, transfers = data_processor.get_processed_data()

        # #Upload Data to AWS MySQL using DataUploader
        DataUploader(persons, promotions, transactions, transfers)

    # # Run the Flask app
    # app.run()

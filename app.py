from flask import Flask, jsonify
from flask_cors import CORS
import sys
from utility.data_processor import DataProcessor
from utility.data_uploader import DataUploader
from controller.data_controller import DataController

app = Flask(__name__)
CORS(app)

app.json.sort_keys = False
DC = DataController()

#PERSONS
@app.route('/api/PersonsTable', methods=['GET'])
def get_persons_data():
    return jsonify(DC.get_all_persons())

@app.route('/api/ClientPromotionsTable', methods=['GET'])
def get_promotion_data():
    return jsonify(DC.get_clients_promotion())

@app.route('/api/NoResponseTable', methods=['GET'])
def get_no_response_data():
    return jsonify(DC.get_no_response_clients())

@app.route('/api/NoResponseByItemTable', methods=['GET'])
def get_no_response_by_item():
    return jsonify(DC.get_no_response_by_item())

@app.route('/api/FavoriteItemsTable', methods=['GET'])
def get_individuals_favorite_items():
    return jsonify(DC.get_individuals_favorite_items())

@app.route('/api/ProbableConnectionsTable', methods=['GET'])
def get_probable_connections():
    return jsonify(DC.get_probable_connections())

#STORES
@app.route('/api/TopSellingItemTable', methods=['GET'])
def get_top_selling_item():
    return jsonify(DC.get_top_selling_item())

@app.route('/api/MostProfitableItemsTable', methods=['GET'])
def get_most_profitable_item():
    return jsonify(DC.get_most_profitable_items())

@app.route('/api/MostProfitableStore', methods=['GET'])
def get_most_profitable_store():
    return jsonify(DC.get_most_profitable_store())

@app.route('/api/StoreInsightsTable', methods=['GET'])
def get_store_insights():
    return jsonify(DC.get_store_insights())

@app.route('/api/BestSellingStoresTable', methods=['GET'])
def get_best_selling_stores():
    return jsonify(DC.get_best_selling_stores())

@app.route('/api/SuccessfulPromotionsTable', methods=['GET'])
def get_yes_response_by_item():
    return jsonify(DC.get_yes_response_by_item())

#TRANSFERS
@app.route('/api/TransferInsightsTable', methods=['GET'])
def get_transfer_insights():
    return jsonify(DC.get_transfer_insights())

#TRANSACTIONS
@app.route('/api/TransactionInsightsTable', methods=['GET'])
def get_transaction_insights():
    return jsonify(DC.get_all_transactions())

@app.route('/api/IndividualTransTable', methods=['GET'])
def get_shopping_history():
    return jsonify(DC.get_individuals_transactions())

@app.route('/api/FavoriteStoreTable', methods=['GET'])
def get_favorite_stores():
    return jsonify(DC.get_person_favorite_store())

if __name__ == "__main__":
    # Check for database reset argument
    if len(sys.argv) > 1 and sys.argv[1] == "--reset-db":
        #Process Data using DataProcessor
        data_processor = DataProcessor()
        persons, promotions, transactions, transfers = data_processor.get_processed_data()

        # #Upload Data to AWS MySQL using DataUploader
        DataUploader(persons, promotions, transactions, transfers)

    # Run the Flask app
    app.run()
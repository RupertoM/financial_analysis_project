from model.data_model import DataModel
from flask import jsonify
from collections import OrderedDict

data_model = DataModel()

class DataController():

    def get_clients_promotion(self):
        return data_model.get_clients_promotion()
    
    def get_no_response_clients(self):
        return data_model.get_no_response_clients()
    
    def get_top_selling_item(self):
        top_selling_item_data = data_model.get_top_selling_item()
        if top_selling_item_data:
            top_item = top_selling_item_data[0]
            output_string = f"The top selling item is {top_item['item']}s with {round(top_item['amount_sales'], 2)} sales."
            return output_string
        else:
            return "No data available."
    
    def get_most_profitable_item(self):
        most_profitable_data = data_model.get_most_profitable_item()
        if most_profitable_data:
            most_profitable = most_profitable_data[0]
            output_string = f"The most profitable item is {most_profitable['item']}s with ${round(most_profitable['total_sales'], 2)} in revenue."
            return output_string
        else:
            return "No data available."
        
    def get_most_profitable_store(self):
        most_profitable_store_data = data_model.get_most_profitable_store()
        if most_profitable_store_data:
            top_store = most_profitable_store_data[0]
            output_string = f"The most profitable store is {top_store['store']} with ${int(top_store['total_profit'])} in sales."
            return output_string
        else:
            return "No data available."
        
    def get_store_insights(self):
        store_insights_data = data_model.get_store_insights()
        if store_insights_data:
            return store_insights_data
        else:
            return "No data available."
        
    def get_transfer_insights(self):
        transfer_insights_data = data_model.get_transfer_insights()
        if transfer_insights_data:
            return transfer_insights_data
        else:
            return "No data available."
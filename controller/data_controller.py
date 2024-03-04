from model.data_model import DataModel
data_model = DataModel()

class DataController():

#PERSONS
    def get_all_persons(self):
        return data_model.get_all_persons()
    
    def get_clients_promotion(self):
        return data_model.get_clients_promotion()
    
    def get_no_response_clients(self):
        return data_model.get_no_response_clients()
    
    def get_individuals_favorite_items(self):
        return data_model.get_individuals_favorite_items()
    
    def get_probable_connections(self):
        return data_model.get_probable_connections()
    
    def get_individuals_transactions(self):
        return data_model.get_individuals_transactions()
    
    def get_person_favorite_store(self):
        return data_model.get_persons_favorite_store()

#STORES   
    def get_store_insights(self):
        store_insights_data = data_model.get_store_insights()
        if store_insights_data:
            return store_insights_data
        else:
            return "No data available."
        
    def get_top_selling_item(self):
        return data_model.get_top_selling_item()
    
    def get_most_profitable_items(self):
        return data_model.get_most_profitable_items()
        
    def get_most_profitable_store(self):
        most_profitable_store_data = data_model.get_most_profitable_store()
        if most_profitable_store_data:
            top_store = most_profitable_store_data[0]
            output_string = f"The most profitable store is {top_store['store']} with ${top_store['total_profit']:.2f} in sales."
            return output_string
        else:
            return "No data available."
        
    def get_best_selling_stores(self):
        return data_model.get_best_selling_stores()
    
    def get_no_response_by_item(self):
        return data_model.get_no_response_by_item()
    
    def get_yes_response_by_item(self):
        return data_model.get_yes_response_by_item()

#TRANSFERS        
    def get_transfer_insights(self):
        transfer_insights_data = data_model.get_transfer_insights()
        if transfer_insights_data:
            return transfer_insights_data
        else:
            return "No data available."
        
#TRANSACTIONS
    def get_all_transactions(self):
        return data_model.get_all_transactions()
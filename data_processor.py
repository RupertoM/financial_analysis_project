import json
import yaml
import pandas as pd

class DataProcessor():
    def __init__(self):
        self._process_persons_data()
        self._process_promotions_data()
        self._process_transactions_data()
        self._process_transfer_data()

    def _process_persons_data(self):
         # Load JSON data into a DataFrame
        with open('data/people.json') as json_file:
            json_data = json.load(json_file)
        json_df = pd.json_normalize(json_data['people'])

        #Sanitize JSON data
        json_df['id'] = pd.to_numeric(json_df['id'], errors='coerce')
        json_df.rename(columns={'location.city': 'city'}, inplace=True)
        json_df.rename(columns={'location.country': 'country'}, inplace=True)
        devices_columns = pd.json_normalize(json_df['devices'].apply(lambda x: {device: True for device in x}).tolist()).fillna(False).infer_objects(copy=False)
        json_df = pd.concat([json_df, devices_columns], axis=1)
        json_df.drop(['devices'], axis=1, inplace=True)
        
        # Load YAML data into a DataFrame
        with open('data/people.yml') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
        yaml_df = pd.json_normalize(yaml_data['people'])

        #Sanitize YAML data
        yaml_df[['city', 'country']] = yaml_df['city'].str.split(',', expand=True)
        yaml_df[['firstName', 'surname']] = yaml_df['name'].str.split(' ', expand=True)
        yaml_df.rename(columns={'phone': 'telephone'}, inplace=True)
        #Remove redundant columns
        yaml_df.drop(['name'], axis=1, inplace=True)


        # Merge JSON and YAML data
        person_df = pd.concat([json_df, yaml_df], ignore_index=True)
        person_df.drop_duplicates(subset=['id'], inplace=True)
        person_df.reset_index(drop=True, inplace=True)
        person_df.sort_values(by=['id'], inplace=True)

        self.shared_people_df = person_df

    def _process_promotions_data(self):
        #Load CSV data into a DataFrame
        promotions_df = pd.read_csv('data/promotions.csv')

        #Resolve the person id related to each record and append it to the DataFrame
        list_of_ids = []
        for i in range(len(promotions_df)):
            registered_email = promotions_df.loc[i, 'client_email']

            #Check if the email is registered
            if registered_email != "''":
                person_row = self.shared_people_df[self.shared_people_df['email'] == registered_email]
                list_of_ids.append(person_row['id'].values[0])
            
            #Otherwise, check if the telephone is registered
            else:
                registered_number = self.shared_people_df.loc[i, 'telephone']
                person_row = self.shared_people_df[self.shared_people_df['telephone'] == registered_number]
                list_of_ids.append(person_row['id'].values[0])
            
        #Append the person id to the DataFrame in order of promotion_id (row number)
        promotions_df['person_id'] = list_of_ids

    def _process_transactions_data(self):
        #Load CSV data into a DataFrame
        transactions_df = pd.read_xml('data/transactions.xml')

        #Resolve the person id related to each transaction and append it to the DataFrame
        list_of_ids = []

        for i in range(len(transactions_df)):
            first_initial = transactions_df.loc[i, 'buyer_name'][0]
            last_name = transactions_df.loc[i, 'buyer_name'][3:]

            person_row = self.shared_people_df[(self.shared_people_df['firstName'].str[0] == first_initial) & (self.shared_people_df['surname'] == last_name)]
            list_of_ids.append(person_row['id'].values[0])

        #Append the person id to the DataFrame in order of transaction_id (row number)
        transactions_df['person_id'] = list_of_ids

    #Transfer data already includes the person id, so no need to sanitize data
    def _process_transfer_data(self):
        #Load CSV data into a DataFrame
        transfers_df = pd.read_csv('data/transfers.csv')


if __name__ == "__main__":
    processor = DataProcessor()
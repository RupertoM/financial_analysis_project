import json
import yaml
import pandas as pd

class DataProcessor():
    def __init__(self):
        self._process_persons_data()


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

        print(person_df)

if __name__ == "__main__":
    processor = DataProcessor()
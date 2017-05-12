from algorithms.factorization_machine import FactorizationMachine
from algorithms.latent_dirichlet_allocation import LatentDirichletAllocation
from app.config import db
from app.config.config import engine
import datetime
import numpy as np
import pandas as pd

class Engine:

    def __init__(self):
        self.users_to_int = {}
        self.items_to_int = {}
        self.users_to_int_counter = 0
        self.items_to_int_counter = 0

    def load_data(self):
        '''
            Loads the data from the data source
        '''        

        today = datetime.datetime.today()
        query = {
            "range": {
                "created_at": {
                    "gte": (today - datetime.timedelta(days=engine["training_data_age"])).strftime("%Y-%m-%d"),
                    "lte": today.strftime('%Y-%m-%d')
                }
            }
        }

        #TODO investigate performance of scroll instead of fetching large records in one go
        res = db.es.search(index="events", body={"query": query}, size=1000000)
        events = []
        data = res["hits"]["hits"]

        # #check the dtype of the essential features
        # first_record = record[0]["_source"]

        # if type(first_record["user"]) == "string":
        #     users_to_int = self.transform_feature_to_int()
        
        # if type(first_record["item"]) == "string":
        #     items_to_int = self.transform_feature_to_int()

        for record in data:
            event = record["_source"]            
            events.append((self.transform_feature_to_int(event["user"]), self.transform_feature_to_int(event["item"], "item"), event["rating"])
            + self.apply_feature_engineering(event["created_at"], "date"))
        print np.array(events).shape
        return np.array(events)

    def transform_feature_to_int(self, feature, type='user'):
        '''
            Assigns a unique integer to an element in a feature
        '''
        if type == 'user':
            if feature not in self.users_to_int:
                self.users_to_int[feature] = self.users_to_int_counter
                self.users_to_int_counter += 1
            return self.users_to_int_counter
        
        else:
            if feature not in self.items_to_int:
                self.items_to_int[feature] = self.items_to_int_counter
                self.items_to_int_counter += 1
            return self.items_to_int_counter

    def apply_feature_engineering(self, feature, type="date"):
        if type == "date":
            transformed_feature = pd.to_datetime(feature)
            return (transformed_feature.year, transformed_feature.month, transformed_feature.day)

    def train(self):
        fm = FactorizationMachine()
        events = self.load_data()
        features = events[:, 0:events.shape[1] - 1] #means to select every data in every row for the first and second to last column
        target = events[:, -1] #selects every data in every row for the last column
        fm.fit(features, target)

    def get_recommendations(self):
        fm.predict(features)
    
    def save_recommendations(self):
        pass
        
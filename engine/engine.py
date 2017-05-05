from algorithms.factorization_machine import FactorizationMachine
from algorithms.latent_dirichlet_allocation import LatentDirichletAllocation
from app.config import db
from app.config.config import engine
import datetime
import numpy as np

class Engine:

    def load_data(self):
        
        today = datetime.datetime.today()
        query = {
            "range": {
                "created_at": {
                    "gte": (today - datetime.timedelta(days=engine["training_data_age"])).strftime("%Y-%m-%d"),
                    "lte": today.strftime('%Y-%m-%d')
                }
            }
        }
        res = db.es.search(index="events", body={"query": query})
        events = []
        data = res["hits"]["hits"]  
        for record in data:
            event = record["_source"]
            events.append((event["user"], event["item"], event["created_at"], event["quantity"]))
        print np.array(events).shape
        return np.array(events)

    def apply_feature_engineering(self):
        pass

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
        
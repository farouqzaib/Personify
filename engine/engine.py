from algorithms.factorization_machine import FactorizationMachine
from algorithms.latent_dirichlet_allocation import LatentDirichletAllocation
from app.config import db
from app.config.config import engine
import datetime

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
        return res["hits"]["hits"]

    def apply_feature_engineering(self):
        pass

    def train(self):
        pass

    def get_recommendations(self):
        pass
    
    def save_recommendations(self):
        pass
        
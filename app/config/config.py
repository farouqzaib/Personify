import os

db = {
	'host': os.getenv('host', '127.0.0.1'),
	'port': os.getenv('port', '')
}

engine = {
	'training_data_age': 100 #specifies in days how much data to be used for training
}
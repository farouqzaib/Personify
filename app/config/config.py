import os

db = {
	'host': os.getenv('host', '127.0.0.1'),
	'port': os.getenv('port', '')
}
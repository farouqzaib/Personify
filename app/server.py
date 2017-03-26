from config import db
from flask import Flask
from routes import register_routes

app = Flask('app')

app.debug = True

register_routes(app)

#controllers

#views

#services

if __name__ == "__main__":
    app.run()


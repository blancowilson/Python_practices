from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:010117@localhost:3007/CONCTACSDB'
app.config['SQLALCHEMY_DATABASE_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)
app.register_blueprint(contacts)




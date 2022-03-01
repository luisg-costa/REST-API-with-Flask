from flask import Flask
from flask_restful import Api #type: ignore
from flask_jwt import JWT #type: ignore

from security import authenticate, identity
from resources.user import UserRegister, User
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "sdfkdfsl23FSDvssfasf56332fdsdD"
# to change authentication URL from /auth
# app = config['JWT_AUTH_URL_RULE'] = '/login'

# to change token expiration time
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)


api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth


api.add_resource(Item,'/item/<string:name>') 
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(User,'/user/<int:user_id>' )

if __name__ == "__main__":
    db.init_app(app)
    app.debug = True
    app.run(port=5000)

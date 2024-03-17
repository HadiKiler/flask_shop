from flask import Flask ,jsonify
from initialize import db
from admin.routes import *
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config.from_object('config.DevConfig') 
db.init_app(app) 

app.register_blueprint(user_blueprint)


from admin.models import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
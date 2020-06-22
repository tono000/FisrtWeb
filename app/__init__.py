from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap 
from wtforms import Form, StringField, SelectField
from elasticsearch import Elasticsearch


bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app



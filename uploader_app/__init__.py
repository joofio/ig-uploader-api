"""Flask app for starting server."""

from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
app.config["SWAGGER"] = {
    "swagger": "2.0",
    "info": {
        "title": "Audit+",
        "description": "Audit+ API",
        "contact": {
            "responsibleOrganization": "Audit+",
            "responsibleDeveloper": "Joao Almeida",
        },
        "termsOfService": "http://me.com/terms",
        "version": "0.0.1",
    },
    # "host": "http://bibliovigilancia.gim.med.up.pt/",  # overrides localhost:5000
    "basePath": "api",  # base bash for blueprint registration
    "schemes": ["http", "https"],
}
swagger = Swagger(app, template=app.config["SWAGGER"])


import uploader_app.views

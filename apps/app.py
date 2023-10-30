from flask import Flask

def initialize():
  app = Flask(__name__)

  # register Blueprint for root
  from apps.root import views as root_views
  app.register_blueprint(root_views.root)

  return app
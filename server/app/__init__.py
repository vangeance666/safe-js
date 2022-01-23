from flask import Flask, render_template

def create_app():
	app = Flask(__name__)
	
	from app.views.main_view import main_view
	from app.views.api_view import api_view 

	app.register_blueprint(main_view, url_prefix='/') # Dashboard Etc
	app.register_blueprint(api_view, url_prefix='/api/') # API to do backendstuffs
	
	return app

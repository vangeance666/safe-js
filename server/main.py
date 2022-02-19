from app import create_app

# def main():
# 	my_app = create_app()
# 	my_app.run(debug=True, port=5000)

# from analyzer.datatypes.js_file import JsFile
# from analyzer.datatypes.page import Page
# from analyzer.features.javascript.static.func_search_count import FuncSearchCount

# from analyzer.controllers.features_controller import FeaturesController
# import analyzer
# 
# import analyzer
# from analyzer.features.javascript.static import *


from analyzer.controllers.features_controller import FeaturesController

if __name__ == '__main__':
	# t = JsFile()
	# p = Page()
	
	C = FeaturesController()

	print(C.get_static_features())



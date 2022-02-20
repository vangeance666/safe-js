from app import create_app


from analyzer.controllers.features_controller import FeaturesController

if __name__ == '__main__':
	
	C = FeaturesController()

	# C.get_static_features()
	print("C.get_static_features(): ", C.get_static_features())



import os
import numpy as np
from analyzer.net.test import InferenceNet
from config import NET_MODELS_FOLDER

from analyzer.core.dataset_generator import DatasetGenerator
class InferenceController:

	MODEL_EXT = ".npz"
	def __init__(self, model_folder=None):
		self._model_folder = model_folder or NET_MODELS_FOLDER
		self._dataset_generator = DatasetGenerator()

	def get_models(self) -> list:
		return [file for file in os.listdir(self._model_folder) if file.endswith(self.MODEL_EXT)]
	
	def predict(self, js_file, model_name="c-1.npz"):
		inference_net = InferenceNet(checkpoint_path=os.path.join(self._model_folder, model_name))
		row_dict = self._dataset_generator.eval_js_file_row(js_file)
		predict_data = np.array(list(row_dict.values())[1:])
		js_file.malign_percent = inference_net.run(predict_data)

		if js_file.malign_percent != 0.0:
			js_file.model_predicted = True
			js_file.model_used = model_name






		
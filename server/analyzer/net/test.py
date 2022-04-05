import os
import sys
from analyzer.net.dataset import *
# from dataset import *
# from malware_classify.dataset import *
# from dataset import *
checkpoint_path = 'checkpoints.kn/c-5.npz'

# checkpoint_path = os.path.join(os.getcwd()+'malware_classify/checkpoints.kn/c-0.npz')

class InferenceNet(object):
	
	def __init__(self, checkpoint_path):
		
		kwds = np.load(checkpoint_path)
		self._layers = {}
		net_name = 'net'
		p = len(net_name + '/')
		for _k in kwds:
			self._layers[_k[p:].split(':')[0]] = kwds[_k]
		
		self._sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))
		self._relu = lambda x:np.maximum(x, 0)
		self._dense = lambda x,name: (
			np.matrix(self._layers[name + '/kernel']).transpose() * x
			+ np.matrix(self._layers[name + '/bias']).transpose() )
		
		def softmax(x):
			e_x = np.exp(x - np.max(x))
			return e_x / e_x.sum(axis=0) 

		self._softmax = softmax
	
	def run(self, x):
		x = self._layers['m'] * x + self._layers['c']
		x = np.reshape(x, [-1, 1])

		x = self._dense(x, 'pre_layer')
		x = self._relu(x)

		for i in range(self._layers['num_residual_blocks']):
			fx = self._dense(x, 'res_layer_a_' + str(i))
			fx = self._relu(fx)
			fx = self._dense(fx, 'res_layer_a_' + str(i))
			x = fx + x

		x = self._dense(x, 'post_layer')
		x = self._sigmoid(x)
		
		is_malign_logits = self._dense(x, 'layers_is_malign')
		is_malign_sigmoid = self._sigmoid(is_malign_logits)

		return float(is_malign_sigmoid)

if __name__ == '__main__':

	inferenceNet = InferenceNet(checkpoint_path)

	# Let's just get a random test sample.
	dataset = Dataset()

	for i in range(10):
		inputs, is_malign = dataset.test.get_batch(1)
		print("inputs: ", inputs, type(inputs))
		

		print(inferenceNet.run(inputs))
		break

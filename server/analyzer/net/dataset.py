import numpy as np
import csv, re, os, sys
from functools import reduce

class Dataset(object):

	def __init__(self):

		print("Loading dataset...")

		file_name = os.getcwd() + '/combined_kevin.csv'

		def md5_file(file_name):
			import hashlib
			hash_md5 = hashlib.md5()
			with open(file_name, 'rb') as f:
				for c in iter(lambda: f.read(4096), b""):
					hash_md5.update(c)
			return hash_md5.hexdigest()

		file_hash = md5_file(file_name)
		serialized_file_name = 'cc_' + file_hash + '.npz'
		
		X = []
		Y_is_malign = []

		is_malign_index = 1
		features_start_index = is_malign_index + 1

		labels = None
		s = 0
		self._data = {'train': [], 'test': [], 'all': []}
		self._mode = 'all'

		if os.path.exists(serialized_file_name):
			
			print("Found serialized dataset cache!")
			
			loaded = np.load(serialized_file_name)
			X = loaded['X']
			Y_is_malign = loaded['Y_is_malign']

		else:
			
			print("Parsing CSV...")
			
			with open(file_name, 'r') as f:
				reader = csv.reader(f)
				for i, line in enumerate(reader):
					if i > 0:
						Y_is_malign.append([float(line[is_malign_index])])
						X.append([float(x) for x in 
							line[features_start_index:]])
			
			X = np.array(X, dtype=np.float32)
			Y_is_malign = np.array(Y_is_malign, dtype=np.float32)
			
			print("Saving serialized dataset cache...")

			np.savez_compressed(serialized_file_name, 
				X=X, 
				Y_is_malign=Y_is_malign)

		def get_random_iter(mode):
			while 1:
				# We only get the range, not the data
				order = np.arange(len(self._data[mode]['X']))
				np.random.shuffle(order)
				for i in order:
					yield i

		self._iters = {}
		
		np.random.seed(12345)
		order = np.arange(len(X))
		np.random.shuffle(order)
		X = X[order]
		Y_is_malign = Y_is_malign[order]

		q = int(0.8 * len(X))

		self._data['train'] = {
			'X': X[:q], 
			'Y_is_malign': Y_is_malign[:q], 
		}
		self._data['test'] = {
			'X': X[q:], 
			'Y_is_malign': Y_is_malign[q:], 
		}
		self._data['all'] = {
			'X': X, 
			'Y_is_malign': Y_is_malign,
		}

		for k in self._data:
			self._iters[k] = iter(get_random_iter(k))

		print("Dataset Loaded!")
	
	@property
	def all(self):
		self._mode = 'all'
		return self

	@property
	def train(self):
		self._mode = 'train'
		return self

	@property
	def test(self):
		self._mode = 'test'
		return self

	def __call__(self, m):
		self._mode = m
		return self

	@property
	def X(self):
		return self._data[self._mode]['X']

	@property
	def Y_is_malign(self):
		return self._data[self._mode]['Y_is_malign']

	@property
	def K(self):
		return self.X.shape[-1]

	def get_batch(self, batch_size=10):
		indices = [next(self._iters[self._mode]) for i in range(batch_size)]
		return self.X[indices], self.Y_is_malign[indices]
	
		
class MinMaxNormalizer(object):
	
	def __init__(self, X):
		upper = np.max(X, axis=0)
		lower = np.min(X, axis=0)

		diff = upper - lower

		m = 1 / (diff + np.array(diff < 1e-5, dtype=np.float))
		self.m = m
		self.c = -lower * m

	def apply(self, Y):
		return self.m * Y + self.c


class NPZSaver(object):
	
	def __init__(self, net):
		self._net = net
	
	def save(self, session, f):
		np.savez_compressed(f, **dict((v.name, session.run(v)) for v in self._net.variables))
	
	def restore(self, session, f):
		kwds = np.load(f)
		for v in self._net.variables:
			if v.name in kwds:
				#print v.name
				session.run(v.assign(kwds[v.name]))

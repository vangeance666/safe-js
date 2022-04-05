import tensorflow.compat.v1 as tf
# import tensorflow as tf
import os 
import math 

tf.disable_v2_behavior()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
# tf.logging.set_verbosity(tf.logging.ERROR)

from dataset import *

class Net(object):

	def __init__(self, x, m, c, num_residual_blocks=2, layer_width=16):

		self.name = 'net'
		self.training = tf.placeholder_with_default(False, shape=None)
		
		with tf.variable_scope(self.name) as scope:

			tf.Variable(m, trainable=False, name='m')
			tf.Variable(c, trainable=False, name='c')

			tf.Variable(num_residual_blocks, trainable=False, name='num_residual_blocks')
			tf.Variable(layer_width, trainable=False, name='layer_width')
			
			x = m * x + c

			i = 0

			x = tf.layers.dense(x, layer_width, name='pre_layer')
			x = tf.nn.relu(x)

			while i < num_residual_blocks:
				fx = tf.layers.dense(x, layer_width, name='res_layer_a_' + str(i))
				fx = tf.nn.relu(fx)
				fx = tf.layers.dense(x, layer_width, name='res_layer_b_' + str(i))
				x = fx + x
				i += 1

			x = tf.nn.dropout(x, tf.cond(self.training, lambda:0.5, lambda:1.0))

			x = tf.layers.dense(x, layer_width, name='post_layer')
			x = tf.nn.sigmoid(x)

			self.is_malign_logits = tf.layers.dense(x, 1, name='layers_is_malign')
			self.is_malign_sigmoid = tf.nn.sigmoid(self.is_malign_logits)

	@property
	def variables(self): return tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, self.name)
	@property
	def kernels(self): return [v for v in self.variables if 'kernel' in v.name[:v.name.rfind(':')].split('/')]
	@property
	def biases(self): return [v for v in self.variables if v.name[:v.name.rfind(':')].split('/')]
	@property
	def total_params(self): return sum(reduce(lambda a,b:a*b, v.get_shape().as_list(), 1) for v in self.variables)	
	@property
	def saver(self): return tf.train.Saver(self.variables)
	@property
	def npz_saver(self): return NPZSaver(self)



if __name__ == '__main__':

	P = dict()
	dataset = Dataset()

	batch_size = 32

	try:
		tf.compat.v1.disable_eager_execution()
	except Exception as e:
		pass


	P['inputs'] =  tf.placeholder(dtype=tf.float32, shape=[batch_size, dataset.K])
	P['learning_rate'] = tf.placeholder(dtype=tf.float32)
	P['is_malign_labels'] =  tf.placeholder(dtype=tf.float32, shape=[batch_size, 1])

	normalizer = MinMaxNormalizer(dataset.all.X)

	net = Net(P['inputs'], normalizer.m, normalizer.c)

	P['is_malign_correct_prediction'] = tf.clip_by_value(
		(P['is_malign_labels'] - 0.5) * (net.is_malign_sigmoid - 0.5) * 1e5, 0.0, 1.0)

	P['is_malign_accuracy'] = tf.reduce_mean(P['is_malign_correct_prediction'])

	P['is_malign_nll_loss'] = tf.reduce_mean(
			tf.nn.sigmoid_cross_entropy_with_logits(
				logits=net.is_malign_logits, labels=P['is_malign_labels']))

	P['combined_loss'] = P['is_malign_nll_loss']

	with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):

		P['train'] = tf.train.AdamOptimizer(P['learning_rate'], epsilon=1e-8).minimize(P['combined_loss'])

	P['combined_stats'] = tf.stack([
		P['is_malign_nll_loss'],
		P['is_malign_accuracy'],
	], axis=0)

	WEIGHT_DECARY_FACTOR = 0.01
	PRINT_INTERVAL = 256
	SAVE_INTERVAL = 2048
	EVAL_INTERVAL = 1
	NUM_BATCHES = 16384

	P['noisy_l2_reg'] = tf.add_n([tf.nn.l2_loss(w * 
		tf.random_normal(w.shape, mean=1.0, stddev=0.1, dtype=tf.float32)) 
		for w in net.kernels]) 

	P['weights_decay'] = tf.train.GradientDescentOptimizer(
		P['learning_rate'] * WEIGHT_DECARY_FACTOR).minimize(P['noisy_l2_reg'])

	checkpoints_dir = 'checkpoints.kn'
	if not os.path.exists(checkpoints_dir):
		os.makedirs(checkpoints_dir)

	def get_session():
		config = tf.ConfigProto(device_count={'GPU':0})
		config.gpu_options.allow_growth=True
		return tf.Session(config=config)

	with get_session() as session:
		
		def get_stats(mode):
			is_malign_nll_loss = 0 
			is_malign_accuracy = 0
			t = 10
			for d in range(t):
				inputs, is_malign = dataset(mode).get_batch(batch_size)
				feed_dict = {
					net.training: False,
					P['inputs']: inputs, 
					P['is_malign_labels']: is_malign, 
				}			
				combined_stats = session.run(P['combined_stats'], feed_dict=feed_dict)
				is_malign_nll_loss += combined_stats[0]
				is_malign_accuracy += combined_stats[1]

			return {
				'is_malign_nll_loss': is_malign_nll_loss / float(t),
				'is_malign_accuracy': is_malign_accuracy / float(t),
			}

		
		batch_index = 0
		learning_step = 0
		session.run(tf.global_variables_initializer())

		checkpoint_num = 0
		has_evaled = False

		print('Network total params: {}'.format(net.total_params))

		learning_rate_annealing_period = 32
		learning_rate_base = 0.001
		learning_rate_decayer = 1.0

		while batch_index < NUM_BATCHES:
			
			learning_rate = max(1e-9, learning_rate_base * learning_rate_decayer *
				math.cos(learning_step / learning_rate_annealing_period))
			
			if learning_step / learning_rate_annealing_period > 0.5 * math.pi:
				learning_step = 0 
				learning_rate_annealing_period *= 2
				learning_rate_decayer *= 0.8
				
				EVAL_INTERVAL *= 2 
				EVAL_INTERVAL = min(256, EVAL_INTERVAL)

			learning_step += 1

			batch_index += 1

			if batch_index and batch_index % PRINT_INTERVAL == 0:				
				s = get_stats('train')
				print('Batch: '+ str(batch_index))
				print('  Train:')
				print('    is_malign_nll_loss: ' + str(s['is_malign_nll_loss']))
				print('    is_malign_accuracy: ' + str(s['is_malign_accuracy']))
				s = get_stats('test')
				print('  Test:')
				print('    is_malign_nll_loss: ' + str(s['is_malign_nll_loss']))
				print('    is_malign_accuracy: ' + str(s['is_malign_accuracy']))

			inputs, is_malign = dataset.train.get_batch(batch_size)
			feed_dict = {
				net.training: True,
				P['inputs']: inputs, 
				P['is_malign_labels']: is_malign, 
				P['learning_rate']: learning_rate
			}
			
			session.run(P['train'], feed_dict=feed_dict)
			session.run(P['weights_decay'], feed_dict=feed_dict)

			if batch_index and batch_index % EVAL_INTERVAL == 0:
				if not has_evaled:
					has_evaled = True
					with open(checkpoints_dir+'/accuracies.txt', 'w') as f:
						f.write('')
				s = get_stats('train')
				train_stats_str = (
					str(s['is_malign_nll_loss']) + ',' +
					str(s['is_malign_accuracy'])
				)
				s = get_stats('test')
				test_stats_str = (
					str(s['is_malign_nll_loss']) + ',' +
					str(s['is_malign_accuracy'])
				)
				with open(checkpoints_dir+'/accuracies.txt', 'a') as f:
					f.write(
						str(batch_index) + ';' + 
						train_stats_str + ';' + 
						test_stats_str + ';' + 
						str(learning_rate) + '\n'
					)

			if batch_index and batch_index % SAVE_INTERVAL == 0:
				print('saving checkpoint {}...'.format(checkpoint_num))
				net.npz_saver.save(session, checkpoints_dir+'/c-{}.npz'.format(checkpoint_num))
				print('checkpoint saved!')
				checkpoint_num += 1

		# batch index, same, same, learning rate



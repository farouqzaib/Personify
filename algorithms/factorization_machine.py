from fastFM import ALS

class FactorizationMachine():
'''
A wrapper around an implementation of Factorization Machines
'''

	def __init__(self):
		self.model = als.FMRegression(n_iter=1000, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)

	def fit(self, features, target);

	def predict(self, features):



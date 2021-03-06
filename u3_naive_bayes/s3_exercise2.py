import numpy as np
from sklearn.naive_bayes import MultinomialNB

np.set_printoptions(precision=6)

class MyMultinomialNB(object):
	def __init__(self, alpha=1.0):
		self.alpha = alpha

	def fit(self, X, y):
		N = X.shape[0]
		# group by class
		separated = [X[np.where(y == i)] for i in np.unique(y)]
		# class prior
		self.class_log_prior_ = [np.log(len(i) / N) for i in separated]
		# count of each term
		count = # Your code here
		return count

X = np.array([
    [2,1,0,0,0,0],
    [2,0,1,0,0,0],
    [1,0,0,1,0,0],
    [1,0,0,0,1,1]
])
y = np.array([0,0,0,1])
nb = MyMultinomialNB().fit(X, y)

print(nb)
assert(np.allclose(nb, np.array([[6,2,2,2,1,1],[2,1,1,1,2,2]])))


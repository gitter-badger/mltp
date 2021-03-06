import numpy as np
from sklearn.naive_bayes import BernoulliNB

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
        count = np.array([np.array(i).sum(axis=0) for i in separated]) + self.alpha
        # log probability of each term
        self.feature_log_prob_ = np.log(count / count.sum(axis=1)[np.newaxis].T)
        return self

    def predict_log_proba(self, X):
        return [(self.feature_log_prob_ * x).sum(axis=1) + self.class_log_prior_
                for x in X]

    def predict(self, X):
        return np.argmax(self.predict_log_proba(X), axis=1)

class MyBernoulliNB(object):
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
        N = X.shape[0]
        # group by class
        separated = [X[np.where(y == i)] for i in np.unique(y)]
        # class prior
        self.class_log_prior_ = [np.log(len(i) / N) for i in separated]
        # count of each term
        count = np.array([np.array(i).sum(axis=0) for i in separated]) + self.alpha

        # number of documents in each class
        smoothing = 2 * self.alpha
        denominator = np.array([len(i) + smoothing for i in separated])
        # probability of each term
        self.feature_prob_ = # Your code here
        return self


X = np.array([
    [2,1,0,0,0,0],
    [2,0,1,0,0,0],
    [1,0,0,1,0,0],
    [1,0,0,0,1,1]
])
y = np.array([0,0,0,1])

nb = MyBernoulliNB(alpha=1).fit(np.where(X > 0, 1, 0), y)
print(nb.feature_prob_)

answer = np.array(
    [[0.8, 0.4, 0.4, 0.4, 0.2, 0.2],
     [0.666667, 0.333333, 0.333333, 0.333333, 0.666667, 0.666667]]
)

assert(np.allclose(nb.feature_prob_, answer))



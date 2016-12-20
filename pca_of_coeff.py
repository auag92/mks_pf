from sklearn.decomposition import RandomizedPCA
from os import listdir
from scipy.io import loadmat
from scipy.io import savemat
import numpy as np
import cPickle as pickle

filenames =  sorted(listdir('coef/'))
coeffs = []
for f in filenames:
    dict_coef = loadmat('coef/' + f)
    coeffs.append(dict_coef[dict_coef.keys()[0]][None])

coeffs = np.concatenate(coeffs)
coeffs = coeffs.reshape(len(coeffs), -1)
print coeffs.shape

pca = RandomizedPCA(n_components=20)
scores = pca.fit_transform(coeffs)
dict_scores = {}
dict_scores['scores'] = scores
pickle.dump(pca, open('pca_model.pkl', 'wb'))
savemat('coeff_scores.mat', dict_scores)

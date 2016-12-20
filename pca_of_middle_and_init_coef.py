from sklearn.decomposition import RandomizedPCA
from os import listdir
from scipy.io import loadmat
from scipy.io import savemat
import numpy as np
import cPickle as pickle

init_filenames =  sorted(listdir('coef/'))
mid_filenames = sorted(listdir('middle_coef/'))
coeffs = []
for f in init_filenames:
    dict_coef = loadmat('coef/' + f)
    coeffs.append(dict_coef[dict_coef.keys()[0]][None])
print len(coeffs)

for f in mid_filenames:
    dict_coef = loadmat('middle_coef/' + f)
    coeffs.append(dict_coef[dict_coef.keys()[0]][None])
print len(coeffs)
coeffs = np.concatenate(coeffs)
coeffs = coeffs.reshape(len(coeffs), -1)
print coeffs.shape

pca = RandomizedPCA(n_components=20)
scores = pca.fit_transform(coeffs)
dict_scores = {}
dict_scores['scores'] = scores
pickle.dump(pca, open('pca_model_mid_and_init.pkl', 'wb'))
savemat('coeff_scores_mid_and_init.mat', dict_scores)

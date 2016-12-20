from pymks.bases import LegendreBasis
from pymks.stats import correlate
from pymks.tools import draw_concentrations
import numpy as np
from os import listdir
from scipy.io import loadmat
from scipy.io import savemat
import cPickle as pickle
from sklearn.decomposition import RandomizedPCA
import matplotlib.pyplot as plt
from pymks.tools import draw_components_scatter

n_samples = 10
corr=[(1, 1)]
l_basis = LegendreBasis(n_states=10, domain=[-1.1, 1.1])
pca = RandomizedPCA(n_components=20)
files = sorted([f for f in listdir('./data') if f[-3:] == 'mat'])[-2:]
print files
X0 = loadmat('data/' + files[0])['data'][:n_samples]
print 'X0', X0.shape
X = np.zeros((len(files) * X0.shape[0],) + X0[0].shape)
print 'X', X.shape
X[:n_samples] = X0
print 'loading data'
for ii, f in enumerate(files[:1]):
    X[(ii + 1) * n_samples:(ii + 2) * n_samples] = loadmat('data/' + f)['data'][:n_samples]

X = X.reshape((2, 10, 95, 95))
X = np.transpose(X, [1, 0, 2, 3])
X = X.reshape((20, 95, 95))


for ii in range(len(X) / 2):
    diff = np.diff(X[ii * 2:(ii) * 2 + 2], axis=0)
    print np.unique(diff)
    # draw_concentrations(X[ii * 2:(ii) * 2 + 2])
print 'X unique', len(np.unique(X))
plt.hist(X.flatten(), bins=100)
plt.show()


plt.hist(np.diff(X, axis=0).flatten(), bins=100)
plt.show()

print 'computting stats...'

X_corr = correlate(X, l_basis, periodic_axes=[0, 1], correlations=corr)

print 'X_corr', X_corr.shape


stats_samples = np.split(X_corr, len(files))

for s, f in zip(stats_samples, files):
    savemat('stats/stats' + f[4:], {'stats': s})

for x in X_corr:
    for s in np.transpose(x, (2, 0, 1)):
        plt.imshow(s)
        plt.show()
print 'n_unique', len(np.unique(X_corr))

print 'doing pca...'
scores = pca.fit_transform(X_corr.reshape((len(X_corr), -1)))
print 'scores', scores.shape
# scores = scores.reshape((2, 10, -1))
# scores = np.transpose(scores, (1, 0, 2))
# scores = scores.reshape((20, -1))
split_scores = np.split(scores[:, :3], 10)
# print [i for i in split_scores]
# print split_scores
draw_components_scatter(split_scores, ['' for i in range(10)])
print 'saving results...'
pickle.dump(scores, open('ch_pca_scores.pkl', 'wb'))
pickle.dump(pca, open('ch_pca_model.pkl', 'wb'))


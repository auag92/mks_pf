from pymks.tools import draw_components_scatter
from pymks.tools import draw_component_variance
import cPickle as pickle
from scipy.io import loadmat
import numpy as np

# #
# pca_model = pickle.load(open('pca_model_mid_and_init.pkl', 'rb'))
# draw_component_variance(pca_model.explained_variance_ratio_)

# scores = loadmat('coeff_scores_mid_and_init.mat')['scores']
# draw_components_scatter([scores[:100, :3], scores[100:400, :3],
#                         scores[400:, :3]],
#                         ['Initial 100', 'Initial Pass 100', 'New Initial'])

# draw_components_scatter([scores[:100, :3], scores[100:400, :3]],
#                         ['Initial 100', 'Initial Pass 100'])


# # # Differences in Coefficients
# scores = loadmat('coeff_scores_mid_and_init.mat')['scores']

# # scores = np.concatenate((scores_dict['coef_0'], scores_dict['coeff_1000']))

# labels = ['First 100', 'Last 300', 'Starting at 300']

# _scores = [scores[:100, :3], scores[100:400, :3], scores[400:, :3]]

# draw_components_scatter(_scores, labels)


scores = pickle.load(open('ch_pca_scores.pkl', 'rb'))[:, :3]

scores = scores.reshape((401, 10, 3))
scores = np.transpose(scores, (1, 0, 2))
scores = scores.reshape((4010, 3))
print scores.shape


scores_split = np.split(scores, 10)
print [i.shape for i in scores_split]
labels = [str(i + 1) for i in range(len(scores_split))]


draw_components_scatter(scores_split, labels)

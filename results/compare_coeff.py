from pymks import MKSLocalizationModel
from os import listdir
from scipy.io import loadmat
from pymks.bases import LegendreBasis
from pymks.datasets import CahnHilliardSimulation
import numpy as np
from pymks.tools import draw_concentrations

sim = CahnHilliardSimulation(gamma=0.4)
means = 0.0008 * np.random.random(1) - 0.0004
X0 = np.concatenate([1e-5 * np.random.randn(1, 95, 95) - m for m in means])

coeff_file = sorted([f for f in listdir('.') if f[:5] == 'coef_'])[-1]
l_basis = LegendreBasis(10, domain=[-1.1, 1.1])


coef = loadmat(coeff_file)['coef_']
model = MKSLocalizationModel(basis=l_basis)

X = X0.copy()
for ii in range(300):
    sim.run(X)
    X = sim.response

model.fit(X0, X)
model.coef_ = coef

X_pred = model.predict(X0)

print X_pred.shape
print X.shape

draw_concentrations([X_pred[0], X[0]])

draw_concentrations([X_pred[0] - X[0]])

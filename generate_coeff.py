from pymks.datasets import CahnHilliardSimulation
from pymks import LegendreBasis
from mks_localization_model_sparse import MKSLocalizationModel
from scipy.io import savemat
import numpy as np

l_basis     = LegendreBasis(n_states=10, domain=[-1.1, 1.1])
model       = MKSLocalizationModel(l_basis)
sim         = CahnHilliardSimulation(gamma=0.4)

np.random.seed(1)
means       = 0.0008 * np.random.random(500) - 0.0004
X0          = np.concatenate([1e-5 * np.random.randn(1, 95, 95) - m for m in means])
X           = X0.copy()
savemat('data/data_step_0000', {'data': X})

for ii in range(4000):
    sim.run(X)
    X   =   sim.response
    if (ii + 1) % 10 == 0:
        step    = str(ii + 1)
        for q in range(4 - len(step)):
            step = '0' + step
        print(step)
        model.fit(X0, X)
        savemat('coef/coef_step_' + step, {'coef_': model.coef_})
        savemat('data/data_step_' + step, {'data': X})
